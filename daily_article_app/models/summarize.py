from typing import List
from textrankr import TextRank

class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens

def summarize_txt(text, k):
    mytokenizer: MyTokenizer = MyTokenizer()
    textrank: TextRank = TextRank(mytokenizer)

    k : int = 3

    summarized: str = textrank.summarize(text, k)
    return summarized
