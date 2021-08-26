from users.models import MyUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    name = models.TextField()
    link = models.TextField()   
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        ordering = ('name',)    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(editable=False, auto_now=True)
    product = models.ForeignKey(Product, on_delete=CASCADE)

    def __str__(self):
        return str(self.price)


    