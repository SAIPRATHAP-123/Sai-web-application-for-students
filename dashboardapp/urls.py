from django.urls import path 
from . import views
from .views import notes, delete_note 
from .views import NotesDetailView 
from django.contrib import admin
from .views import *
from .views import delete_Book



urlpatterns = [
    # path('', demo),
    path('list', Booklist),
    path('add/',post_Book),
    path('update/<int:id>',update_Book),
    path("delete/<int:id>",delete_Book),
    path('',views.home,name='home'),
    path('sai/',views.sai,name='sai'),
    path('notes/',views.notes,name='notes'),
    # path('note_details/',views.note_details,name='note_details'),
    path('delete-note/<int:pk>/',views.delete_note, name='delete-note'),
    path('notes_detail/<int:pk>/',views.NotesDetailView.as_view(), name='notes-detail'),
    path('homework/',views.homework,name='homework'),
    # path(' delete_homework/<int:pk>/',views. delete_homework, name=' delete_homework'),
    path('update_homework/<int:pk>/',views.update_homework, name="update-homework"),
    path('delete-homework/<int:pk>/',views.delete_homework, name='delete-homework'),
    path('youtube/',views.youtube,name='youtube'),
    path('todo/',views.todo,name='todo'),
    path('update-todo/<int:pk>/',views.update_todo, name="update-todo"),
    path('delete-todo/<int:pk>/',views.delete_todo, name='delete-todo'),
    path('books/',views.books,name='books'),
    path('dictionary/',views.dictionary,name='dictionary'),
    path('wiki/',views.wiki,name='wiki'),
    path('conversion/',views.conversion,name='conversion'),
    


]
 