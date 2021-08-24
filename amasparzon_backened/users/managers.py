from .models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        
        u = self.create_user(email,
                        password=password,
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u