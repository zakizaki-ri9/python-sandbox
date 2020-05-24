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

## クラスベースAPIViewにおけるmixinsとGenerics

- [Class-based Views](https://www.django-rest-framework.org/tutorial/3-class-based-views/)

`rest_framework.mixins`を継承したAPIViewは、  
RESTfulAPIの振る舞いをするメソッドを提供してくれる。

```python
# example
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

`rest_framework.generics`は`mixins`をさらにラッパーしたViewを提供している。  
特別な振る舞いをしないのであれば、以下で事が済む。

```python
# example
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

### GenericsAPIViewのフック

`perfume_create`/`perfume_update`/`perfume_delete`を定義することで、  
GenericsAPIView側でSelialiers経由の更新操作をフックできる。

- [perfume_createの場合](https://github.com/encode/django-rest-framework/blob/acbd9d8222e763c7f9c7dc2de23c430c702e06d4/rest_framework/mixins.py#L23-L24)
- [フックの仕組み](https://www.django-rest-framework.org/api-guide/generic-views/)
  - `generics.〜APIView`は、`mixins.〜ModelMixin`を継承している
  - `get`/`post`などのHTTPメソッドに応じた処理を実施している
    - https://github.com/encode/django-rest-framework/blob/acbd9d8222e763c7f9c7dc2de23c430c702e06d4/rest_framework/generics.py#L184-L291

## [Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

レコードの読み書き権限の仕組みが提供されている。  
以下で素振りすることが可能。

- [Authentication & Permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)

自分で制約を追加したい場合は、[Custom permissions](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions)の仕組みを使う。  
以下実装例。

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```

## マイグレーション

### Null許容の外部キーを作成するパターン

外部キーで紐づくレコードも合わせて削除したい。  
が、Nullも許容したい（後から外部キーを追加する場合のイメージ）は、  
`on_delete=models.CASCADE,null=True`を設定する。

```python
owner = models.ForeignKey(
    "auth.User",
    related_name="snippets",
    on_delete=models.CASCADE,
    null=True
)
```

# 参考記事

