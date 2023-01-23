
# TP Crawl ENSAI - Indexation Web

Ce mini-projet implémente un crawler singlethread. Le crawler analyse d'abord les sitemaps
si ces derniers sont référencés dans le fichier robots.txt du site. Une fois que les URLs sont extraites
à partir des sitemaps, le crawler cherche jusqu'à 50 pages non référencées dans les sitemaps.
Une option est disponible pour n'extraire que les pages externes au site.

A partir d'une URL d'entrée unique (exemple: https://ensai.fr/), le crawler écrit dans deux fichiers
.txt les URLs des pages trouvées. La liste "interne" comprend les pages trouvées dans les sitemaps
tandis que la liste "externe" comprend les pages trouvées en scrapant le site. Le crawler respecte les règles de politesse indiquées dans le fichier robots.txt : les pages interdites par le site ne sont pas ajoutées dans les listes.




## Authors

- [@tiroumalaifreddy](https://www.github.com/tiroumalaifreddy)


## Installation

Dans l'idéal, lancer un environnement virtuel (voir https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html).

Pour installer les packages requis:
```bash
pip install -r requirements.txt
```
    
## Usage/Examples

Le crawler prend en entrée:
- ```--url_main {url : str}````: permet d'indiquer le site sur lequel le crawler doit se placer
- en option ```--onlyexternal```: permet d'indiquer au crawler de n'extraire que les pages externes au site fournis en entrée. La liste "externe" ne comprendra alors que les pages vraiment externes.

En se plaçant à la racine du projet:

```python
python3.8 main.py --onlyexternal --url_main https://www.ensai.fr
```

OU

```python
python3.8 main.py --url_main https://www.ensai.fr
```

Deux fichiers .txt seront alors crées dans le dossier exports:
-list_internal-(...) : liste des sites trouvées dans les sitemaps
-list_external-(...) : liste des sites en analysant les pages du site

## Limites

Dans le cas où le fichier ```robots.txt``` du site donné en entrée n'indique aucun sitemaps, la liste "interne" ne comportera que l'URL donnée en entrée. En revanche, si l'option ```onlyexternal``` n'est pas donnée (ie égal à ```False```), la liste externe devrait comprendre un grand nombre de pages "internes" au site.