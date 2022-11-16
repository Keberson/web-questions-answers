from django.shortcuts import render
from django.core.paginator import Paginator

from app.models import Question, Answer


def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)


def index(request):
    return render(request, 'index.html', {'page_obj': paginate(Question.objects.last_questions(), request)})


def hot_handler(request):
    return render(request, 'index.html', {'page_obj': paginate(Question.objects.hot_questions(), request)})


def tag_handler(request, **kwargs):
    tag = kwargs['tag_name']

    return render(request, 'index.html', {'page_obj': paginate(Question.objects.tag_questions(tag), request)})


def question_handler(request, **kwargs):
    q_id = kwargs['question_id']

    return render(request, 'question.html',
                  {'question': Question.objects.get(id=q_id),
                   'page_obj': paginate(Answer.objects.get_by_id(q_id), request, 30)})


def login_handler(request):
    return render(request, 'login.html')


def signup_handler(request):
    return render(request, 'signup.html')


def ask_handler(request):
    return render(request, 'ask.html')
