import pandas as pd


def get_lst():
    df = pd.read_excel('backend/Sample_Questions_Compliance.xls')
    lst = []
    for index, row in df.iterrows():
        lst.append((row['Model Question'], row['Additional Tags / Synonyms for questions (from QnA Chatbot)'],row['Model Answer']))
    return lst

def str_in_lst(question, lst):
    for i in lst:
        if question in i[0]:
            return i[2]
        elif question in str(i[1]):
            return i[2]
    else:
        return False