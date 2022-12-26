from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    longUrl = models.TextField(null=False, blank=False)
    shortUrl = models.CharField(max_length=30, primary_key=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortUrl

    class Meta:
        ordering = ['create']

    def clean(self):
        # data from the form is fetched using super function
        super(Url, self).clean()
        short = self.shortUrl
        long = self.longUrl
        # conditions to be met for the username length
        if ' ' in short:
            raise ValidationError('Short url is not allowed to contain spaces')
        if ' ' in long:
            raise ValidationError('Long url is not allowed to contain spaces')
        return self
