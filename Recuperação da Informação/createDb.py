import dbOperations as db
import termStemming as stemm

#call it once just if you need to initiate de database
def initiateDb():
    db.destroy_all()
    musics = stemm.get_term_list()
    print('Criando banco de dados...')
    for music in musics:
        db.create_singer(music['singer'])
        db.create_music(music['name'], music['lyrics'])
        db.create_singer_association(music['name'], music['singer'])
        for term in music['terms']:
            db.create_term(term)
            db.create_term_music_association(term, 2, music['name'])
        for term in music['singer'].lower().split():
            db.create_term(term)
            db.create_term_music_association(term, 1, music['name'])
        for term in music['name_terms']:
            db.create_term(term)
            db.create_term_music_association(term, 0, music['name'])
    print('Banco de Dados criado com sucesso!')

if __name__ == "__main__":
    initiateDb()
    db.close()