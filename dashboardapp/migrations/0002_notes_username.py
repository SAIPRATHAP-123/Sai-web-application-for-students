# Generated by Django 5.0 on 2023-12-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='username',
            field=models.CharField(blank=True, max_length=251),
        ),
    ]
