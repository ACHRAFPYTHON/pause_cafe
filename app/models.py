from datetime import datetime
from email.policy import default
from operator import mod
from tkinter import TRUE
from unicodedata import name
from cv2 import dft
from django.db import models
from django.forms import DecimalField
from matplotlib import image

class serveur(models.Model):
    matricule=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField( max_length=254,default="")
    password=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos',null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
    
class boissonschaudes(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    desceription=models.TextField(max_length=200,default="")
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class jus(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    desceription=models.TextField(max_length=200)
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class crepes(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    desceription=models.TextField(max_length=200)
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class carte(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    desceription=models.TextField(max_length=200)
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class boissonsfraiches(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    desceription=models.TextField(max_length=200)
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name


class glaces(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    desceription=models.TextField(max_length=200)
    prix=models.DecimalField(decimal_places=2,max_digits=4,default=0)
    image=models.ImageField(upload_to='photos',null=True,blank=True)
    rate=models.IntegerField()
    stock=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class lignecommande(models.Model):
    produits=models.CharField(max_length=30,primary_key=True)
    quantite=models.IntegerField()
    remarque=models.TextField(default="")
    price=models.IntegerField()

class comande(models.Model):
    
    time=models.TimeField(primary_key=True,default=datetime.time(datetime.now()))
    date=models.DateField(default=datetime.date(datetime.now()))
    listitem=models.TextField()
    price=models.IntegerField()
