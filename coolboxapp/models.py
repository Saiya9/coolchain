from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from datetime import datetime

STATUS =(
    ('Shipped', 'Shipped'),
    ('Shipping', 'Shipping'),
    ('Cancelled', 'Cancelled')
)

ROLE = (
    ('admin','ADMIN'),
    ('driver','DRIVER')
)

# Create your models here.
class User(AbstractUser):
    admin_id = models.CharField(max_length=10,primary_key=True)
    role_user = models.CharField(max_length=20, choices=ROLE, blank=True)
    id_card = models.CharField(max_length=13)
    profile_user = models.ImageField(default='/Profile_Images/default.png', upload_to='Profile_Images')
    
    def __str__(self):
        return f"{self.admin_id}: {self.username}"

class Driver(models.Model):
    driver_id = models.CharField(max_length=10,primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercreate")
    driver_user = models.CharField(max_length=30)
    driver_password = models.CharField(max_length=30)
    driver_fname = models.CharField(max_length=30)
    driver_lname = models.CharField(max_length=30)
    driver_email = models.CharField(max_length=30)
    id_card = models.CharField(max_length=13)
    driver_phone = models.CharField(max_length=30)
    drivinglicense_id = models.CharField(max_length=30)
    issue_date = models.DateField(blank=True,null=True)
    expire_date = models.DateField(blank=True,null=True)
    profile_driver= models.ImageField(default='/Driver_Images/default.png', upload_to='Driver_Images')

    def __str__(self):
        return f"{self.driver_id}: {self.driver_name}"

class Car(models.Model):
    car_id = models.CharField(max_length=10,primary_key=True)
    car_band = models.CharField(max_length=20)
    total_coolbox_weight = models.FloatField(blank=True, null=True)
    temp_max = models.FloatField(blank=True, null=True)
    temp_min = models.FloatField(blank=True, null=True)
    license_plate = models.CharField(max_length=15)
    car_picture = models.ImageField(upload_to='Car_images')

    def __str__(self):
        return f"{self.car_id}: {self.license_plate}"

class Type_medicine(models.Model):
    type_id = models.CharField(max_length=10,primary_key=True)
    type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.description}"

class Medicine(models.Model):
    medicine_id = models.CharField(max_length=10,primary_key=True)
    medicine_name = models.CharField(max_length=50)
    medicine_type = models.ForeignKey(Type_medicine, on_delete=models.CASCADE, related_name="medicinetype")
    medicine_tempmax = models.FloatField(blank=True, null=True)
    medicine_tempmin = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=200)
    total = models.FloatField(blank=True, null=True)
    t_measurement = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.medicine_name}: {self.medicine_type}"

class Coolbox(models.Model):
    coolbox_id = models.CharField(max_length=40,primary_key=True)
    medicine_name = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="medicinename")
    weight = models.FloatField(blank=True, null=True)
    coolboxtemp_max = models.FloatField(blank=True, null=True)
    coolboxtemp_min = models.FloatField(blank=True, null=True)
    dimension = models.CharField(max_length=40)
    d_measurement = models.CharField(max_length=40)
    t_measurement = models.CharField(max_length=40)
    total = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, blank=True)

    def __str__(self):
        return f"{self.medicine_name}"




class shipping(models.Model):
    shipping_id = models.CharField(max_length=15,primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driverfk")
    
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="carfk")
    coolbox_id = models.ManyToManyField(Coolbox,  related_name="coolboxfk")
    ship_date = models.DateField(blank=True,null=True)
    ship_time = models.TimeField(blank=True,null=True)
    original = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.shipping_id}: {self.driver_id}"

