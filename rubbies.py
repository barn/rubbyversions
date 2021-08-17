#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from bs4 import BeautifulSoup
import requests
import re
# from amazing_printer import ap
# import ipdb
# import requests

# requests code goes here to download https://www.ruby-lang.org/en/downloads/

fp = ''

if True:
    r = requests.get('https://www.ruby-lang.org/en/downloads/')
    if r.status_code != requests.codes.ok:
        print("requests failed")
        exit()
    fp = r.text
else:
    f = open("rubby_downloads.html", "r")
    fp = f.read()


soup = BeautifulSoup(fp, 'html.parser')

parts_to_find = {'stable': 'Stable releases:',
                 'maint': re.compile('''^In security maintenance phase.*:''')}

for nom, findme in parts_to_find.items():

    stables = soup.find(text=findme).parent.parent.ul.find_all('li')

    for link in list(stables):
        s = str(link).replace("\n", '')

        souper = BeautifulSoup(s, 'html.parser')

        ruby_ver, ruby_link, ruby_sha = [souper.a.text, souper.a['href'],
                                         souper.br.next_sibling]
        ruby_ver = ruby_ver.split(' ')[1]
        ruby_sha = ruby_sha.split(' ')[1]

        print(f"For {nom}, Ruby version: {ruby_ver}, link: {ruby_link},"
              f" sha256: {ruby_sha}")
