import csv

def save_to_file(contents):
  file = open("myprotein.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(['제품이름','제품가격'])
  for content in contents:
    writer.writerow(list(content))

  return


