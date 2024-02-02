from django.shortcuts import render,redirect
from .models import Notes
# from datetime import datetime
# from django.utils import timezone
import datetime
import time
from . models import *
from . forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from django.views import generic 
from .forms import HomeworkForm
from youtubesearchpython import VideosSearch
import requests
from .forms import DashboardForm
from .forms import UserRegistrationForm
import wikipedia
from .forms import ConversionForm, ConversionLengthForm, ConversionMassForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
# from rest_framework.generics import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import *
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


#ModelViewSet
#+
#Router register
class Techtoolviewset(viewsets.ModelViewSet):
      queryset=Techtools.objects.all()
      serializer_class=TechtoolsSerializer   #class define must
    #   authentication_classes=[BasicAuthentication]
    #   permission_classes=[IsAuthenticated]
    

#ViewSet
#+
#Router+RouterRegister
class Cityviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=City.objects.all()
        serializer=CitySerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=City.objects.get(id=id)
            serializer=CitySerializer(queryset)
            return Response(serializer.data)
    def update(self,request,pk):
        id=pk
        queryset=City.objects.get(pk=id)
        serializer=CitySerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id=pk
        queryset=City.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'deleted'})
    def create(self,request):
        queryset=City.objects.all()
        serializer=CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
 #ConcreteAPIView   
        
class FilmstarinfoListAPIView(ListAPIView):
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer  #class define must
class FilmstarinfoCreateAPIView(CreateAPIView):
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer   #class define must
class FilmstarinfoRetrieveAPIView(RetrieveAPIView):
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer   #class define must
class FilmstarinfoUpdateAPIView(UpdateAPIView):
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer    #class define must  
class FilmstarinfoUpdateAPIView(UpdateAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer    #class define must
class FilmstarinfoDestroyAPIView(DestroyAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer    #class define must
class FilmstarinfoListCreateAPIView(ListCreateAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer    #class define must
class FilmstarinfoRetrieveUpdateAPIView(RetrieveUpdateAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer   #class define must
class FilmstarinfoRetrieveDestroyAPIView(RetrieveDestroyAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer   #class define must
class FilmstarinfoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):        
    queryset=Filmstarinfo.objects.all()
    serializer_class=FilmstarinfoSerializer   #class define must   
          
#GenericAPIView       
class Studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  #class define must 
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request) 
    
class Studentdel(GenericAPIView,DestroyModelMixin,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer   #class define must 
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
       
class Studentup(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer   #class define must 
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
        
#Mixins        
@api_view(['GET'])#READ
def Booklist(request):
    booksobj=BooksModel.objects.all()
    serializer=BookSerializer(booksobj,many=True)  #Ther is no class define
    return Response(serializer.data)

@api_view(['POST'])#CREATE
def post_Book(request):
    booksobj=BooksModel.objects.all()
    serializer=BookSerializer(data=request.data)  #Ther is no class define
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])#UPDATE
def update_Book(request,id):
    booksobj=BooksModel.objects.get(id=id)
    serializer=BookSerializer(instance=booksobj,data=request.data)  #Ther is no class define
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])#DELETE
def delete_Book(request,id):
    booksobj=BooksModel.objects.get(id=id)   #Ther is no class define
    booksobj.delete()
    return Response("Your Book is Permanently deleted") 

@api_view(['GET'])
def demo(request):
    student_obj=Student.objects.all() 
    serializer=StudentSerializer(student_obj,many=True)   #Ther is no class define
    return Response({'status':200,'payload':serializer.data})



   
def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page or any other desired page

# Create your views here.

def my_view(request):
    # Your view logic here
    return render(request, 'bootstrap4/uni_form.html')
@login_required
def home(request):
    return render(request,'dashboard/home.html')
def sai(request):
    return render(request,'dashboard/home.html')
@login_required
# @api_view()
def notes(request):
    # sai_object = Notes.objects.all()
    # serializer =NotesSerializer(sai_object,many=True)
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'],created_date=request.POST['created_date'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} successfully!")
        return redirect('notes')

    else:
        form = NotesForm()    

    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,
               'form':form
               }
    return render(request,'dashboard/notes.html',context)
@login_required
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')


# def note_details(generic, DetailView):
#     model = Notes
login_required
class NotesDetailView(generic.DetailView):
    model = Notes
    template_name = 'dashboardapp/notes_detail.html'
@login_required
def homework(request):
    # import pdb; 
    # pdb.set_trace()
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                finished = True if finished == 'on' else False
            except KeyError:
                finished = False 

            homeworks = Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                is_finished=finished,
                due=request.POST['due'],
            )
            homeworks.save()
            messages.success(request,f"Homework Added from {request.user.username} successfully!")
            return redirect('homework')
    else: 
        form = HomeworkForm()     
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done =True
    else:
        homework_done = False    

    context = {
        'homeworks': homework,
        'homeworks_done': homework_done,
        'form': form,
    }
    
    return render(request, 'dashboard/homework.html', context)

@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')
     
@login_required
def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')


def youtube(request):
    if request.method == "POST":
        # import pdb;
        # pdb.set_trace()
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []


        for i in video.result()['result']:
            result_dict = {
                'input' : text,
                'title' : i['title'],
                'duration' : i['duration'],
                'thumbnail' : i['thumbnails'][0]['url'],
                'channel' : i['channel']['name'],
                'link' : i['link'],
                'views' : i['viewCount']['short'],
                'published' : i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+= j['text']

                    result_dict['description']= desc
                result_list.append(result_dict)


        context={'form':form,'results':result_list}                                       
        return render(request,'dashboard/youtube.html',context)    
    else:
        form = DashboardForm()
    context = {'form':form}
    return render(request,"dashboard/youtube.html",context)

@login_required
def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST["is_finished"]
                if finished == "on":
                    finished = True
                else:
                    finished = False

            except:
                finished = False

            todo = Todo(
                user = request.user,
                title = request.POST["title"],          
                created_date = request.POST["created_date"],
                is_finished = finished               

            ) 
            todo.save() 
            messages.success(request,f"Todo Added from {request.user.username}!")
            return redirect('todo')

    else:        
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todo_done = True
    else:
        todo_done =False    
    context = {
        "todo":todo,
        "form":form,
        "todo_done":todo_done

    }
    return render(request,"dashboard/todo.html",context)

@login_required
def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')


def books(request):
    if request.method == "POST":
        # import pdb;
        # pdb.set_trace()
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()

        result_list = []
        for i in range(10):
            # import pdb
            # pdb.set_trace()
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle' : answer['items'][i]['volumeInfo'].get('subtitle'),
                'description' : answer['items'][i]['volumeInfo'].get('description'),
                'count' : answer['items'][i]['volumeInfo'].get('pagrCount'),
                'categories' : answer['items'][i]['volumeInfo'].get('categories'),
                'rating' : answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail' : answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview' : answer['items'][i]['volumeInfo'].get('previewLink'),
            }

            result_list.append(result_dict)
        context={
            'form':form,
            'results':result_list
        }                                       
        return render(request,'dashboard/books.html',context)    
    else:
        form = DashboardForm()
    context = {'form':form
    }
    return render(request,"dashboard/books.html",context) 


def dictionary(request):
    if request.method == "POST":
        # import pdb;
        # pdb.set_trace()
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()

        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form':form,
                'input':text,
                'phonetics': phonetics,
                'audio':audio,
                'definition':definition, 
                'example':example,
                'synonyms':synonyms              
            }

        except:
            context={
                'form':form,
                'input':''
            }
        return render(request,"dashboard/dictionary.html",context)

    else:    
        form = DashboardForm()
        context = {"form":form}
    return render(request, 'dashboard/dictionary.html',context)


def wiki(request):
    if request.method=="POST":
        # import pdb
        # pdb.set_trace()
        text = request.POST['text']
        form= DashboardForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request,"dashboard/wiki.html",context)
    
    else:
        form=DashboardForm()
        context={
            'form':form
        }
    return render(request,'dashboard/wiki.html',context)


def conversion(request):
    if request.method == "POST":
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first == 'yard' and second =='foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first == 'foot' and second =='yard':
                        answer = f'{input} foot = {int(input)/3} yard'

                    context = {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer

                    }
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first == 'pound' and second =='kilogram':
                        answer = f'{input} pound = {int(input)*0.453592} kilogram'
                    if first == 'kilogram' and second =='pound':
                        answer = f'{input} kilogram = {int(input)*2.20462} pound'

                    context = {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer

                    }

    else:                                
        form = ConversionForm()
        context={"form":form,
                 "input":False
        }

      
    return render(request,"dashboard/conversion.html",context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            send_registration_email(username, email)

            messages.success(request,f"Account Created for {username}!!")
            # return redirect('register')
            return redirect("login")
    else:         
        form = UserRegistrationForm()
    context = {
        "form":form
    }
    return render(request,"dashboard/register.html",context)

def send_registration_email(username, email):
    subject = "Welcome to SAI's webportal"
    # import pdb
    # pdb.set_trace() 
    login_url = reverse('login')

    message = f'Thanks you Dear {username} for registering ! We appreciate your Login.\n\n'
    message += "Click the following link to log in to our (SAI's) web portal: http://192.168.180.205:9000/login/"


    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)



@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished =False,user= request.user)
    todos = Todo.objects.filter(is_finished =False,user= request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False

    context = {
        'homeworks': homeworks,
        'todos': todos,
        'homework_done': homework_done,
        'todos_done' : todos_done

    }        
        
    return render(request, "dashboard/profile.html",context)


def error_404(request, exception=None):   
    return render(request, 'dashboard/error_404.html', status=404)
def error_403(request, exception=None):
    return render(request, 'dashboard/error_404.html', status=403)
# def server_error(request):
#     return render(request, 'dashboard/error_500.html', status=500)
def server_error(request):
    return render(request, 'dashboard/error_500.html', status=500)


