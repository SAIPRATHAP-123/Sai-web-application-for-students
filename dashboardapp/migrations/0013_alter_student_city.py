# Generated by Django 4.2.9 on 2024-01-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0012_student_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(default='Bangalore', max_length=50),
        ),
    ]
