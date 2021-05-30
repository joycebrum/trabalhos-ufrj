from neo4j import GraphDatabase
from bottle import get, run, request, response, static_file

class Example:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    def close(self):
        self.driver.close()

    @get("/")
    def get_index(self):
        return static_file("index.html", root="static")


if __name__ == "__main__":
    example = Example("bolt://localhost:7687", "neo4j", "130598")
    print(example.get_index())
    print("Sucesso")
    example.close()