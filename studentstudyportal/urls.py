"""
URL configuration for studentstudyportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.urls.conf import include
from dashboardapp import views as dash_views
from dashboardapp import views
from django.contrib.auth import views as auth_views
from dashboardapp.views import custom_logout
from dashboardapp.views import error_403, error_404
from django.conf import settings
from django.conf.urls import handler500
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# from django.views.generic import TemplateView  # Import TemplateView


router=DefaultRouter()
router.register('build',views.Cityviewset,basename='city')
router.register('builds',views.Techtoolviewset,basename='Tech')


handler403 = error_403 
handler404 = error_404
handler500 = 'dashboardapp.views.server_error'
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboardapp.urls')),
    path('',include(router.urls)),
    path('', views.home, name='home'), 
    path('list/', views.FilmstarinfoListAPIView.as_view()),
    path('create/', views.FilmstarinfoCreateAPIView.as_view()),
    path('retrieve/<int:pk>/', views.FilmstarinfoRetrieveAPIView.as_view()),
    path('update/<int:pk>/', views.FilmstarinfoUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.FilmstarinfoDestroyAPIView.as_view()),
    path('listcreate/', views.FilmstarinfoListCreateAPIView.as_view()),  
    path('ru/<int:pk>/', views.FilmstarinfoRetrieveUpdateAPIView.as_view()),
    path('rd/<int:pk>/', views.FilmstarinfoRetrieveDestroyAPIView.as_view()),
    path('rud/<int:pk>/', views.FilmstarinfoRetrieveUpdateDestroyAPIView.as_view()),    
    path('apicreate/', views.Studentlistcreate.as_view()),   
    path('deldis/<int:pk>/', views.Studentdel.as_view()),
    path('register/',dash_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="dashboard/login.html"),name = 'login'),
    path('profile/',dash_views.profile,name='profile'),
    path('logout/', custom_logout, name='logout'),
    # Add a catch-all pattern for 404 errors
    re_path(r'^.*$', error_404),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # path('logout/',auth_views.LogoutView.as_view(template_name="dashboard/logout.html"),name = 'logout'),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)