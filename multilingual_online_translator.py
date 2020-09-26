import requests
from bs4 import BeautifulSoup


all_languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']

print('Hello, you\'re welcome to the translator. Translator supports:')
for position, val in enumerate(all_languages, 1):
    print(str(position) + '.', val.capitalize())

your_lang = int(input('Type the number of your language: \n'))
translate_lang = int(input('Type the number of a language you want to translate to or "0" to translate to all languages: \n'))
word = input('Type the word you want to translate: \n')
_url = f'https://context.reverso.net/translation/{all_languages[your_lang - 1]}-{all_languages[translate_lang - 1]}/{word}'

headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(_url, headers=headers)
#print('200 OK') if r.status_code == 200 else print(f'status of the response: {r.status_code}')
soup = BeautifulSoup(r.content, 'html.parser')


def words_translation(_soup):
    words_trans = _soup.select('#translations-content .translation')
    words_trans_list = [item.text.strip() for item in words_trans]

    for i in words_trans_list[:5]:
        print(i)


def examples_content(_soup):
    _examples_content = _soup.select('#examples-content .text')
    _examples_content_list = [item.text.strip('\n " " []') for item in _examples_content]

    print("\n\n".join(("\n".join(j for j in _examples_content_list[i:i+2]) for i in range(0,10,2))))


def translation(_soup):
    print(f'\n{all_languages[translate_lang - 1].capitalize()} Translations:')
    words_translation(_soup)
    print(f'\n{all_languages[translate_lang - 1].capitalize()} Examples:')
    examples_content(_soup)


translation(soup)

