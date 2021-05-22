import rpyc
from rpyc.utils.server import ThreadedServer
import hashlib

CHORD_PORT = 9100

class ChordRing(rpyc.Service):
    exposed_aux = 9
    def __init__(self):
        self.nodes = [[] for x in range(0,16)]
    def on_connect(self, conx):
        print("Conexão estabelecida com Chord")
    def on_disconnect(self, conx):
        print("Conexão encerrada com Chord")
    def exposed_hash_function(self, identifier):
        return int(hashlib.sha1(str(identifier).encode('utf-8')).hexdigest(), 16) % 16
    def exposed_add_node(self, identifier):
        key = self.exposed_hash_function(identifier)
        self.nodes[key].append(identifier)
        return key
    def exposed_get_ring(self):
        return self.nodes
    def exposed_get_successor(self, key):    
        j = key
        for i in range(0, 16):
            j = (j + 1) % 16
            if len(self.nodes[j]) > 0:
                return j, self.nodes[j]
    def exposed_get_finger_table(self, n):
        finger=[]   
        for k in range(0, 4):
            successor = (n + pow(2, k)) % 16
            if not self.nodes[successor]:
                successor, content = self.exposed_get_successor(successor)
            finger.append(successor)
        return finger
    def exposed_get_address_node(self, key):
        if self.nodes[key]:
            return self.nodes[key][0]
        else:
            return None
    def exposed_search_in_node(self, pos, identifier):
        if pos >= 0  and pos < 16:
            if identifier in self.nodes[pos]:
                return 'É o identificador do nó ' + str(pos)
            for element in self.nodes[pos]:
                if type(element) is tuple:
                    if identifier == element[0]:
                        return element[1]
        return False
    def exposed_insert(self, key, value):
        pos = self.exposed_hash_function(key)
        if not self.nodes[pos]:
            pos = self.exposed_get_successor(pos)[0]
        self.nodes[pos].append((key, value))
        return pos
    
class Process(rpyc.Service):
    exposed_aux = 10
    def __init__(self, identifier, chord): 
        self.identifier = identifier
        self.chord = chord
        self.key = self.chord.root.add_node(identifier)
        self.successor = None
        self.finger_table = []
    def on_connect(self, conx):
    	print("Conexao estabelecida com Process.")
    def on_disconnect(self, conx):
    	print("Conexao encerrada com Process.")
    	
    def exposed_identifier(self):
        return self.identifier
    def exposed_get_ring(self):
        return self.chord.root.get_ring()

    def is_in_circular_interval(self, x, a, b):
        if b < a: #circular case
            return x > a and b <= x
        else:
            return x > a and x <= b
    def closest_preceding_node(self, key):
        m = len(self.finger)-1
        for i in range(m, -1, -1):
            #if finger[i] e (self.key, key) not including key
            if self.finger[i] < key and self.is_in_circular_interval(self.finger[i], self.key, key):
                return self.finger[i]
        return self.successor[0]
    def exposed_find_successor(self, identifier):
        if not self.successor:
            self.successor = self.chord.root.get_successor(self.key)
            self.finger = self.chord.root.get_finger_table(self.key)
            print('Finger table para o nó:', self.key, self.finger)
        key = self.chord.root.hash_function(identifier)
        
        if self.is_in_circular_interval(key, self.key, self.successor[0]):
            return self.successor[0]
        else:
            preceding_pos = self.closest_preceding_node(key)
            print('Buscando', key, ' Atual', self.key, ' Predecessor', preceding_pos)
            endr = self.chord.root.get_address_node(preceding_pos)
            if endr:
                endr = endr.split(':')
                successor_node = rpyc.connect(endr[0], endr[1])
                ans = successor_node.root.find_successor(identifier)
                return ans
        return None
    def exposed_search_identifier(self, identifier):
        position = self.exposed_find_successor(identifier)
        if position:
            value = self.chord.root.search_in_node(position, identifier)
            if value: return position, value
        return None

    def exposed_insert(self, key, value):
        return self.chord.root.insert(key, value)
        

def run_chord():
    chord = ThreadedServer(ChordRing(), port = CHORD_PORT)
    chord.start()
