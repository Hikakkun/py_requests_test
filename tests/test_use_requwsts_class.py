import pytest
from conftest import UseRequestsClass
import subprocess
import time
import socket
import urllib.parse
import os

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
HOST = '127.0.0.1'
PORT = 8000
CREATE_FILE_PATH_LIST = []
def get_request_base_url():
    """
    リクエストのベースURLを取得します。

    Returns:
        str: ベースURL
    """
    return f"http://{HOST}:{PORT}"

@pytest.fixture(scope="session")
def setup_server():
    """
    テスト用のHTTPサーバーをセットアップします。
    セッションスコープのフィクスチャとして使用されます。
    """
    #サーバを起動
    server_process = subprocess.Popen(['python', '-m', 'http.server', '--directory', SCRIPT_DIRECTORY,'--bind', HOST, str(PORT)])
    wait_for_server()
    yield
    #サーバを終了
    server_process.terminate() 
    server_process.wait()
    #テストで作成したファイルを削除
    for file_path in CREATE_FILE_PATH_LIST:
        os.remove(file_path)

def wait_for_server():
    """
        サーバが起動するまで待機する関数    
    """
    max_attempts = 30  # 最大で30回試行
    wait_time = 1  # 待機時間（秒）

    for _ in range(max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                break
            except (ConnectionRefusedError, OSError):
                time.sleep(wait_time)    

def create_file(file_name : str, file_content : str):
    """
    指定されたファイル名と内容でファイルを作成し、作成したファイルパスをリストに追加します。

    Args:
        file_name (str): 作成するファイルの名前
        file_content (str): ファイルに書き込む内容
    """
    create_file_path = os.path.join(SCRIPT_DIRECTORY, file_name)
    with open(create_file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)
        CREATE_FILE_PATH_LIST.append(create_file_path)

def test_html(setup_server):
    #正常なHTMLファイルに対して正しい結果が得られることを検証します。
    file_name = "title.html"
    file_content = r"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>テスト用のHTML</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML document for testing purposes.</p>
        </body>
        </html>    
    """
    create_file(file_name, file_content)
    request_url = urllib.parse.urljoin(get_request_base_url(), file_name)
    use_requests_class = UseRequestsClass(request_url)
    assert use_requests_class.execute("title") == "テスト用のHTML"
    assert use_requests_class.execute("body h1") == "Hello, World!"
    assert use_requests_class.execute("body p") == "This is a simple HTML document for testing purposes."

def test_request_exception(setup_server):
    #存在しないファイルへのリクエストに対してNoneが返ることを検証します。
    request_url = urllib.parse.urljoin(get_request_base_url(), "non_existent_file")
    use_requests_class = UseRequestsClass(request_url)
    assert use_requests_class.execute("title") == None