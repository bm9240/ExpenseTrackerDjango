from django.db import models
from datetime import datetime

class Account(models.Model):
    name = models.CharField(max_length=100)
    expense = models.FloatField(default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    expense_list = models.ManyToManyField('Expense', blank = True)
    

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transportation', 'Transportation'),
        ('Housing', 'Housing'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    category = models.CharField(max_length=100, choices= CATEGORY_CHOICES)
    date = models.DateField(null = False,default = datetime.now().date())
    description = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)


    


    
