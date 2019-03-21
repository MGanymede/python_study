from selenium import webdriver
import time


def __get_current_month():
    return time.strftime("%Y-%m", time.localtime())


class Rent:
    def __init__(self):
        self.data = []
        self.fetchDate = ""

    def get_rent_data(self):
        current_month = self.__get_current_month()
        if len(self.data) == 0 or current_month != self.fetchDate:
            browser = webdriver.Chrome()
            browser.get("https://www.shzfzl.gov.cn/gg_house/zl_house.html")
            elements = browser.find_elements_by_css_selector(".zlHouse-body-text-same")
            data = []
            for element in elements:
                contents = element.find_elements_by_tag_name("span")
                row = []
                for index, content in enumerate(contents):
                    row.append(content.text)
                data.append(row)
            self.data = data
            self.fetchDate = self.__get_current_month()
            browser.quit()
            return data
        else:
            return self.data



    @staticmethod
    def __get_current_month():
        return time.strftime("%Y-%m", time.localtime())

