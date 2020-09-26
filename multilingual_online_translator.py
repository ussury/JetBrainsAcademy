import requests
from bs4 import BeautifulSoup


print("""Hello, you're welcome to the translator.
Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
""")

lang_dict = {
    '1': 'arabic',
    '2': 'german',
    '3': 'english',
    '4': 'spanish',
    '5': 'french',
    '6': 'hebrew',
    '7': 'japanese',
    '8': 'dutch',
    '9': 'polish',
    '10': 'portuguese',
    '11': 'romanian',
    '12': 'russian',
    '13': 'turkish'
}

your_lang = input('Type the number of your language: \n')
translate_lang = input('Type the number of language you want to translate to: \n')
word = input('Type the word you want to translate: \n')
_url = f'https://context.reverso.net/translation/{lang_dict[your_lang]}-{lang_dict[translate_lang]}/{word}'


headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(_url, headers=headers)
#print('200 OK') if r.status_code == 200 else print(f'status of the response: {r.status_code}')
soup = BeautifulSoup(r.content, 'html.parser')


def words_translation(_soup):
    words_trans = _soup.select('#translations-content .translation')
    words_trans_list = []
    for item in words_trans:
        words_trans_list.append(item.text.strip())

    for i in words_trans_list[:5]:
        print(i)


def examples_content(_soup):
    _examples_content = _soup.select('#examples-content .example')
    _examples_content_list = []
    for item in _examples_content:
        _examples_content_list.append(item.get_text(strip=True))

    for i in _examples_content_list[:5]:
        print(i + '\n')


def translation(_soup):
    print(f'\n{lang_dict[translate_lang]} Translations:')
    words_translation(_soup)
    print(f'\n{lang_dict[translate_lang]} Examples:')
    examples_content(_soup)


translation(soup)


