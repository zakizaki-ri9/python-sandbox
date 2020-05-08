from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question

# 関数ベースの書き方
def index(request):
    # 公開日時が最新である5件を取得
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # テンプレートに渡す辞書型を生成
    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)

    # 以下はショートカットrenderを使わないやり方
    # template = django.template.loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exits")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# クラスベースの書き方
# class QuestionView(View):
#     def index(request):
#         return HttpResponse("Hello, world. You're at the polls index.")
#     def detail(self, request, *args, **kwargs):
#         return HttpResponse(f"You're looking at question {question_id}.")
