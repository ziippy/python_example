import requests
from bs4 import BeautifulSoup

import urllib.request
import os

def crawler(root_folder, url_base, url):
    #html = requests.get('http://cs231n.stanford.edu/slides/2015/caffe_tutorial.pdf')
    html = requests.head(url)
    # print(html.headers)
    cType = html.headers['Content-Type']
    if 'html' not in cType:
        # to file
        sub_url = url.replace(url_base, '')
        sub_url = root_folder + '/' + sub_url
        if len(sub_url) > 0:
            directory_path = os.path.dirname(sub_url)
            if os.path.isdir(directory_path) is False:
                os.makedirs(directory_path, exist_ok=True)
                print('directory created: ' + directory_path)

        urllib.request.urlretrieve(url, sub_url)
        print('file downloaded: ' + sub_url)
        return

    # to html
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    links = soup.body.find_all('a')
    # print(links)

    is_find_parent_directory = False
    for link in links:
        # print(link.text.strip(), link.get('href'))
        if link.text.strip() == 'Parent Directory':
            is_find_parent_directory = True
            continue

        if is_find_parent_directory is True:
            print('Go to link: ', url + link.get('href'))
            crawler(root_folder, url_base, url + link.get('href'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root_folder = 'cs231n.stanford.edu'
    crawler(root_folder, 'http://cs231n.stanford.edu/slides/', 'http://cs231n.stanford.edu/slides/')
    #crawler('http://cs231n.stanford.edu/slides/', 'http://cs231n.stanford.edu/slides/2015/caffe_tutorial.pdf')
