from multi_rake import Rake

def create_absatze(file_name):
    #params:
    #file_name: string in format file.txt

    #returns: a list of strings, where each string represents one absatz
    #(Absatz defined as line == \n with the line before that ending on a point)

    file = open(file_name, 'r')
    read_lines = file.readlines()

    lines = [line for line in read_lines]

    absatze = []
    last_absatz_index = 0
    for index, line in enumerate(lines):
        if line == '\n':
            if lines[index-1].endswith('.\n'):
                absatze.append(lines[last_absatz_index:index])
                last_absatz_index = index
    return [''.join(_) for _ in absatze]

def find_word(absatze, word):
    #params:
    #absatze: a list of strings, where each string represents one absatz
    #word: lowercase string with the word to search for

    #returns: a list of touple, with (index, how often it appears); list is orderd with the highes number of 
    #counts first
    counts = []
    for index,i in enumerate(absatze):
        counts.append((index, i.lower().count(word)))
    return counts 

def get_keywords(question):
    rake = Rake()
    keywords = rake.apply(question)
    return [_[0] for _ in keywords]

import pickle
def safe_list(file_name, lst):
    with open(file_name, "wb") as fp:   #Pickling
        pickle.dump(lst, fp)
    
def get_list(file_name):
    with open(file_name, "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    
    return b

def get_length(dic):
    length = 0
    for key in dic.keys():
        for i in dic[key]:
            length = length + len(i[1])
    return length


import itertools
def get_absatze(question, absatze):
    key_words = get_keywords(question)
    dic = {}
    for word in key_words:
        if length(dic) <= 4000:
            lst = find_word(absatze, word)
            dic[word] = [(j,absatze[i]) for i, j in enumerate(lst) if j !=0]
            print([(j,'test') for i, j in enumerate(lst) if j !=0])
    
    length = get_length(dic)

    if length == 0:
        List_1 = [i.split(' ') for i in key_words]
        key_words = list(itertools.chain(*List_1))
        dic = {}
        for word in key_words:
            lst = find_word(absatze, word)
            dic[word] = [(j,absatze[i]) for i, j in enumerate(lst) if j !=0]
    
    print(dic)
    #while get_length(dic) >= 4000:


    return dic


absatze1 = create_absatze('Handbook.txt')

safe_list('Handbook_absatz.txt',absatze1)

absatze2 = create_absatze('Sample_Contract.txt')

safe_list('Sample_Contract_absatz.txt',absatze2)

absatze3 = create_absatze('BCGs.txt')

safe_list('BCGs_absatz.txt',absatze3)


absatze = get_list('Handbook_absatz.txt') + get_list('BCGs_absatz.txt') + get_list('Sample_Contract_absatz.txt')

questions = ['What is bribery?', 'What are the Supplier’s obligation in case of late delivery?', 'What are the Supplier’s obligation in case of not meeting the delivery date?',
'Where is the seat of arbitration?', 'Which law does apply?', 'Is a earthquake a force majeure event?', 
'What does the global key account management do?', 'Are gifts of money allowed?', 'What is the Compliance Review Board? What is CRB?',
'Who needs to participate in Compliance Review Board (CRB)?', '"Where can I report compliance cases? Where can I report compliance violations?"']

#questions = ['What are the Supplier’s obligation in case of late delivery?'] 
'''
for question in questions:
    print(question)
    dic = get_absatze(question, absatze)
    for key in dic.keys():
        length = 0
        for i in dic[key]:
            length = length + len(i[1])
    
    print(length)'''