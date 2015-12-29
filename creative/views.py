from django.shortcuts import render, redirect
from creative.quote import quote_of_the_day, word_of_the_day
from creative.models import Repository, AdminUser
# Create your views here.


def admin_view(request):
    if request.session.get("admin_logged_in", False):
        return render(request, "admin.html")
    else:
        return render(request, "login.html")


def login(request):
    pwd = request.POST.get('pwd', '')
    auth = False
    if pwd != '':
        auth = AdminUser().verify_pwd(pwd)
    if auth:
        request.session["admin_logged_in"] = True
        return render(request, "admin.html")
    else:
        return redirect("/creative")


def logout(request):
    del request.session['admin_logged_in']
    return redirect("/creative")


def analyze(request):
    return render(request, "analyze.html")


def wish_list(request):
    return render(request, "list.html")


def home(request):
    quote = quote_of_the_day()
    word = word_of_the_day()
    repo = [{'type': 'Short Story',
            'content': Repository.objects.filter(tag='Short Story')},
            {'type': 'Poetry',
            'content': Repository.objects.filter(tag='Poetry')},
            {'type': 'Essay',
            'content': Repository.objects.filter(tag='Essay')},
            {'type': 'Start',
            'content': Repository.objects.filter(tag='Starts')}]
    return render(request, 'home.html', {'repo': repo, 'auth': False,
                                         'quote': quote, 'word': word})


def add(request):
    if not request.session.get("admin_logged_in", False):
        return redirect('/creative')
    name_ = request.POST.get('title', '')
    if name_ != '':
        tag_ = request.POST.get('type', '')
        status_ = request.POST.get('status', '')
        content_ = request.POST.get('text-content', '')
        Repository.objects.create(name=name_,
                                  tag=tag_,
                                  status=status_,
                                  content=content_)
        return redirect('/creative/admin')
    else:
        return render(request, "add.html")


def display(request, entry_id):
    entry = Repository.objects.filter(id=entry_id)[0]
    return render(request, "entry.html", {'entry': entry})
