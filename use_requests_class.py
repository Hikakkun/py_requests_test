from dataclasses import dataclass
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from bs4 import BeautifulSoup

@dataclass
class UseRequestsClass:
    url : str 
    
    def execute(self, css_selector : str) -> str | None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTPエラーが発生しました: {http_err}')

        except Timeout as timeout_err:
            print(f'タイムアウトエラーが発生しました: {timeout_err}')

        except RequestException as req_err:
            print(f'リクエストエラーが発生しました: {req_err}')

        except Exception as err:
            print(f'予期せぬエラーが発生しました: {err}')

        else:
            # エラーが発生しなかった場合の処理
            soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
            search_element_soup = soup.select_one(css_selector)
            return search_element_soup.get_text("")
        
        return None
        