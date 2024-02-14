# py_requests_test
* pythonのrequestsライブラリを使ったコードのテスト

## UseRequestsClass(テスト対象のクラス)
* HTTPリクエストを行い、指定されたCSSセレクタに基づいてHTML要素を取得するクラス

## テストコード
### テストの流れ
* テストの前にPython の http.serverを用いてローカルサーバを立てる
* 各テストの前にテスト用ファイルを作成
* 作成したファイルにhttpアクセスしてUseRequestsClassのメソッドを実行