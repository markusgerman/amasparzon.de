from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template

from amasparzon_backened.settings import EMAIL_HOST_USER

from .models import Product

@receiver(post_save, sender=Product)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Send email confirmation to user when product is created
    """
    if created:

        context = { 'product' : instance, 'user' : instance.user }

        message = get_template('product_created_mail.html').render(context)

        mail = EmailMessage(
            subject =  "Wir beobachten dein Produkt jetzt!",
            body = message,
            from_email = EMAIL_HOST_USER,
            to = [instance.user.email],
        )
        mail.content_subtype = "html"

        return mail.send()