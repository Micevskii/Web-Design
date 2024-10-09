from django.shortcuts import render,redirect
from .models import Contactform
from django.contrib import messages
from django.core.mail import send_mail

def contact (request):
    if request.method == 'POST':
       name = request.POST['name']
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']
       user_id = request.POST['user_id']

       kontakt = Contactform(name=name, email=email, subject=subject, message=message, user_id=user_id)

       kontakt.save()
       full_message = f"Порака: {message}\n\nИспратил: {email}"

       #Send mail
       send_mail(
           subject,
           full_message,
           'micevski231239@gmail.com',
           [email, 'micevskifilip09@gmail.com'],
           fail_silently=False
       )

       return redirect('index')