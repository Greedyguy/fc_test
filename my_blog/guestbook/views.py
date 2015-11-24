from django.shortcuts import HttpResponse

from .models import Post

def list_posts(request):
	last_post = Post.objects.last()
	output = '마지막 글 본문 : {}'.format(
		last_post.content
	)

	return HttpResponse(output)