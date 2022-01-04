from django.template.loader import get_template
from users.models import MyUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage

User = settings.AUTH_USER_MODEL
from amasparzon_backened.settings import EMAIL_HOST_USER

class Product(models.Model):
    asin = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.TextField()
    image = models.TextField(max_length=2049)
    user = models.ManyToManyField(User, blank=True)
    
    class Meta:
        ordering = ('name',)    

    def __str__(self) -> str:
        return self.name

    def get_product_url(self) -> str:
        """
        Get the url of the product
        """
        return f'https://www.amazon.de/dp/{self.asin}'

    def send_confirmation_mail(self, user):
        """
        Send confirmation mail to user
        """
        context = { 'product' : self, 'user' : user }

        message = get_template('product_created_mail.html').render(context)

        mail = EmailMessage(
            subject =  "Wir beobachten dein Produkt jetzt!",
            body = message,
            from_email = EMAIL_HOST_USER,
            to = [user.email],
        )
        mail.content_subtype = "html"

        return mail.send()

class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(editable=False, auto_now=True)
    product = models.ForeignKey(Product, on_delete=CASCADE)

    def __str__(self):
        return str(self.price)


    