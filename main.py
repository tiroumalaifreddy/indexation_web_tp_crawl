import functions
import click
from urllib.parse import urlsplit
import itertools
import time
from urllib.parse import urlparse

list_url_found_internal = []
list_url_found_external = []
list_url_found_external_base = []
@click.command()
@click.option('--url_main') 
@click.option('--onlyexternal', is_flag=True)
def run(onlyexternal, url_main : str = 'https://www.scharles.net/'):
    global list_url_found_internal
    global list_url_found_external
    if functions.authorized_fetch_whole_site(url_main = url_main) == False:
        print("Error : website does not allow crawling")
    else:
        sitemaps = functions.get_sitemaps(url_main)
        if sitemaps:
            list_type = []
            for sitemap in sitemaps:
                list_type.append(functions.xml_type_sitemap(sitemap))
            if True in list_type:
                sitemaps = [sitemaps[list_type.index(True)]]
            for sitemap in sitemaps:
                list_url_found_internal.append(functions.get_urls_from_sitemap(sitemap))
            list_url_found_internal= list(itertools.chain(*list_url_found_internal))
            list_url_found_internal= list(itertools.chain(*list_url_found_internal))
            list_url_found_internal = functions.authorized_fetch_pages(url_main, list_url_found_internal)
            list_url_found_internal = [*set(list_url_found_internal)]
        if len(list_url_found_internal) == 0:
            list_url_found_internal.append(url_main)
        i = 0
        if onlyexternal:
            while len(list_url_found_external) < 50 and i != len(list_url_found_internal):
                url_page = list_url_found_internal[i]
                list_new_pages = functions.get_urls_from_webpage(url_page = url_page)
                for new_link in list_new_pages:
                    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(new_link))
                    domain = urlparse(base_url).netloc
                    domain_main = urlparse(url_main).netloc
                    if new_link not in list_url_found_external and new_link not in list_url_found_internal and domain != domain_main:
                            list_url_found_external.append(new_link)
                    if base_url not in list_url_found_external_base and base_url != url_main:
                            list_url_found_external_base.append(base_url)
                i += 1
                time.sleep(5)
            j = 0
            length_list = len(list_url_found_external)
            while len(list_url_found_external) < 50 and j < length_list:
                url_page = list_url_found_external[j]
                list_new_pages = functions.get_urls_from_webpage(url_page = url_page)
                for new_link in list_new_pages:
                    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(new_link))
                    domain = urlparse(base_url).netloc
                    domain_main = urlparse(url_main).netloc
                    if new_link not in list_url_found_external and new_link not in list_url_found_internal and domain != domain_main:
                            list_url_found_external.append(new_link)
                    if base_url not in list_url_found_external_base and base_url != url_main:
                            list_url_found_external_base.append(base_url)
                j += 1
                length_list = len(list_url_found_external)
                time.sleep(5)

        if onlyexternal == False:
            while len(list_url_found_external) < 50 and i != len(list_url_found_internal):
                url_page = list_url_found_internal[i]
                list_new_pages = functions.get_urls_from_webpage(url_page = url_page)
                for new_link in list_new_pages:
                    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(new_link))
                    if new_link not in list_url_found_external and new_link not in list_url_found_internal:
                            list_url_found_external.append(new_link)
                    if base_url not in list_url_found_external_base and base_url != url_main:
                            list_url_found_external_base.append(base_url)
                i += 1
                time.sleep(5)
            j = 0
            length_list = len(list_url_found_external)
            while len(list_url_found_external) < 50 and j < length_list:
                url_page = list_url_found_external[j]
                list_new_pages = functions.get_urls_from_webpage(url_page = url_page)
                for new_link in list_new_pages:
                    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(new_link))
                    domain = urlparse(base_url).netloc
                    domain_main = urlparse(url_main).netloc
                    if new_link not in list_url_found_external and new_link not in list_url_found_internal:
                            list_url_found_external.append(new_link)
                    if base_url not in list_url_found_external_base and base_url != url_main:
                            list_url_found_external_base.append(base_url)
                j += 1
                length_list = len(list_url_found_external)
                time.sleep(5)
        list_url_found_external = list_url_found_external[:50]
        file_internal = 'exports/list_internal-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
        file_external = 'exports/list_external-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
        with open(file_internal, 'w') as fp:
            for item in list_url_found_internal:
                fp.write("%s\n" % item)
        with open(file_external, 'w') as fp:
            for item in list_url_found_external:
                fp.write("%s\n" % item)


if __name__ == '__main__':
    run()