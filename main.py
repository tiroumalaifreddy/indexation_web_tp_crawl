import functions
import click
from urllib.parse import urlsplit
import itertools

list_url_found_internal = []
list_url_found_external = []

# @click.command()
# @click.option('--url_main')
def run(url_main : str = 'https://www.ensai.fr'):
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
        while len(list_url_found_internal) < 50:
            for url_page in list_url_found_internal:
                list_new_pages = functions.get_urls_from_webpage(url_page = url_page)
                for new_link in list_new_pages:
                    if new_link not in list_url_found_external:
                        list_url_found_external.append(new_link)
            for url_page in list_url_found_external:
                run(url_page)
        with open(r'list_internal.txt', 'w') as fp:
            for item in list_url_found_internal:
                fp.write("%s\n" % item)


if __name__ == '__main__':
    run()