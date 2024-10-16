from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog}'