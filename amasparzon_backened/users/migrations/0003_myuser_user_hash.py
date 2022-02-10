# Generated by Django 3.2.6 on 2021-12-21 20:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_hash',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]