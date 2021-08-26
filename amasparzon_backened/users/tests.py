import unittest
from users.models import MyUser
from django.test import TestCase

class MyUserTestCase(TestCase):
    """
    Test for checking wheather the email is unique.
    """
    @unittest.expectedFailure
    def test_email_uniqueness(self):
        MyUser.objects.create(email="testmail@amasparzon.de", password="1234")
        MyUser.objects.create(email="testmail@amasparzon.de", password="1234")
    

