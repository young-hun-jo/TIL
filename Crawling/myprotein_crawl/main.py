import requests
from bs4 import BeautifulSoup
from save import save_to_file

url = requests.get(
    "https://www.myprotein.co.kr/nutrition/protein/whey-protein.list")
soup = BeautifulSoup(url.text, 'html.parser')
products = soup.find_all("div", {'class': 'productListProducts_product'})
lists = [] 
for product in products:
  results = product.find("div",{'class':'athenaProductBlock'})
  title = results.find('span')['data-product-title']
  price = results.find('span')['data-product-price']
  info = {'이름' : title, '가격' : price}
  product_info = info.values()
  lists.append(product_info)
content = lists
save_to_file(content)

  

