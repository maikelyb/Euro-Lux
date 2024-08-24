from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,email,['magdysameh945@gmail.com'])  # Change 'your@email.com' to your email address
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {"form":form})
