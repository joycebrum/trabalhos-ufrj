import glob, os, re
from nltk.stem.lancaster import LancasterStemmer

def generate_tokens(clean_str, separators):
    music = clean_str.split('\n', 2)
    tokens = re.split('|'.join(separators), music[2])
    return music[0], music[1], [t for t in tokens if t]

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

def get_term_list():
    stopwords = ['of', 'the', 'a', 'an', 'on', 'in', 'out', 'under', 'am', 'is', 'are', 'was', 'were', '\'m', '\'re', '\'ll', '\'s', 'and', 
    'oh', 'to', 'but', '\'']
    separators = clean_separators([' ',',','.','!','?',':',';','/','\\n', '\''])
    os.chdir("./music files")
    musics = []
    for file_name in glob.glob("*.txt"):
        file = open(file_name)
        content = remove_stop_words(file.read().lower(), stopwords)
        music = {}
        music['name'], music['singer'], music['terms'] = generate_tokens(content, separators)
        music['name_terms'] = stemming(music['name'].split())
        music['terms'] = stemming(music['terms'])
        musics.append(music)
    return musics
