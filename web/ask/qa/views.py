from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignUpForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })


def show_question(request, id_question):

    question = get_object_or_404(Question, id=id_question)
    if request.method == "POST":
        answer = Answer()
        answer.question = question
        answer.author = request.user
        answer.text = request.POST.get('text')
        answer.save()
        url = question.get_absolute_url()
        return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    answers_list = Answer.objects.filter(question=id_question)
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers_list,
        'form': form,
    })


def ask(request):

    if request.method == "POST":
        form = AskForm(request.POST)
        question = Question()
        question.title = request.POST.get('title')
        question.text = request.POST.get('text')
        question.author = request.user
        question.save()
        url = question.get_absolute_url()
        return HttpResponseRedirect(url)
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
