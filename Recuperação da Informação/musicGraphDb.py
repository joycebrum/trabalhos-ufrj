from bottle import get, run, request, response, static_file
import json
import dbOperations as db
import bm25

@get("/")
def get_index():
    return static_file("./index.html", root="static")

@get("/graph")
def get_graph():
    response.content_type = "application/json"
    return json.dumps(db.get_graph())

@get("/search")
def get_search():
    try:
        q = request.query["q"]
        results = bm25.search(q)
    except KeyError:
        results = db.all_musics()

    response.content_type = "application/json"
    return json.dumps([{"music": { 'name': row["name"], 'singer': row['singer']}} for row in results])

@get("/lyrics/<name>/<singer>")
def get_lyrics(name, singer):
    result = db.get_lyric(name, singer)
    response.content_type = "application/json"
    return json.dumps(result)

if __name__ == "__main__":
    run(port=8080)
    db.close()