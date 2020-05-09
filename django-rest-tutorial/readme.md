# [django REST framework](https://www.django-rest-framework.org)の素振り

---

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

