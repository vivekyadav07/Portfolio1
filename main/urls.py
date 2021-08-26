
from django.urls import path 
from main import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('projects/',views.projects, name ='projects'),

    path('skills/',views.skills,name = 'skills'),
    path('about/',views.about,name = 'about'),
    path('services/',views.services,name = 'services'),
    path('contact/',views.contact,name = 'contact'),
    #path('Project & certificates/',views.Project-certificates,name = 'Project & certificates'),
    path('certificates/',views.certificates, name = 'certificates'),
   # path('resume/',views.resume,name = 'resume'),






    path('',views.index, name = 'index')
]