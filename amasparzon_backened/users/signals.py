from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template

#custom user model
from django.contrib.auth import get_user_model
Users = get_user_model()

from amasparzon_backened.settings import EMAIL_HOST_USER

@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Send email confirmation to user when account is created
    """
    if created:

        context = { 'user' : instance }

        message = get_template('account_created_mail.html').render(context)

        mail = EmailMessage(
            subject =  "Vielen Dank für deine Anfrage!",
            body = message,
            from_email = EMAIL_HOST_USER,
            to = [instance.email],
        )
        mail.content_subtype = "html"

        return mail.send()

