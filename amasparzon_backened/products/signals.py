from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from django.db.models.signals import m2m_changed

from amasparzon_backened.settings import EMAIL_HOST_USER

from .models import Product,Price
        
# @receiver(m2m_changed, sender=Product.user.through)
# def create_user_profile(sender, instance, **kwargs):
#     """
#     Send email confirmation to user when added to product
#     """
#     pass

    # if created:

    #     context = { 'product' : instance, 'user' : instance.user }

    #     message = get_template('product_created_mail.html').render(context)

    #     mail = EmailMessage(
    #         subject =  "Wir beobachten dein Produkt jetzt!",
    #         body = message,
    #         from_email = EMAIL_HOST_USER,
    #         to = [instance.user.email],
    #     )
    #     mail.content_subtype = "html"

    #     return mail.send()

