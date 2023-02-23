from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Contact, Team,Clients
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request,'core/index.html')


def about(request):
    team = Team.objects.filter()
    clients = Clients.objects.filter()
    
    context = {'team':team, 'clients':clients}
    return render(request, 'core/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            comment = Contact()
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.message = form.cleaned_data['message']
            comment.save()
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            HttpResponseRedirect('/contact')

    else:
        form = ContactForm()

    return render(request,'core/contact.html',{'form':form})


