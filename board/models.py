from django.db import models

class Board_Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    category = models.CharField(max_length=100, null=False)
    upload_file = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.IntegerField(default=0, null=False)
    image = models.TextField(null=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f'/board/{self.pk}/'
    
    def get_file_name(self):
        return self.upload_file.name.split('/')[-1]
    
    def get_file_ext(self):
        return self.get_file_name.split('.')[-1]
    

class Board_Comment(models.Model):
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    board_post = models.ForeignKey('Board_Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} :: {self.content}'
    
    def get_absolute_url(self):
        return self.board_post.get_absolute_url()


class Board_Recomment(models.Model):
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    board_comment = models.ForeignKey('Board_Comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} :: {self.content}'
    
    def get_absolute_url(self):
        return self.board_comment.get_absolute_url()