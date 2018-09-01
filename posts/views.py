# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
#from ipware import get_client_ip


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'posts/index.html', context)

def comment(request):
    if request.POST['comment']:
        p = Post(post_text = request.POST['comment'], pub_date=timezone.now(),
         client_ip = get_client_ip(request))
        p.save()

    latest_post_list = Post.objects.order_by('-pub_date')
    context = {'latest_post_list': latest_post_list}

    return render(request, 'posts/index.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip