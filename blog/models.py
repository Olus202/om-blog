import datetime
from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    pub_date = models.DateField(default=datetime.date.today())
    image = models.ImageField(upload_to='photos/posts', default='')
