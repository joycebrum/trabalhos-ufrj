import glob, os, re
from nltk.stem.lancaster import LancasterStemmer

def separate(music, separators):
    tokens = re.split('|'.join(separators), music)
    return [t for t in tokens if t]

def clean_separators(separators):
    for i in range(0, len(separators)):
        if separators[i] in ['?','\\','/', '.'] :
            separators[i]= "\\" + separators[i]
    return separators

def remove_stop_words(terms, stopwords):
    return [term for term in terms if term not in stopwords]

def stemming(terms):
    st = LancasterStemmer()
    return [st.stem(term) for term in terms]

def generate_tokens(string):
    stopwords = ['of', 'the', 'a', 'an', 'on', 'in', 'out', 'under', 'am', 'is', 'are', 'was', 'were', 'm', 're', 'll', 's', 've', 't', 'and', 
    'oh', 'to', 'but', 'yeah']
    separators = clean_separators([' ',',','.','!','?',':',';','/','-','\\n', '\'', '\"', '\(', '\)'])
    terms = separate(string.lower(), separators)
    return remove_stop_words(terms, stopwords)

def pre_process(string):
    terms = generate_tokens(string)
    return stemming(terms)

def get_term_list():
    os.chdir("./music files")
    musics = []
    for file_name in glob.glob("*.txt"):
        file_content = open(file_name).read().split('\n', 2)
        music = {}
        music['name'], music['singer'], music['lyrics'] = file_content[0], file_content[1], file_content[2]
        music['name_terms'] = pre_process(music['name'])
        music['terms'] = pre_process(file_content[2].lower())
        musics.append(music)
    return musics

if __name__ == "__main__":
    terms = get_term_list()
    for row in terms:
        print(row['name'], '-', row['singer'])
        print(row['name_terms'])
        print(row['terms'])
        print('')
    print(len(terms), 'documentos processados.')