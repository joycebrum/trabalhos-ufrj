from neo4j import GraphDatabase
from py2neo import Graph

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "130598"), encrypted=False)
graph = Graph(password = "130598")

def close():
    driver.close()

def get_graph():
    return graph.run(
    "MATCH (t:Term)-[:APPEARS_IN]->(m:Music) "
    "RETURN t, m ")

def search(q):
    return graph.run(
        "MATCH (m:Music)-[r:BELONGS_TO]->(s:Singer) "
        "RETURN ID(m) as id, m.name as name, s.name as singer")
        # "WHERE music.name =~ {title} "
        # "RETURN movie", {"title": "(?i).*" + q + ".*"})

def get_lyric(name, singer):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"})-[r:BELONGS_TO]->(s:Singer {name: \"%s\"}) RETURN m.lyrics as lyrics" %(name, singer)
    ).evaluate()

def find_music(name, singer):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"})-[r:BELONGS_TO]->(s:Singer {name: \"%s\"}) RETURN ID(m) as id, m.name as name, s.name as singer" %(name, singer)
    ).data()

def total_occurrences():
    return graph.run("MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) RETURN count(r)").evaluate()

def number_of_documents():
    return graph.run("MATCH (m:Music) RETURN count(m)").evaluate()

def document_len(document_id):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE ID(m) = %s "
        "RETURN count(r)" %(document_id)
    ).evaluate()

def number_documents_with_term(term):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE t.value = \"%s\" "
        "RETURN count(m)" %(term)
    ).evaluate()

def term_frequency_in_document(document_id, term):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE ID(m) = %s and t.value = \"%s\" "
        "RETURN count(r)" %(document_id, term)
    ).evaluate()

def create_singer(name):
    return graph.run(
        "MERGE (s:Singer {name:'%s'}) RETURN s" %(name)
    )

def create_music(name, lyrics):
    return graph.run(
        "MERGE (a:Music {name:\"%s\", lyrics: \"%s\"}) RETURN a" %(name, lyrics)
    )

def create_term(term):
    return graph.run(
        "MERGE (t:Term {value:'%s'}) RETURN t" %(term)
    )

def create_term_music_association(term, relevance, name):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"}), (t:Term {value:'%s'}) "
        "CREATE (t)-[r:APPEARS_IN]->(m) SET r.relevance = %s "
        "RETURN t,r,m" %(name, term, relevance)
    )

def create_singer_association(music, singer):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"}), (s:Singer {name:'%s'}) "
        "MERGE (m)-[r:BELONGS_TO]->(s) "
        "RETURN m,r,s" %(music, singer)
    )

def destroy_all():
    print('Destruindo todo o banco de dados...')
    results = graph.run(
        "MATCH (n) DETACH DELETE n"
    )
    print('Banco de dados destruído\n')

