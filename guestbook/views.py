from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .models import Post
from .models import Category

def list_posts(request):
	try:
		page = int(request.GET['page'])
		if page < 1:
			page = 1
	except Exception:
		page = 1
	per_page = 5

	posts = Post.objects.order_by('-created_at')[page-1:page*per_page]

	return render(request, 'list.html',{
		'posts':posts,
	})

def view_post(request,pk):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'view.html', {
		'post':post,
	})

def create_post(request):
	#글쓰기 생성화면에 필요한 카테고리 data전달
	if request.method == 'GET':
		categories = Category.objects.all()
		ctx = {
			'categories' : categories,
		}
	#입력값 저장처리
	else:
		form = request.POST
		#category에 입력받은 카테고리 값을 넣어줌
		category = get_object_or_404(Category, pk=form['category'])
		#post에 form에서 입력받은 값들을 넣어줌
		post = Post(
			title=form['title'],
			content=form['content'],
			category=category,
		)
		post.full_clean()
		post.save()
		#data 생성하고 저장 후 생성된 글로 redirect시켜주기 위해 url생성
		url = reverse('gbs:view_post', kwargs={'pk' : post.pk})
		return redirect(url)
	return render(request, 'edit.html', ctx)
'''
#render 예제
def hello(request):
	posts = Post.objects.order_by('-created_at')

	return render(request, 'hello.html', {
		'title': 'hello world',
		'posts': posts,
		}
	)


def hello(request):
	return redirect('/guestbook/list')
'''