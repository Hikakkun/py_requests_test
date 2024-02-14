# py_requests_test
* pythonのrequestsライブラリを使ったコードのテスト
## 使用ライブラリ
* python 3.12.0
* pip 23.2.1
```text:requirements.txt
requests==2.31.0
beautifulsoup4==4.12.2
pytest==8.0.0
```
## UseRequestsClass(テスト対象のクラス)
* HTTPリクエストを行い、指定されたCSSセレクタに基づいてHTML要素を取得するクラス

## テストの流れ
* テストの前にPython の http.serverを用いてローカルサーバを立てる
* 各テストの前にテスト用ファイルを作成
* 作成したファイルにhttpアクセスしてUseRequestsClassのメソッドを実行