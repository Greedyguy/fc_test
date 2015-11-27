from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	tags = models.ManyToManyField('Tag')
	category = models.ForeignKey('Category')

	def __str__(self):
		return '<Post {} : {}>'.format(self.pk, self.title[:8])

	def get_absolute_url(self):
		return '/list/{}/'.format(self.pk)

class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	post = models.ForeignKey(Post)

	def __str__(self):
		return '<Comment {} : {} 번째 게시물 댓글>'.format(self.pk, self.post_id, self)

class Tag(models.Model):
	name = models.CharField(max_length=40)

class Category(models.Model):
	name = models.CharField(max_length=80)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)