# Generated by Django 4.2.9 on 2024-01-27 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboardapp', '0013_alter_student_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(default='city_name', max_length=50),
        ),
        migrations.CreateModel(
            name='Filmstarinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acted', models.IntegerField()),
                ('coactor', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('totalfilms', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'filmstarinfo',
                'verbose_name_plural': 'filmstarinfo',
                'db_table': 'filmstarinfo',
            },
        ),
    ]
