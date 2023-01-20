
# TP Crawl ENSAI - Indexation Web

Ce mini-projet implémente un crawler singlethread. Le crawler analyse d'abord les sitemaps
si ces derniers sont référencés dans le fichier robots.txt du site. Une fois que les URLs sont extraites
à partir des sitemaps, le crawler cherche jusqu'à 50 pages non référencées dans les sitemaps.
Une option est disponible pour n'extraire que les pages externes au site.

A partir d'une URL d'entrée unique (exemple: https://ensai.fr/), le crawler écrit dans deux fichiers
.txt les URLs des pages trouvées. La liste "interne" comprend les pages trouvées dans les sitemaps
tandis que la liste "externe" comprend les pages trouvées en scrapant le site.




## Authors

- [@tiroumalaifreddy](https://www.github.com/tiroumalaifreddy)


## Usage/Examples

Le crawler prend en entrée:
- ```--url_main {url : str}````: permet d'indiquer le site sur lequel le crawler doit se placer
- en option ```--onlyexternal```: permet d'indiquer au crawler de n'extraire que les pages externes au site fournis en entrée. La liste "externe" ne comprendra alors que les pages vraiment externes.

```python
import Component from 'my-project'

function App() {
  return <Component />
}
```

