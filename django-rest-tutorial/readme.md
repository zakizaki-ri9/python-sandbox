# [django REST framework](https://www.django-rest-framework.org)の素振り

---

# コマンド

```bash
# 仮想環境に入る
poetry shell
```

## 仮想環境

```bash
# フォーマット
black .

# 起動
python manage.py runserver

# デバッグ
## snippets_list
http http://127.0.0.1:8000/snippets/
## snippets_detail
http http://127.0.0.1:8000/snippets/1/
```

# メモ

## [シリアライザ](https://www.django-rest-framework.org/api-guide/serializers/)

- Form / ModelForm的な動きをする
  - 例）JSONデータをモデルに変換する

### [フィールド指定](https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include)

`class Meta:`の`model`/`fields`を記述することで、  
シリアライズ/デシリアライズする際のモデル/フィールドが指定可能。

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        # fields = '__all__'
```

`fields = '__all__'`で、すべてのフィールドを指定可能。  
だが、**意図しないフィールドを公開して（レスポンスとして返して）しまう**  
**恐れがあるため、フィールドは明示的に指定したほうがよい。**

# 参考記事

