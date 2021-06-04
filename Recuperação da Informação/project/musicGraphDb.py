from neo4j import GraphDatabase
from bottle import get, post, run, request, response, static_file
from py2neo import Graph
import termStemming as stemm

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "130598"), encrypted=False)
graph = Graph(password = "130598")

def close():
    driver.close()
    
@get("/")
def get_index():
    return static_file("index.html", root="static")

@get("/graph")
def get_graph():
    results = graph.run(
    "MATCH (t:Term)-[:APPEARS_IN]->(m:Music) "
    "RETURN t, m ")
    return results

@get("/musics")
def get_musics():
    results = graph.run(
    "MATCH (m:Music) RETURN m ")
    return results

@post("/music/<name>/<singer>")
def create_music(name, singer):
    return graph.run(
        "MERGE (a:Music {name:'%s', singer:'%s'}) RETURN a" %(name, singer)
    )

@post("/term/<term>")
def create_term(term):
    return graph.run(
        "MERGE (t:Term {value:'%s'}) RETURN t" %(term)
    )

@post("/<term>/<relevance>/appearsin/<name>/<singer>")
def create_associate(term, relevance, name, singer):
    return graph.run(
        "MATCH (m:Music {name:'%s', singer: '%s'}), (t:Term {value:'%s'}) "
        "MERGE (t)-[r:APPEARS_IN]->(m) SET r.relevance = %s "
        "RETURN t,r,m" %(name, singer, term, relevance)
    )


@post("destroy")
def destroy_all():
    print('Destruindo todo o banco de dados...')
    results = graph.run(
        "MATCH (n) DETACH DELETE n"
    )
    print('Banco de dados destruído\n')

#call it once just if you need to initiate de database
def initiateDb():
    destroy_all()
    musics = stemm.get_term_list()
    for music in musics:
        create_music(music['name'], music['singer'])
        for term in music['name_terms']:
            create_term(term)
            create_associate(term, 0, music['name'], music['singer'])
        for term in music['singer'].split():
            create_term(term)
            create_associate(term, 1, music['name'], music['singer'])
        for term in music['terms']:
            create_term(term)
            create_associate(term, 2, music['name'], music['singer'])
    print('Banco de Dados criado com sucesso!')


if __name__ == "__main__":
    # initiateDb() # it is commented to avoid initialize already initialied DB
    run(port=8080)
    # example.destroy_all()
    # print(create_music('Love Story', 'Taylor Swift'))
    # print(get_musics())
    # print("Sucesso")
    # example.close()