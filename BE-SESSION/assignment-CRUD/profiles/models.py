from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, default="이름", null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=20, default="010-0000-0000", null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)
