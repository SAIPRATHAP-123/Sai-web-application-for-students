from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from django.utils import timezone
# import pytz
import datetime
from django.utils import timezone


# Create your models here.

class BooksModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    author =models.CharField(max_length=50)
    read_by =models.CharField(max_length=50)
    
    class Meta:
        db_table = "booksmodel"
        verbose_name = "booksmodel"  
        verbose_name_plural  = "booksmodel"
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    age = models.IntegerField()
    father_name =models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='city_name')
    
    class Meta:
        db_table = "student"
        verbose_name = "student"  
        verbose_name_plural  = "student"
    
    def __str__(self):
        return self.name
    
class Filmstarinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    acted= models.IntegerField()
    coactor=models.CharField(max_length=50)
    age = models.IntegerField()
    totalfilms=models.IntegerField()
    
     
    class Meta:
        db_table = "filmstarinfo"
        verbose_name = "filmstarinfo"  
        verbose_name_plural  = "filmstarinfo"
    
    def __str__(self):
        return self.name 
    
class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    main_towns= models.CharField(max_length=100)
    main_malls=models.CharField(max_length=100)
    Total_pop=models.IntegerField()
    famous=models.CharField(max_length=100)
    
    class Meta:
        db_table = "city"
        verbose_name = "city"  
        verbose_name_plural  = "city"

    def __str__(self):
        return self.name
class Techtools(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    names=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    where_using=models.CharField(max_length=100) 
    how_many_users=models.IntegerField()
    
    class Meta:
        db_table = "techtools"
        verbose_name = "techtools"  
        verbose_name_plural  = "techtools"
        
    def __str__(self):
        return self.domain    
    
                
        
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=251, blank=True)
    title = models.CharField(max_length=200)
    description=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "notes"
        verbose_name = "notes"  
        verbose_name_plural  = "notes"

    def __str__(self):
        return self.title
    

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description=models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "homework"
        verbose_name = "Homework"  
        verbose_name_plural  = "Homework"

    def __str__(self):
        return self.subject  


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=251)
    is_finished = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "todo"
        verbose_name = "Todo"
        verbose_name_plural = "Todo"

    def __str__(self):
        return self.title    


     


        
