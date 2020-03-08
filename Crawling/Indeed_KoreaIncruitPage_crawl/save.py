import csv

def save_to_file(contents):
  file = open("indeed_data_marketing_incruit_info.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['title','company','location','info_link'])
  for content in contents:
    writer.writerow(list(content.values()))
    
  return 