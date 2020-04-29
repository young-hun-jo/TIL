import csv

def save_to_file(reviews):
  file = open("avengers_endgame_reviews.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "user", "content"])
  for review in reviews:
    writer.writerow(list(review.values()))

  return 