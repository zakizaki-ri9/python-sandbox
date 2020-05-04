# DjangoGirlsのチュートリアルを進める

---

# メモ

```bash
# ウェブサーバーを起動する
python manage.py runserver

# アプリケーション（モデル？）の作成
python manage.py startapp モデル名

# マイグレーションの作成
python manage.py makemigrations モデル名

# マイグレーションの実行
python manage.py migrate # 全部実行
python manage.py migrate モデル名

# スーパーユーザー（/admin/）の作成
python manage.py createsuperuser

# django shell
python manage.py shell
```
