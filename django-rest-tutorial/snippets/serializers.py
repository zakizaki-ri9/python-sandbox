from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]


# シリアライザで Form / ModelForm に似た働き（JSON等のデータをインスタンス変換）する
class SnippetSerializer(serializers.ModelSerializer):

    # ReadOnlyFieldで、更新フィールドとして扱わないようにする
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet

        # 項目変更した際に、意図しないフィールド公開を防ぐため、公開するフィールドを明示的にした方がよい
        fields = ["id", "title", "code", "linenos", "language", "style", "owner"]
        # fields = '__all__' で全てのフィールドを指定する
