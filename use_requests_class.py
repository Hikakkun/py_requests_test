from dataclasses import dataclass
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from bs4 import BeautifulSoup

@dataclass
class UseRequestsClass:
    """
    HTTPリクエストを行い、指定されたCSSセレクタに基づいてHTML要素を取得するクラス。

    Attributes:
        url (str): リクエストを行う対象のURL
    """
    url : str 
    
    def execute(self, css_selector : str) -> str | None:
        """
        指定されたCSSセレクタに基づいてHTML要素を取得します。

        Args:
            css_selector (str): 取得するHTML要素を指定するCSSセレクタ

        Returns:
            str | None: 取得したHTML要素のテキスト。エラーが発生した場合はNone。
        """
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
        