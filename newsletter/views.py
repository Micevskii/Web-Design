# newsletter/views.py
from django.shortcuts import render, redirect
from .forms import NewsletterForm
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            return redirect('index') 
    else:
        form = NewsletterForm()
    
    return render(request, 'index', {'form': form})
