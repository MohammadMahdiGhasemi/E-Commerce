from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Sends a test email'

    def handle(self, *args, **options):
        subject = 'Test Email'
        message = 'This is a test email.'
        from_email = 'ghasemi.ferdosi@gmail.com'
        to_email = 'ghasemi.programmer@gmail.com'

        send_mail(subject, message, from_email, [to_email])
        self.stdout.write(self.style.SUCCESS('Test email sent successfully.'))