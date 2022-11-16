from django.shortcuts import render
from django.core.paginator import Paginator


def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)


def index(request):
    questions = []

    for i in range(1, 30):
        questions.append({
            'id': i,
            'title': 'Title ' + str(i),
            'text': 'Text is ' + str(i),
            'tags': ['test'],
            'answers': 5 + i,
            'likes': 10 + i
        })

    return render(request, 'index.html', {'page_obj': paginate(questions, request)})


def hot_handler(request):
    questions = []

    for i in range(1, 20):
        questions.append({
            'id': i,
            'title': 'Title ' + str(i),
            'text': 'Text is ' + str(i),
            'tags': ['test'],
            'answers': 5 + i,
            'likes': 10 + i
        })

    return render(request, 'index.html', {'page_obj': paginate(questions, request)})


def tag_handler(request, **kwargs):
    tag = kwargs['tag_name']

    questions = []

    for i in range(1, 20):
        questions.append({
            'id': i,
            'title': 'Title ' + str(i),
            'text': 'Text is ' + str(i),
            'tags': ['test', tag],
            'answers': 5 + i,
            'likes': 10 + i
        })

    return render(request, 'index.html', {'page_obj': paginate(questions, request)})


def question_handler(request, **kwargs):
    q_id = kwargs['question_id']

    answers = []

    for i in range(1, 10):
        answers.append({
            'name': 'User ' + str(i),
            'text': 'Bla-bla-bla',
            'likes': i,
            'isCorrect': i == 1
        })

    question = {
        'id': q_id,
        'title': 'Title ' + str(q_id),
        'text': 'Text is ' + str(q_id),
        'tags': ['test'],
        'likes': 10 + q_id,

    }

    return render(request, 'question.html', {'question': question, 'page_obj': paginate(answers, request, 5)})


def login_handler(request):
    return render(request, 'login.html')


def signup_handler(request):
    return render(request, 'signup.html')


def ask_handler(request):
    return render(request, 'ask.html')
