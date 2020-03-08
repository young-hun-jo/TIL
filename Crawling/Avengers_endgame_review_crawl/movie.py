import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com/movie/bi/mi/review.nhn?code=136900"

def extract_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div',{'class':'paging'})
    pages = pagination.find_all('span')

    page_num = []
    for page in pages:
        page_num.append(int(page.string))
        max_page = page_num[-1]
    
    return max_page

def exract_reviews(html):
  title = html.find('a').strong
  user = html.find('span',{'class':'user'}).find('a')
  content = html.find('p').find('a')
  
  return {'title':title.string,'user':user.string,'content':content.string}
   
    
def req_last_page(last_page):
  reviews = []
  for page in range(last_page):
    print(f"Scrapping Page : {page}")    
    result = requests.get(f"{URL}&page={page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find("ul",{'class':'rvw_list_area'})
    results = results.find_all('li')
    for result in results:
      review = exract_reviews(result)
      reviews.append(review)

  return reviews


