from django.db import models

class Board_Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    category = models.CharField(max_length=100, null=False)
    upload_file = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.IntegerField(default=0, null=False)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return self.upload_file.name.split('/')[-1]
    
    def get_file_ext(self):
        return self.get_file_name.split('.')[-1]


class Board_Image(models.Model):
    image = models.ImageField(upload_to='board/images/%Y/%m/%d/', blank=True)

    board_post = models.ForeignKey('Board_Post', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_file_name()}'

    def get_file_name(self):
        return self.image.name.split('/')[-1]
    
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


class Board_Recomment(models.Model):
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    board_comment = models.ForeignKey('Board_Comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} :: {self.content}'