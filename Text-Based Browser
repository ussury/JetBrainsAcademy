import os
import requests
import sys
from pathlib import Path
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore

args = sys.argv

folder = Path(args[1])
tabs_list = deque()
invalid_url_message = 'Error: Invalid URL'

if not os.path.exists(folder):
    os.mkdir(folder)


def file_name(url):
    f_name = url.split('/')[-1]
    dot = f_name.rfind('.')

    return f_name[:dot]


def back_link():
    try:
        pop_link = tabs_list.pop()
        parent_dir = Path(folder)
        with open(os.path.join(parent_dir, pop_link)) as f:
            content = f.read()
        print(content)
    except IndexError:
        print('Не получилось открыть вкладку')


def open_tabs(_link):
    with open(os.path.join(folder, _link)) as f:
        content = f.read()
    print(content)


def save_web_files(url):
    if 'https://' not in url:
        url = 'https://' + url

    f_name = file_name(url)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tag_list = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'ol', 'ul', 'li']
    result_text = ''
    for tag in soup.find_all(tag_list):
        if tag.string is not None:
            result_text += tag.text + '\n'

    print(Fore.BLUE + result_text)
    parent_dir = Path(folder)
    with open(os.path.join(parent_dir, f_name), 'a') as f:
        f.write(result_text)

    return tabs_list.append(f_name)


while True:
    link = input()

    if link in tabs_list:
        open_tabs(link)
    elif link == 'exit':
        exit()
    elif '.' in link:
        save_web_files(link)
    elif link == 'back':
        back_link()
    else:
        print(invalid_url_message)
