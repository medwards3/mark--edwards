from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return reverse('blog.views.post', args=[self.slug])

	def was_published_recently(self):
		return self.published >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.CharField(max_length=55)
	text = models.TextField()


