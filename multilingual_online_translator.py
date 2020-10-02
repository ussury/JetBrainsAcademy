import sys
import requests
from bs4 import BeautifulSoup

args = sys.argv

all_languages = {'arabic': 'arabic', 'german': 'german', 'english': 'english', 'spanish': 'spanish', 'french': 'french',
                 'hebrew': 'hebrew', 'japanese': 'japanese', 'dutch': 'dutch', 'polish': 'polish',
                 'portuguese': 'portuguese', 'romanian': 'romanian', 'russian': 'russian', 'turkish': 'turkish'}

word = args[3]
to_lang = ''

try:
    your_lang = all_languages[args[1]]
except KeyError:
    print(f"Sorry, the program doesn't support {args[1]}")
    exit()

try:
    to_lang = all_languages[args[2]] if args[2] != 'all' else 'all'
except KeyError:
    print(f'Sorry, the program doesn\'t support {args[2]}')
    exit()


translation_file = f'{word}.txt'
url = 'https://context.reverso.net/translation/'


def get_soup(_url):
    try:
        r = requests.get(_url, headers={'user-agent': 'Mozilla/5.0'})
    except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
        exit()
    else:
        if r.status_code == 404:
            print(f"Sorry, unable to find {word}")
            exit()

    return BeautifulSoup(r.content, 'html.parser')


def translate():
    _url = f'{url}{your_lang}-{to_lang}/{word}'
    soup = get_soup(_url)
    words_translation = [i.text.strip() for i in soup.select('#translations-content .translation')]
    examples_content = [i.text.strip('\n " " []') for i in soup.select('#examples-content .text')]

    print(f'\n{to_lang.capitalize()} Translations:')
    for i in words_translation[:5]:
        print(i)

    print(f'\n{to_lang.capitalize()} Examples:')
    print("\n\n".join(("\n".join(j for j in examples_content[i:i + 2]) for i in range(0, 10, 2))))


def translate_all():
    with open(translation_file, 'w') as f:
        for i in all_languages:
            if i != your_lang:
                _url = f'{url}{your_lang}-{i}/{word}'
                soup = get_soup(_url)

                words_translation = [i.text.strip() for i in soup.select('#translations-content .translation')]
                examples_content = [i.text.strip('\n " " []') for i in soup.select('#examples-content .text')]

                print(f'\n{i.capitalize()} Translations:')
                print(words_translation[1])
                f.write(f'{i.capitalize()} Translations:' + '\n' + words_translation[1] + '\n')

                print(f'\n{i.capitalize()} Examples:')
                print('\n'.join(examples_content[:2]))
                print()
                f.write(f'\n{i.capitalize()} Examples:' + '\n' + examples_content[0] + '\n\n')
            else:
                continue


if to_lang == 'all':
    translate_all()
else:
    translate()

