import functions
import click
from urllib.parse import urlsplit

list_url_found_internal = []
list_url_found_external = []

@click.command()
@click.argument('url_main')
def run(url_main : str):
    if functions.authorized_fetch_whole_site(url_main = url_main) == False:
        print("Error : website does not allow crawling")
    else:
        sitemaps = functions.get_sitemaps(url_main)
        if sitemaps:
            for sitemap in sitemaps:
                list_url_found_internal.append(functions.get_urls_from_sitemap(sitemap))
            list_url_found_internal= sum(list_url_found_internal, [])
            list_url_found_internal = functions.authorized_fetch_pages(url_main, [*set(list_url_found_internal)])
        
        