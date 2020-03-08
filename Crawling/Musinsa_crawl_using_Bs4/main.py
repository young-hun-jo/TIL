import requests
from bs4 import BeautifulSoup
from save import save_to_file

URL = requests.get("https://store.musinsa.com/app/contents/bestranking")
musinsa = BeautifulSoup(URL.text, 'html.parser')

lists = []
product_sec = musinsa.find("div", {'class': 'list-box'})
products = product_sec.find_all("li", {'class': 'li_box'})
for product in products:
    rankings = product.find("p", {'class': 'n-label'})
    ranking = rankings.find("span")
    if ranking:
        _ = ranking.extract()
        ranks = rankings.text.strip()
    else:
        ranks = rankings.text.strip()
    brand = product.find("div", {'class': 'article_info'})
    results = brand.select('p.item_title:nth-of-type(1)')
    for result in results:
        if result.text == '[신학기]':
            brand_name = brand.select_one('p:nth-of-type(2)').get_text()
        else:
            brand_name = result.select_one('a').get_text()
    pro_names = brand.find("p", {'class': 'list_info'}).find('a')['title']
    prices = brand.find("p", {'class': 'price'})
    origin = prices.find('del')
    if origin:
        _ = origin.extract()
        price = prices.text.strip()
    else:
        price = prices.text.strip()

    info = {
        'ranks': ranks,
        'brand': brand_name,
        'product': pro_names,
        'price': price
    }
    product_info = info.values()
    lists.append(product_info)
contents = lists
save_to_file(contents)



