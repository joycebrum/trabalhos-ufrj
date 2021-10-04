import math
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# para poder carregar uma malha .obj:
loadPrcFileData("","load-file-type p3assimp")

# deativar caching (para que o panda3D não use dados "velhos"):
cache = BamCache.get_global_ptr()
cache.set_active(False)


class MeuApp(ShowBase):
    def __init__(self):
        '''Abre a janela, cria um gráfo de cena e prepara tudo que é preciso
        para renderizar essa cena na janela. Define a luz da cena, chama um
        método que carrega malhas em formato .obj e mapea texturas nelas. Chama 
        também um método que define a câmera e o movimento/setting dela.'''
        ShowBase.__init__(self)
        self.carregarModelos()

        # definir luz e sombra:
        alight = AmbientLight('Ambient')
        alight.setColor((0.4, 0.4, 0.4, 1))
        alnp = self.render.attachNewNode(alight)
        self.render.setLight(alnp)
        
        plight = PointLight('plight')
        plight.setColor((0.6, 0.6, 0.6, 1))
        plight.setShadowCaster(True, 2048, 2048)
        self.render.setShaderAuto()
        plnp = self.render.attachNewNode(plight)
        plnp.setPos(2, 6, 3)
        self.render.setLight(plnp)
    
        # desativar trackball controle de camera:
        base.disableMouse()
        # chamar o método dollyZoomTask cada frame:
        self.taskMgr.add(self.dollyZoomTask, "DollyZoomTask")


        
    ##========== Método que carrega as malhas ========== 
    def carregarModelos(self):
        '''Carrega malhas em formato .obj e mapea texturas nelas. Especifica
        a posição, escalonamento e a orientação dos modelos. Coloca os modelos
        no grafo de cena usando o método reparentTo.'''

        self.fundo = self.loader.loadModel("esquina_tex.obj")
        tex = loader.loadTexture('esquina.png')
        self.fundo.setTexture(tex,1)
        self.fundo.reparentTo(self.render) # fazendo a malha visível

        self.bush1 = self.loader.loadModel("arbusto.obj")
        tex = loader.loadTexture('arbusto.jpg')
        self.bush1.setTexture(tex, 1)
        self.bush1.setScale(0.008, 0.008, 0.008) # escalonamento X, Y, Z
        self.bush1.setPos(1.5,-1,0) # posicao (X,Y,Z)
        self.bush1.reparentTo(self.render) # fazendo a malha visível

        self.bush2 = self.loader.loadModel("arbusto.obj")
        tex = loader.loadTexture('arbusto.jpg')
        self.bush2.setTexture(tex, 1)
        self.bush2.setScale(0.008, 0.008, 0.008) # escalonamento X, Y, Z
        self.bush2.setPos(1,-2,0) # posicao (X,Y,Z)
        self.bush2.reparentTo(self.render) # fazendo a malha visível

        self.house = self.loader.loadModel("house.obj")
        tex = loader.loadTexture('cottage_diffuse.png')
        self.house.setTexture(tex, 1)
        self.house.setScale(0.0008, 0.0008, 0.0008) # escalonamento X, Y, Z
        self.house.setPos(-1,-4,0) # posicao (X,Y,Z)
        self.house.setHpr(180,90,0) # rotacao em volta de Z, X, Y
        self.house.reparentTo(self.render) # fazendo a casa visível

        self.bob = self.loader.loadModel("bob190k_tex.obj")
        tex = loader.loadTexture('bob_diffuse.png')
        self.bob.setTexture(tex,1)
        self.bob.setScale(1, 1, 1) # escalonamento X, Y, Z 
        #self.bob.setHpr(90,0,0) # rotacao em volta de Z, X, Y
        self.bob.setPos(1,-4,0) # posicao (X,Y,Z)
        self.bob.reparentTo(self.render)
 
        self.spot1 = self.loader.loadModel("spot190k_tex.obj")
        tex = loader.loadTexture('spot_purple.png')
        self.spot1.setTexture(tex,1)
        self.spot1.setScale(0.4, 0.4, 0.4) 
        self.spot1.setPos(1,-1,0) 
        self.spot1.reparentTo(self.render)

        self.spot2 = self.loader.loadModel('spot190k_tex.obj')
        tex = loader.loadTexture('spot_yellow.png')
        self.spot2.setTexture(tex,1)
        self.spot2.setScale(0.4, 0.4, 0.4) 
        self.spot2.setPos(0.5,-2,0)
        self.spot2.reparentTo(self.render)

        self.spot3 = self.loader.loadModel('spot190k_tex.obj')        
        tex = loader.loadTexture('spot_pink.png')
        self.spot3.setTexture(tex,1)
        self.spot3.setScale(0.4, 0.4, 0.4) 
        self.spot3.setPos(0,-1,0)
        self.spot3.reparentTo(self.render)

        self.bush3 = self.loader.loadModel("arbusto.obj")
        tex = loader.loadTexture('arbusto.jpg')
        self.bush3.setTexture(tex, 1)
        self.bush3.setScale(0.008, 0.008, 0.008) # escalonamento X, Y, Z
        self.bush3.setPos(-0.5,-2,0) # posicao (X,Y,Z)
        self.bush3.reparentTo(self.render) # fazendo a malha visível

        self.bush4 = self.loader.loadModel("arbusto.obj")
        tex = loader.loadTexture('arbusto.jpg')
        self.bush4.setTexture(tex, 1)
        self.bush4.setScale(0.008, 0.008, 0.008) # escalonamento X, Y, Z
        self.bush4.setPos(-1,-2,0) # posicao (X,Y,Z)
        self.bush4.reparentTo(self.render) # fazendo a malha visível
   
        

    ##========== Método que define o movimento de camera ========== 
    def dollyZoomTask(self, tarefa):
        '''
            O método diminui o ângulo de visão (FOV) de uma câmera enquanto
        movimenta verticalmente a mesma. Dessa forma, no ponto mais alto da
        da câmera, tem-se a impressão de um zoom-out enquanto que no ponto
        mais baixo da câmera tem-se a impressão de um zoom-in.
        '''
        deslocamento = 4 * abs(math.cos(tarefa.time/2))
        # altura da câmera, varia ciclicamente entre 0.75 e 4.75
        zpos = 0.75 + deslocamento
        
        largura = 4
        # tarefa.time retorna o tempo que se passou em segundos, a funcao
        # math.cos é usada para criar um movimento periódico
        # FOV de 10 a 50 
        FOV =  10 + 50 * abs(math.cos(tarefa.time/2))

        self.camera.lookAt(0,-1,0.5)

        
        self.camera.setPos(0, 4, zpos)
        base.camLens.setFov(FOV)
        return tarefa.cont


aula4 = MeuApp()
# última linha: metódo run renderiza a janela e trata as background tarefas:
aula4.run()
