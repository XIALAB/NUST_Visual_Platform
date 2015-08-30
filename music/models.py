import datetime

from django.db import models
from django.utils import timezone


class WangyiMusic(models.Model):
    sm_id = models.CharField(primary_key=True, max_length=50)
    user_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    cat = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    ctime = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    pnum = models.IntegerField(default=0)
    colnum = models.IntegerField(default=0)
    shnum = models.IntegerField(default=0)
    comnum = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

