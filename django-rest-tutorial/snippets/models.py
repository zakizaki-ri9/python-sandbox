from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE, null=True
    )
    highlighted = models.TextField(default="")

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ["created"]
