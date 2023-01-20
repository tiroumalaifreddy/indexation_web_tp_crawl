import urllib.robotparser
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests
import validators


def authorized_fetch_whole_site(url_main : str):
    rp = urllib.robotparser.RobotFileParser()
    if url_main[-1] == "/":
        url_main = url_main[:-1]
    rp.set_url(url_main + '/robots.txt')
    rp.read()
    return rp.can_fetch("*", "url_main" + "/")

def authorized_fetch_pages(url_main, list_url_page : list):
    rp = urllib.robotparser.RobotFileParser()
    if url_main[-1] == "/":
        url_main = url_main[:-1]
    rp.set_url(url_main + '/robots.txt')
    rp.read()
    list_authorized_fetch_pages = []
    for url_page in list_url_page:
        if rp.can_fetch("*", url_page):
            list_authorized_fetch_pages.append(url_page)
    return list_authorized_fetch_pages

def get_sitemaps(url_main : str):
    rp = urllib.robotparser.RobotFileParser()
    if url_main[-1] == "/":
        url_main = url_main[:-1]
    rp.set_url(url_main + '/robots.txt')
    rp.read()
    return rp.site_maps()

def xml_type_sitemap(url_xml : str):
    response = urllib.request.urlopen(url_xml)
    xml = BeautifulSoup(response)
    sitemaps = xml.findAll('sitemap')
    if sitemaps:
        return True

def get_urls_from_sitemap(url_sitemap : str):
    list_urls_from_sitemap = []
    response = urllib.request.urlopen(url_sitemap)
    xml = BeautifulSoup(response)
    urls = xml.find_all('url')
    sitemaps = xml.findAll('sitemap')
    if sitemaps:
        for sitemap in sitemaps:
            sitemap_url = sitemap.find('loc').string
            list_urls_from_sitemap.append(get_urls_from_sitemap(sitemap_url))

    for url in urls:
        if xml.find("loc"):
            loc = url.findNext("loc").text
            list_urls_from_sitemap.append(loc)
    return list_urls_from_sitemap

def get_urls_from_webpage(url_page : str):
    response = requests.get(url_page)
    if response.status_code != 200:
        urls = []
    #response = urllib.request.urlopen(url_page)
    else:
        page = BeautifulSoup(response.text)
        urls = []
        for link in page.find_all('a'):
            new_link = link.get('href')
            base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(new_link))
            if validators.url(new_link):
                urls.append(new_link)
    return urls