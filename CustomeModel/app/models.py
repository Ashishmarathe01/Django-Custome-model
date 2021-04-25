


from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class MyManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have Phone Number')
       


        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),  
            password=password,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    

class Myclass(AbstractBaseUser):
    email                    = models.EmailField( verbose_name='email address', max_length=255,unique=True, )
    username                 =models.CharField(max_length=30,unique=True )
    phone                    =models.CharField(max_length=13,unique=True)
    date_joined              =models.DateField(verbose_name="date joined",auto_now_add=True)
    last_login               =models.DateField(verbose_name="date joined",auto_now=True)
    is_active                = models.BooleanField(default=True)
    is_staff                 =models.BooleanField(default=False)
    is_admin                 = models.BooleanField(default=False)
    is_superuser             =models.BooleanField(default=False)

    objects = MyManager()
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['phone',]

    def __str__(self):
        return self.email+" "+self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True    