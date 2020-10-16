import re
import requests

from nltk.corpus import wordnet
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

TRANSLATE_URL = 'https://translate.google.cn/translate_a/single?client=gtx&dt=t&ie=UTF-8&oe=UTF-8&sl=zh-CN&tl=EN&q='

zh_words = '欢乐斗地主是腾讯公司开始的一款实时对战棋牌手游，玩家可以使用手机在线斗地主，拥有多种斗地主游戏模式，您可以与百万游戏玩家一起畅玩游戏，还可以和好友拼倍数、拼财富！'

print(zh_words)
print(len(zh_words))
print()

print(f'TRANSLATING: {TRANSLATE_URL}{zh_words}')
res = requests.get(f'{TRANSLATE_URL}{zh_words}')

translated_words_to_english = ''
for translation in res.json()[0]:
    translated_words_to_english += f'{translation[0]} '
print(f'TRANSLATED: {translated_words_to_english}')
print()

TRANSLATE_URL = 'https://translate.google.cn/translate_a/single?client=gtx&dt=t&ie=UTF-8&oe=UTF-8&sl=EN&tl=zh-CN&q='
res = requests.get(f'{TRANSLATE_URL}{translated_words_to_english}')
translated_words_from_en_to_zh = ''
for translation in res.json()[0]:
    translated_words_from_en_to_zh += f'{translation[0]}'

print('ORIGINAL SENTENCE:')
print(zh_words)
print('PROCESSED USING GOOGLE TRANSLATE:')
print(print(translated_words_from_en_to_zh))
print()

for word in translated_words_to_english.split(' '):
    word = word.lower()
    if word:
        syns = wordnet.synsets(word)
        try:
            print(f'{word} --- {syns}')
        except IndexError:
            print(word)

tokenized = word_tokenize(translated_words_to_english)
print(tokenized)
print(pos_tag(tokenized))
tag_to_process = {'PRP$', 'RB', 'RBR', 'RBS', 'JJ', 'JJR', 'UH', 'JJS', 'VB', 'VBD', 'VBZ', 'NNP', 'NNPS', 'WRB', 'VBG', 'VBP'}
processed_words = ''
for text, tag in pos_tag(tokenized):
    synonym = ''
    if tag in tag_to_process:
        text = text.lower()
        syns = wordnet.synsets(text)
        for syn in syns:
            if syn.lemmas()[0].name() == text or syn.lemmas()[0].name() in text:
                continue
            synonym = syn.lemmas()[0].name()
            break

        if synonym:
            processed_words += f'{synonym} '
        else:
            processed_words += f'{text} '
    else:
        processed_words += f'{text} '
    print(f'{text},{tag},{synonym}')

print()
print(processed_words)
TRANSLATE_URL = 'https://translate.google.cn/translate_a/single?client=gtx&dt=t&ie=UTF-8&oe=UTF-8&sl=EN&tl=zh-CN&q='
res = requests.get(f'{TRANSLATE_URL}{processed_words}')
print('ORIGINAL SENTENCE:')
print(zh_words)
print('PROCESSED USING NLTK:')
translated_words_from_en_to_zh = ''
for translation in res.json()[0]:
    translated_words_from_en_to_zh += f'{translation[0]}'
print(print(translated_words_from_en_to_zh))
print()


"""
ORIGINAL SENTENCE:
欢乐斗地主是腾讯公司开始的一款实时对战棋牌手游，玩家可以使用手机在线斗地主，拥有多种斗地主游戏模式，您可以与百万游戏玩家一起畅玩游戏，还可以和好友拼倍数、拼财富！
PROCESSED USING GOOGLE TRANSLATE:
快乐房东是一款由腾讯开发的实时棋牌游戏。玩家可以使用手机在线与房东搏斗。它具有多种游戏模式。您可以与数百万玩家一起玩游戏，也可以与朋友打倍数。 ，争取财富！

ORIGINAL SENTENCE:
欢乐斗地主是腾讯公司开始的一款实时对战棋牌手游，玩家可以使用手机在线斗地主，拥有多种斗地主游戏模式，您可以与百万游戏玩家一起畅玩游戏，还可以和好友拼倍数、拼财富！
PROCESSED USING NLTK:
地主是腾讯发起的实时国际象棋和纸牌游戏。玩家可以使用自己的手机在线上与房东作战。它具有多种游戏模式。您可以与数百万玩家一起操纵游戏，并且可以与好友一起战斗。为财富而战！

快乐斗地主是腾讯启动的一款实时棋类游戏。玩家可以用手机在线斗地主，有多种斗地主游戏模式。可以和上百万的游戏玩家一起玩游戏，也可以和朋友一起争取多次和财富！
"""
