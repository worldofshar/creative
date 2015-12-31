from django.shortcuts import render, redirect
from creative.quote import quote_of_the_day, word_of_the_day
from creative.models import Repository, AdminUser, Comment
# Create your views here.
from django.http import JsonResponse


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
    return render(request, 'home.html', {'quote': quote, 'word': word})


def get_entry(request):
    tag_type = request.GET.get('tag_type', '')
    entries_obj = Repository.objects.filter(tag=tag_type)
    entries = []
    for item in entries_obj:
        url = "/creative/display/" + str(item.id)
        entry = {"name": item.name, "url": url, "status": item.status}
        entries.append(entry)
    return JsonResponse({'entries': entries})


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


def add_comment(request):
    user = request.POST.get('username', '')
    if user != '':
        comment = request.POST.get('comment_text', '')
        rating_ = request.POST.get('rating', 0)
        entry_id = int(request.POST.get('entry', ''))
        entry = Repository.objects.filter(id=entry_id)[0]
        Comment.objects.create(username=user,
                               comment_text=comment,
                               rating=rating_,
                               entry_id=entry)
        return redirect("/creative/display/"+str(entry_id)+"/")


def display(request, entry_id):
    entry = Repository.objects.filter(id=entry_id)[0]
    comments = Comment.objects.filter(entry_id=entry_id)
    return render(request, "entry.html",
                  {'entry': entry, 'comments': comments})
