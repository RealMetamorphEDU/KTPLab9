# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }

            art = None
            try:
                art = Article.objects.get(title=form["title"])
            except Article.DoesNotExist:
                pass
            if form["text"] and form["title"] and art is None:
                art = Article.objects.create(text=form["text"],
                                             title=form["title"],
                                             author=request.user)
                return redirect('get_article', article_id=art.id)
            else:
                if art is not None:
                    form['errors'] = u"Название статьи не уникально!"
                else:
                    form['errors'] = u"Не все поля заполнены!"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        usr = None
        try:
            usr = User.objects.get(username=form["username"])
            usr = User.objects.get(email=form["mail"])
            # если юзер существует, то ошибки не произойдет и
            # программа удачно доберется до следующей строчки
            print (u"Такой юзер уже есть")
        except User.DoesNotExist:
            print (u"Такого юзера ещё нет")
        if form["username"] and form["mail"] and form["password"] and usr is None:
            usr = User.objects.create(username=form["username"],
                                      email=form["mail"],
                                      password=make_password(form["password"]))
            return redirect('archive')
        else:
            if usr is not None:
                form['errors'] = u"Логин или почта уже заняты"
            else:
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})


def input_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is None:
                form['errors'] = u"Такой пользователь не зарегестрирован!"
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html', {})
