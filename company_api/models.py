from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250,null=False,unique=True)
    location = models.CharField(max_length=250,null=False)
    domain = models.CharField(max_length=100,choices=(('IT','IT'),('Non-IT','Non_IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250,null=False)
    email = models.CharField(max_length=250,null=False)
    phone_no = models.CharField(max_length=10,null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name