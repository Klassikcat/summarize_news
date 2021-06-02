from typing import List
from textrankr impot TextRank

def summarize_txt(text, k):
    mytokenizer: MyTokenizer = MyTokenizer()
    textrank: TextRank = TextRank(mytokenizer)

    k : int = 3

    summarized: str = textrank.summarize(text, k)
    return summarized
