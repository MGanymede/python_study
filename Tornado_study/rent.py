import requests
class RentFetcher:
    def get_rent_info(self):
        url = "https://www.shzfzl.gov.cn/Project/getProjectList"
        response = requests.get(url);
        html = response.content
        html_doc = str(html, 'utf-8')
        print(html_doc)

rent = RentFetcher()
rent.get_rent_info()