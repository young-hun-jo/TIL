import csv

def save_to_file(contents):
  file = open("bestseller.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(['순위','브랜드','제품명','가격'])
  for content in contents:
    writer.writerow(list(content))
  return