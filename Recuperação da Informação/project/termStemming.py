import glob, os, re
from nltk.stem.lancaster import LancasterStemmer

def generate_tokens(music, separators):
    tokens = re.split('|'.join(separators), music)
    return [t for t in tokens if t]

def clean_separators(separators):
    for i in range(0, len(separators)):
        if separators[i] in ['?','\\','/', '.'] :
            separators[i]= "\\" + separators[i]
    return separators

def remove_stop_words(music, stopwords):
    remove = '|'.join(stopwords) 
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    return regex.sub("", music)

# function to get unique values
def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    return list(list_set)

def stemming(terms):
    st = LancasterStemmer()
    return unique([st.stem(term) for term in terms])


def pre_process(string):
    stopwords = ['of', 'the', 'a', 'an', 'on', 'in', 'out', 'under', 'am', 'is', 'are', 'was', 'were', '\'m', '\'re', '\'ll', '\'s', '\'ve', 'and', 
    'oh', 'oh-oh', 'to', 'but', '\'', 'yeah']
    separators = clean_separators([' ',',','.','!','?',':',';','/','-','\\n', '\'', '\"', '\(', '\)'])
    terms = remove_stop_words(string.lower(), stopwords)
    terms = generate_tokens(terms, separators)
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