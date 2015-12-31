from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogArticle(models.Model):
	title = models.CharField(max_length=400)
	blog_content = models.TextField()
	autor = models.ForeignKey(User)
