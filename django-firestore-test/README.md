# Django x FireStoreの素振り

---

# メモ

## FireStoreの設定

- [クイックスタート: サーバー クライアント ライブラリの使用](https://cloud.google.com/firestore/docs/quickstart-servers?hl=ja)

を元に進める。

### インストール

```bash
# FireStoreを扱うライブラリを追加
poetry add google-cloud-firestore
```

### 設定

`Cloud DataStore`の読み書き権限を付与したサービスアカウントを作成。  
キーをJSON形式で出力し、ローカルに配置したら、Django起動時に環境変数として登録するよう実装。

```python
# config/settings/local.py
from .base import *

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, ".tmp/serviceAccount.json")
```

上記は、ルート（`BASE_DIR`）配下に`.tmp/serviceAccount.json`として配置、  
それを環境変数として設定している。

### 動作確認

データ登録に成功すればOK。

```bash
poetry run python manage.py shell
```

```python
from google.cloud import firestore
# 初期化
db = firestore.Client()

# 登録
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
```
