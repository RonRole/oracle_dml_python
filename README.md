# Oracleのレコードをdmlに変換するツール
## 概要
- 開発などで、別環境のOracleに適用するdmlを作成するケースが多い
- 「一部のカラムは実行時引数で更新したい」「文字列型のデータを入れる場合、dmlではシングルクォートで囲まないといけない」など、要求や制約が多い
- 手作業でいちいち作成するのは面倒
- 自動で指定したテーブルのレコードをdmlに変換出来たら便利かもしれない

## 使い方
1. settings_default.jsonをコピーして、settings.jsonにリネーム
2. settings.jsonを編集
3. query_default.jsonをコピーして、query.jsonにリネーム
4. query.jsonを編集
5. 実行
    ~~~bash
    docker-compouse up -d
    docker-compose exec app bash
    # コンテナ内部で    
    python3 ora_dml.py
   ~~~ 

## メモ
- 元ネタがあるところからdmlを作るというツールなので、全く新しいデータのdmlは作れない
- 「商品データを、ユーザーIDだけ変えて追加したい」といったユースケースを想定
- 現状Oracle専用だけれど、他のデータベースでも使えるようにすると良いかもしれない