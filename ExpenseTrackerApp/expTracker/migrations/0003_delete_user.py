# Generated by Django 5.0.6 on 2024-06-15 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expTracker', '0002_user_remove_expense_monthly_expenses_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
