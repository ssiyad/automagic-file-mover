#  MIT License
#
#  Copyright (c) 2020 Sabu Siyad
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

# Thank you https://fileinfo.com/

from contextlib import closing
from json import load, dump
from os import path
from re import match

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException:
        return None


def is_good_response(resp):
    content_type = resp.headers["Content-Type"].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find("html") > -1)


def get_category(url):
    file = path.join('moover', 'extensions.py')
    with open(file, 'r') as f:
        ext = load(f)

    raw_html = simple_get(url)
    page = BeautifulSoup(raw_html, 'html.parser')
    tables = page.find_all('table')
    for table in tables:
        rows = table.select('tr')
        for row in rows:
            if row.find_next('td'):
                x = row.find_next('td')
                y = x.find_next_sibling()
                ext_short = x.get_text()

                reg = r'^.(.+)$'
                reg_match = match(reg, ext_short)
                if reg_match:
                    ext_short = reg_match.group(1)

                if ext_short not in ext:
                    ext[ext_short] = y.get_text()

    with open(file, 'w') as f:
        dump(ext, f, sort_keys=True, indent=4)


def main():
    raw_html = simple_get('https://fileinfo.com/browse')
    cat_page = BeautifulSoup(raw_html, 'html.parser')
    cat_table = cat_page.find('div', {'class': 'category'})
    for elem in cat_table.select('a'):
        link = 'https://fileinfo.com' + elem['href']
        get_category(link)

    print('Successfully updated extensions')


if __name__ == '__main__':
    main()
