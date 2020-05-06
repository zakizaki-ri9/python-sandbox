# [現場で使えるDjangoの教科書 基礎編](https://www.amazon.co.jp/現場で使える-Django-の教科書《基礎編》-横瀬-明仁/dp/4802094744)を元に素振り

---

# 概要

## pipenv系

```bash
# 初期化
pipenv --three

# パッケージインストール
pipenv install パッケージ名
pipenv install パッケージ名==バージョン

# 開発環境のみの場合は以下
pipenv install --dev パッケージ名

# 脆弱性チェック
pipenv check

# 仮想環境に入る
pipenv shell
```

## Django系

### プロジェクト作成

```bash
django-admin startproject プロジェクト名 ディレクトリ
# django-admin startproject app .
```

以下、公式に記載されている注意点。

> 組み込みの Python モジュールや Django のコンポーネントの名前を使わないようにしてください。とりわけ、 django (Django 自体と名前が衝突します) や test (組み込みの Python パッケージ名と名前が衝突します) を使わないようにしましょう。

### 起動

```bash
python manage.py runserver
```

# 参考資料

- [Django ドキュメント / 2.2](https://docs.djangoproject.com/ja/2.2/)
  - [チュートリアル](https://docs.djangoproject.com/ja/2.2/intro/tutorial01/)
- [Qiita - PipenvでDjango開発環境をつくる](https://qiita.com/nochifuchi/items/4fe0164f0d8949cf11b7)
