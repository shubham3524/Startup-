from news.models import Article,UserArticle
from news.forms import Userarticleform
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def userarticle_add(request):
    
    if request.method == "POST":
        form = Userarticleform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Article saved to database')
            return redirect('submityourideas')
        else:
            messages.error(request,'Article could not be saved')
    else:
        form = Userarticleform()
    ctx = {
        "form":form,
        "title":"Add new article"
    }
    return render(request,"submityourideas.html",ctx)
    
def article_view(request):
    articles = Article.objects.all()
    ctx = {
        'title':"all articles",
        'articles':articles,
    }
    return render(request,"news.html",ctx)
    
def User_view(request):
    article = UserArticle.objects.all()
    ctx = {
        'title':"Article",
        'article': article,
    }
    return render(request,"publicideas.html",ctx)

def article_detail_new(request,id):
    try:
        article = Article.objects.get(id=id)
        ctx ={
            'title':"article detail",
            'article':article,
        }
        return render(request,"newsdetail.html",ctx)
    except:
        return redirect("userideas")
    
def article_detail(request,id):
    try:
        article = UserArticle.objects.get(id=id)
        ctx ={
            'title':"article detail",
            'article':article,
        }
        return render(request,"newsdetail.html",ctx)
    except:
        return redirect("news")

def userarticle_detail(request,id):
    try:
        article = UserArticle.objects.get(id=id)
        ctx ={
            'title':"article detail",
            'article':article,
        }
        return render(request,"ideadetail.html",ctx)
    except:
        return redirect("#")