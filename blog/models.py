from django.db import models


class Post(models.Model):
    STATUS = (
        (0,)
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
