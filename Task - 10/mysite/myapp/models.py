from django.db import models

# Create your models here.
class student(models.Model):
    s_id = models.AutoField(primary_key=True)
    stu_user_name = models.CharField(max_length=30 , default='NULL22')
    user_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    