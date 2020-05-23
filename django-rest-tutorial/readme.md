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

## [リクエストとレスポンス](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

### [`request.data`](https://www.django-rest-framework.org/api-guide/requests/#data)

- `request.data`でリクエストの内容が確認できる
- HTTPメソッドごとに応じたリクエストをフィルタリングできる
  - `request.POST`
  - `request.PUT`
  - etc...

### ビューの扱い

- 関数ベースのビューは`@api_view`
- クラスベースのビューは`APIView`クラス

### フォーマットの指定

[`format_suffix_patterns`の仕組み](https://www.django-rest-framework.org/api-guide/requests/#data)を使うことで、  
JSON等のフォーマットを指定できる。

```python
"""
urls.py
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
views.py
"""
# 関数ベース
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    # 処理

# クラスベース
class SnippetList(APIView):
    def get(self, request, format=None):
        # 処理

    def post(self, request, format=None):
        # 処理
```

# 参考記事

