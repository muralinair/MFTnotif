from django.db import models
#from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=150,default='')
    password=models.CharField(max_length=150,default='')
    email=models.EmailField()
    category=models.CharField(max_length=30,default='customer')

class OrdersTable(models.Model):
    ordersId=models.CharField(max_length=100)
    ordersStatus=models.CharField(max_length=10)
    orderCustomerID=models.CharField(max_length=10,default='')
    ordersSellerID=models.CharField(max_length=10,default='')

class statuschangetemptable(models.Model):
    orderIdchange=models.CharField(max_length=100)
    ordersstatuschange=models.CharField(max_length=10)
    

