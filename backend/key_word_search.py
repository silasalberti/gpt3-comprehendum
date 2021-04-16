#stopwörter
#fragewörter
#Satzzeichen
#

def create_absätze(file_name):
    #params:
    #file_name: string in format file.txt

    #returns: a list of strings, where each string represents one absatz
    #(Absatz defined as line == \n with the line before that ending on a point)

    file = open(file_name, 'r')
    read_lines = file.readlines()

    lines = [line for line in read_lines]

    absätze = []
    last_absatz_index = 0
    for index, line in enumerate(lines):
        if line == '\n':
            if lines[index-1].endswith('.\n'):
                absätze.append(lines[last_absatz_index:index])
                last_absatz_index = index
    return [''.join(_) for _ in absätze]

def find_word(absätze, word):
    #params:
    #absätze: a list of strings, where each string represents one absatz
    #word: lowercase string with the word to search for

    #returns: a list of ints where count[i] is how often the word appears in absätze[i]
    counts = []
    for i in absätze:
        counts.append(i.lower().count(word))
    print(counts)
    return counts 



absätze = create_absätze('backend/Handbook.txt')

find_word(absätze, 'siemens')
