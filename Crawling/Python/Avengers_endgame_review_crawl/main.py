from movie import extract_last_page, exract_reviews, req_last_page

from save import save_to_file

last_page = extract_last_page()
extract_review = req_last_page(last_page)

save_to_file(extract_review)











