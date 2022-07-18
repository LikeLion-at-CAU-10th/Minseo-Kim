from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, default="이름", null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=20, default="010-0000-0000", null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)

class Url(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    is_completed = models.BooleanField(default=False, null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
