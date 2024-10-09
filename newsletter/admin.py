# newsletter/admin.py
from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    actions = ['send_newsletter']

    def send_newsletter(self, request, queryset):
        for subscriber in queryset:
            send_mail(
                subject='Your Newsletter',
                message='Here is the latest newsletter content.',  # Customize this message
                from_email='filipmicevski407@gmail.com',  # Replace with your email
                recipient_list=[subscriber.email],
                fail_silently=True,
            )
        self.message_user(request, "Newsletter sent successfully to selected subscribers!")

    send_newsletter.short_description = "Send Newsletter to Selected Subscribers"

admin.site.register(Subscriber, SubscriberAdmin)
