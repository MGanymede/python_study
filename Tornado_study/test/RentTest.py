import  unittest
from mock import patch

from  Tornado_study.fetcher.Rent import Rent

class RentTest(unittest.TestCase):

    @patch('selenium.webdriver.Chrome')
    def test_mock(self,  Chrome_mock):
        class mock_webdriver:
            def get(self, url):
                return mock_webdriver()
            def find_elements_by_css_selector(self, name):
                return [mock_webdriver()]
            def find_elements_by_tag_name(self, name):
                return [mock_webdriver()]
            def __init__(self):
                self.text = "hello world"
            def quit(self):
                return True
        Chrome_mock.return_value = mock_webdriver()
        rent = Rent()
        data = rent.get_rent_data()
        assert len(data)==1
        assert data[0][0] == "hello world"


