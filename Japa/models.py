from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.files.base import ContentFile
from PIL import Image
import base64
import json

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address_type = models.CharField(max_length=20, choices=[('house', 'House'), ('apartment', 'Apartment'), ('office', 'Office'), ('other', 'Other')], blank=True, null=True)
    door_number = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_id(self):
        return self.id
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

class NyKategori(models.Model):
    Navn = models.CharField(max_length=50)
    Billede = models.BinaryField(blank=True, null=True)

    def set_image(self, image):
        binary_data = image.read()
        self.Billede = binary_data
    
    def get_image(self):
        if self.Billede:
            return base64.b64encode(self.Billede).decode()
        else:
            return None
    
    def __str__(self):
        return self.Navn
    
class NyRestaurant(models.Model):
    Navn = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=50)
    Beskrivelse = models.CharField(max_length=50)
    Åbningstid = models.TimeField()
    Lukketid = models.TimeField()
    Leveringsgebyr = models.FloatField()
    Minimumsordre = models.FloatField()
    Kategorier = models.ManyToManyField(NyKategori)
    Billede = models.BinaryField(blank=True, null=True)

    def set_image(self, image):
        binary_data = image.read()
        self.Billede = binary_data

    def get_image(self):
        if self.Billede:
            return base64.b64encode(self.Billede).decode()
        else:
            return None
    
    def get_id(self):
        return self.id


    def __str__(self):
        return self.Navn
    

class NyUnderkategori(models.Model):
    Navn = models.CharField(max_length=50)
    Kategori = models.ManyToManyField(NyKategori)

    def __str__(self):
        return self.Navn

class NytMad(models.Model):
    Billede = models.BinaryField(blank=True, null=True)
    Navn = models.CharField(max_length=50)
    Beskrivelse = models.CharField(max_length=200)
    Pris = models.FloatField()
    Underkategori = models.ManyToManyField(NyUnderkategori)

    def set_image(self, image):
            binary_data = image.read()
            self.Billede = binary_data

    def get_image(self):
        if self.Billede:
            return base64.b64encode(self.Billede).decode()
        else:
            return None
        
    def get_id(self):
        return self.id

    def __str__(self):
        return self.Navn
    

class NyBestilling(models.Model):
    Kunde = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    KundeNavn = models.CharField(max_length=50, blank=True, null=True)
    Restaurant = models.ForeignKey(NyRestaurant, on_delete=models.CASCADE)
    Mad = models.TextField(default="[]")
    Leveringsadresse = models.TextField()
    Leveringsadresse_type = models.CharField(max_length=20, choices=[('house', 'House'), ('apartment', 'Apartment'), ('office', 'Office'), ('other', 'Other')], default='house')  # Provide a default value here
    Dørnummer = models.CharField(max_length=10, blank=True, null=True)
    Leveringsgebyr = models.FloatField()
    Total_pris = models.FloatField()
    Leverings_tid = models.TextField()
    Bestillings_tid = models.DateTimeField(auto_now_add=True)
    Leveret = models.BooleanField(default=False)
    Afhentet = models.BooleanField(default=False)
    Annulleret = models.BooleanField(default=False)
    Accepteret = models.BooleanField(default=False)

    Courier = models.ForeignKey(CustomUser, related_name='courier_orders', on_delete=models.SET_NULL, blank=True, null=True)


    def set_mad(self, mad_ids):
        self.Mad = json.dumps(mad_ids)

    def get_mad(self):
        return json.loads(self.Mad)

    def get_id(self):
        return self.id

    def __str__(self):
        return self.Bestillings_tid.strftime("%B %d, %Y, %I:%M %p")
