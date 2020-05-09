from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# リスト内包表記でitem[1]がnullでないもののみを抽出している
LEXERS = [item for item in get_all_lexers() if item[1]]
# LEXERSから言語の大小文字を抽出し、昇順ソート
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# エディタ系を抽出し、昇順ソート
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    class Meta:
        ordering = ["created"]
