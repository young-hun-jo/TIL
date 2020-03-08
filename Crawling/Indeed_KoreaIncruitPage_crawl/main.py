from indeed import extract_last_page, multi_req_page
from save import save_to_file
last_indeed_page = extract_last_page()
multi_req = multi_req_page(last_indeed_page)

save_to_file(multi_req)






