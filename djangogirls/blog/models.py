# djangoのライブラリを利用する
from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model = django.db.Model = Djangoのモデルとして認識させる
class Post(models.Model):
    # フィールド（カラム）の定義 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログ公開時に呼び出されるメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # toString()を自作したようなもの
    def __str__(self):
        return self.title
