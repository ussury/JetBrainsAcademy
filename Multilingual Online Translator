import requests
from bs4 import BeautifulSoup

lang = input('''Type "en" if you want to translate from French into English, 
or "fr" if you want to translate from English into French: \n''')
word = input('Type the word you want to translate: \n')
print(f'You chose "{lang}" as the language to translate "{word}".')


def get_url(_lang):
    _url = ''
    if lang == 'en':
        _url = 'https://context.reverso.net/translation/french-english/'
    if lang == 'fr':
        _url = 'https://context.reverso.net/translation/english-french/'

    return _url


headers = {'user-agent': 'Mozilla/5.0'}

r = requests.get(get_url(lang) + word, headers=headers)

print('200 OK') if r.status_code == 200 else print(f'status of the response: {r.status_code}')

soup = BeautifulSoup(r.content, 'html.parser')


def words_translation(_soup):
    words_trans = _soup.select('#translations-content .translation')
    words_trans_list = []
    for item in words_trans:
        words_trans_list.append(item.text.strip())

    print('Translation ' + ', '.join(words_trans_list))


def examples_content(_soup):
    examp_content = soup.select('#examples-content .example .text')
    examp_content_list = []
    for item in examp_content:
        examp_content_list.append(item.text.strip('\n " "'))

    print('Translation ' + ', '.join(examp_content_list))


words_translation(soup)
examples_content(soup)
