from django.conf.urls import url

from . import views
from .views import list_posts

urlpatterns = [
	url(r'list/$', list_posts),
]