import requests
from bs4 import BeautifulSoup

all_languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
                 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']

print('Hello, you\'re welcome to the translator. Translator supports:')
for position, val in enumerate(all_languages, 1):
    print(str(position) + '.', val.capitalize())

your_lang = int(input('Type the number of your language: \n'))
to_lang = int(input('Type the number of a language you want to translate to or "0" to translate to all languages: \n'))
word = input('Type the word you want to translate: \n')
translation_file = f'{word}.txt'
url = 'https://context.reverso.net/translation/'


def get_soup(_url):
    r = requests.get(_url, headers={'user-agent': 'Mozilla/5.0'})
    return BeautifulSoup(r.content, 'html.parser')


def one_translate():
    _url = f'{url}{all_languages[your_lang - 1]}-{all_languages[to_lang - 1]}/{word}'
    soup = get_soup(_url)

    text_words_translation = f'\n{all_languages[to_lang - 1].capitalize()} Translations: \n'
    words_translation = [i.text.strip() for i in soup.select('#translations-content .translation')]
    for i in words_translation[:1]:
        text_words_translation += i + '\n'
    print(text_words_translation)

    text_examples_content = f'{all_languages[to_lang - 1].capitalize()} Examples: \n'
    examples_content = [i.text.strip('\n " " []') for i in soup.select('#examples-content .text')]
    text_examples_content += '\n'.join(examples_content[:2])
    print(text_examples_content)


def translate_all():
    with open(translation_file, 'w') as f:
        for i in all_languages:
            if i != all_languages[your_lang - 1]:
                _url = f'{url}{all_languages[your_lang - 1]}-{i}/{word}'
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


if to_lang > 0:
    one_translate()
else:
    translate_all()
