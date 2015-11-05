# coding=UTF-8

import os
import requests
from bs4 import BeautifulSoup

dir_url_template = "http://conferences.sigcomm.org/imc/{year}/papers/"


def make_dirs(d):
    try:
        os.makedirs(d)
    except OSError:
        pass


def fetch(year, local_dir):
    make_dirs(local_dir)
    url = dir_url_template.format(year=year)
    soup = BeautifulSoup(requests.get(url).text)
    soup.find_all('a')


if __name__ == '__main__':
    fetch(2014, "papers/sigcomm/2014")

