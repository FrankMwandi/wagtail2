from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page

@register_snippet

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="blog_posts" )
    
    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    """
    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]
    """