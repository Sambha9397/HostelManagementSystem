from django.db import models

# Create your models here.

class SignUp(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mob = models.CharField(max_length=10)
    pwd = models.CharField(max_length=8)  # Consider hashing the password
    rpwd = models.CharField(max_length=8)  # This is redundant; consider removing it
    img = models.ImageField(upload_to='images/')
    doc = models.FileField(upload_to='documents/')
    

    class Meta:
        db_table = "register"
         

class Sharing(models.Model):
    sharing_number = models.IntegerField(unique=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)

  
class Room(models.Model):
    room_number = models.IntegerField()
    bed_number=models.IntegerField()  

# models.py

from django.db import models

class Sharing(models.Model):
    sharing_number = models.IntegerField(unique=True)
    rent = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Sharing {self.sharing_number}"


class Rooms(models.Model):
    room_number = models.IntegerField(unique=True)
    bed_number = models.IntegerField()
    sharing = models.ForeignKey(Sharing, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f"Room {self.room_number}, Bed {self.bed_number}"


class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"{self.full_name} ({self.room})"

 

class room_booked(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mob = models.CharField(max_length=10)
    sharing_number = models.IntegerField(unique=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    room_number=models.IntegerField()
    bed_number=models.IntegerField()


