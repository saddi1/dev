from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from Vs_cloud_tech import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'VS Cloud Tech'})


def about(request):
    return render(request, 'about.html', {'title': 'About | VS Cloud Tech'})


def services(request):
    return render(request, 'services.html', {'title': 'Services | VS Cloud Tech'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = Contact()
            subject = "VS Cloud Tech Pvt Ltd."
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.number = form.cleaned_data['number']
            obj.message = form.cleaned_data['message']
            obj.save()
            html_message = render_to_string('mail_template.html', {'obj.name': obj.name})
            plain_message = strip_tags(html_message)
            try:
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER,
                          [obj.email, ], html_message=html_message, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.info(request, 'Hi, Thanks for contacting us! We will get back to you soon')
            return redirect('.')
        else:
            messages.info(request, 'Some error in saving form!')
            return redirect('.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'title': 'Contact Us | VS Cloud Tech'})
