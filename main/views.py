
from django.shortcuts import render
from datetime import datetime
from main.models import Contact
from django.contrib import messages
from django.conf import settings as conf_settings
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    context ={}
    return render(request, 'main/index.html',context)


def projects (request):
    context ={}
    return render (request, 'main/projects.html',context)


def skills(request):
    context ={}
    return render (request, 'main/skills.html',context)

def about(request):
    context ={}
    return render (request, 'main/about.html',context) 

def services(request):
    context ={}
    return render (request, 'main/services.html',context) 



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        EmailMessage(
            'New message from %s' %name,
            'Hi admin, new message form this email address: %s\n\n Message: %s' %(email, message),
            conf_settings.EMAIL_HOST_USER,
            ['vivekiiit72@gmail.com', ],
        ).send()


        contact = Contact(name=name, email=email, subject=subject, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, 'main/contact.html',{'name':name})
    
    else:
        return render(request, 'main/contact.html')
   
   

def certificates(request):
    context ={}
    return render (request, 'main/certificates.html',context)

