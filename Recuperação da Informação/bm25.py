import dbOperations as db
import termStemming as stemm
import math

K1 = 1
b = 0.75
def init_search (query_string):
    query = stemm.pre_process(query_string)
    documents = db.all_musics()
    N = db.number_of_documents()
    avg_doclen = db.total_occurrences()/N
    n = [db.number_documents_with_term(q) for q in query]
    return query, documents, N, avg_doclen, n

def get_relevance_document_rank(N, n, avg_doclen, doc, query):
    #to do think a way to use the relevance on BM25
    print('do nothing')
    return 0

def search_with_relevance(query_string):
    query, documents, N, avg_doclen, n = init_search(query_string)
    for document in documents:
        doclen = db.document_len(document['id'])
        document['rank'] = get_relevance_document_rank(N, n, avg_doclen, {'len': doclen, 'id': document['id']}, query)
    return sorted(documents, key=lambda k: k['rank'], reverse=True)

def get_document_rank(N, n, avg_doclen, doc, query):
    soma = 0
    i = 0
    for q in query:
        fij = db.term_frequency_in_document(doc['id'], q)
        temp = (1-b) + b*(doc['len']/avg_doclen)
        Bij = ( (K1 + 1)*fij ) / (K1*temp + fij)
        pre_log_value = (N-n[i]+0.5)/(n[i]+0.5)
        soma += Bij * math.log(pre_log_value, 2)
        i += 1
    return soma

def search(query_string):
    query, documents, N, avg_doclen, n = init_search(query_string)
    for document in documents:
        doclen = db.document_len(document['id'])
        document['rank'] = get_document_rank(N, n, avg_doclen, {'len': doclen, 'id': document['id']}, query)
    return sorted(documents, key=lambda k: k['rank'], reverse=True)

if __name__ == "__main__":
    res = search('lov story')
    for r in res:
        print(r['name'], r['rank'])
