# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
	context = {
		'posts': Post.objects.all(),
	}
	return render(request, 'notes/index.html', context)

def new_post(request):
	new_post = Post.objects.create(post=request.POST['post'])
	return redirect('/')
