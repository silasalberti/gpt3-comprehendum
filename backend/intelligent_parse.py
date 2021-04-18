import pandas as pd
from docx import Document

def get_lst():
    df = pd.read_excel('Sample_Questions_Compliance.xls')
    lst = []
    
    for index, row in df.iterrows():
        lst.append((row['Model Question'], row['Additional Tags / Synonyms for questions (from QnA Chatbot)'],row['Model Answer']))

    wordDoc = Document('Sample_Questions_Legal.docx')

    for table in wordDoc.tables:
        for row in table.rows:
            sub = [0,'',0]
            i = 0
            for cell in row.cells:
                try:
                    int(cell.text)
                except Exception as e:
                    if i in [0, 1]:
                        if i == 0:
                            sub[i] = cell.text
                        if i == 1:
                            sub[i+1] = cell.text
                    if cell.text != '':
                        i = i + 1
            lst.append(tuple(sub))

    return lst


def str_in_lst(quest, lst):
    for i in lst:
        if quest in i[0]:
            return i[2]
        elif quest in str(i[1]):
            return i[2]
    else:
        return False


    
    
#print(get_lst())
