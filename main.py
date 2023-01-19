import functions
import click

list_url_found = []

@click.command()
@click.argument('url_main')
def run(url_main : str):
    if functions.authorized_fetch_whole_site(url_main = url_main) == False:
        print("Error : website does not allow crawling")
    else:
        sitemaps = functions.get_sitemaps(url_main)
        if sitemaps:
            for sitemap in sitemaps:
                list_url_found.append(functions.get_urls_from_sitemap(sitemap))
            list_url_found = sum(list_url_found, [])
            list_url_found = functions.authorized_fetch_pages(url_main, [*set(list_url_found)])
        
        