from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    upload_file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.IntegerField(default=0, null=False)
    image = models.TextField(null=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return self.upload_file.name.split('/')[-1]
    
    def get_file_ext(self):
        return self.get_file_name.split('.')[-1]
    

class Category(models.Model):
    category = models.CharField(max_length=100, null=False)

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'


class Comment(models.Model):
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return self.post.get_absolute_url()

    def __str__(self):
        return f'{self.author} :: {self.content}'


class Recomment(models.Model):
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return self.comment.get_absolute_url()

    def __str__(self):
        return f'{self.author} :: {self.content}'