from django.http import HttpResponse


# 関数ベースの書き方
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    return HttpResponse(f"You're looking at question {question_id}.")


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
