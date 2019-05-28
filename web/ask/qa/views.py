from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.


def login(request):

    return HttpResponse('login')


def signup(request):

    return HttpResponse('signup')


def logout(request):

    return HttpResponse('logout')


def show_question(request, id_question):

    question = get_object_or_404(Question, id=id_question)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():

            form.question = id_question
            form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
        else:
            HttpResponse('fuckup')
    else:
        form = AnswerForm(initial={'question': id_question})
    answers_list = Answer.objects.filter(question=id_question)
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers_list,
        'form': form,
    })


def ask(request):

    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
        else:
            HttpResponse('fuckup')
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })


def popular(request):

    questions = Question.objects.popular()
    get_page = request.GET.get('page', 1)
    paginator = Paginator(questions, 3)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(get_page)
    return render(request, 'home.html', {
        'h1_title': "Popular Question",
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def home(request):

    questions = Question.objects.new()
    get_page = request.GET.get('page', 1)
    paginator = Paginator(questions, 3)
    paginator.baseurl = '/?page='
    page = paginator.page(get_page)
    return render(request, 'home.html', {
        'h1_title': "Last Question",
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })
