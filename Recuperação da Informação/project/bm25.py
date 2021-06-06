import dbOperations as db

K1 = 1
b = 0.75

if __name__ == "__main__":
    music = db.find_music('Love Story', 'Taylor Swift')
    print(music[0]['id'])
    print('len(dj) =', db.document_len(music[0]['id']))
    print('avg_doclen =', db.total_occurrences()/db.number_of_documents())
    print('N =', db.number_of_documents())
    print('ni =', db.number_documents_with_term('lov'))
    print('fij=', db.term_frequency_in_document(music[0]['id'], 'lov'))