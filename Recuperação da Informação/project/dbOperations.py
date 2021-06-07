from neo4j import GraphDatabase
from py2neo import Graph

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "130598"), encrypted=False)
graph = Graph(password = "130598")

def close():
    driver.close()

def get_graph():
    results = graph.run(
        "MATCH (m:Music)-[:BELONGS_TO]->(s:Singer) "
        "RETURN m.name as music, s.name as singer "
        "LIMIT %s" %(100))
    nodes = []
    rels = []
    i = 0
    print(results)
    for music, singer in results:
        nodes.append({"name": music, "label": "movie"})
        target = i
        i += 1
        singer = {"name": singer, "label": "singer"}
        try:
            source = nodes.index(singer)
        except ValueError:
            nodes.append(singer)
            source = i
            i += 1
        rels.append({"source": source, "target": target})
    return {"nodes": nodes, "links": rels}

def search(q):
    return graph.run(
        "MATCH (m:Music)-[r:BELONGS_TO]->(s:Singer) "
        "RETURN ID(m) as id, m.name as name, s.name as singer").data()
        # "WHERE music.name =~ {title} "
        # "RETURN movie", {"title": "(?i).*" + q + ".*"})

def all_musics():
    return graph.run(
        "MATCH (m:Music)-[r:BELONGS_TO]->(s:Singer) "
        "RETURN ID(m) as id, m.name as name, s.name as singer").data()

def get_lyric(name, singer):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"})-[r:BELONGS_TO]->(s:Singer {name: \"%s\"}) RETURN m.lyrics as lyrics" %(name, singer)
    ).evaluate()

def find_music(name, singer):
    return graph.run(
        "MATCH (m:Music {name:\"%s\"})-[r:BELONGS_TO]->(s:Singer {name: \"%s\"}) RETURN ID(m) as id, m.name as name, s.name as singer" %(name, singer)
    ).data()

def total_occurrences():
    return graph.run("MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) RETURN count(DISTINCT r)").evaluate()

def number_of_documents():
    return graph.run("MATCH (m:Music) RETURN count(m)").evaluate()

def document_len(document_id):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE ID(m) = %s "
        "RETURN count(DISTINCT r)" %(document_id)
    ).evaluate()

def number_documents_with_term(term):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE t.value = \"%s\" "
        "RETURN count(DISTINCT m)" %(term)
    ).evaluate()

def term_frequency_in_document(document_id, term):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE ID(m) = %s and t.value = \"%s\" "
        "RETURN count(r)" %(document_id, term)
    ).evaluate()

def term_frequency_in_document_with_relevance(document_id, term):
    return graph.run(
        "MATCH (t:Term)-[r:APPEARS_IN]->(m:Music) "
        "WHERE ID(m) = %s and t.value = \"%s\" "
        "RETURN r.relevance as relevance, count(*) as quant" %(document_id, term)
    ).data()

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
