from django.db import models

#server of devices with alerts and manegment

#Alert of the Device
class Alert (models.Model):
    name=models.CharField(max_length=200)#name of the alert
    descr=models.CharField(max_length=100)#description of the alert
    number_iP_of_d=models.CharField(max_length=200)#number ip of the alert 
    type_Alert = models.CharField(max_length=200)#typ of alert pf alert

#Data like index or else on the device
class Data(models.Model):
    name=models.CharField(max_length=200)#id of the data
    descr=models.CharField(max_length=100)#description of the data
    number_iP_of_d=models.CharField(max_length=200)#number ip of the data 
    type_data = models.CharField(max_length=200)#typ of alert of data
    namber=models.IntegerField(max_length=200)#number like 100 or -10



#Report on the device
class Report(models.Model):
    name=models.CharField(max_length=200)#id of the report
    descr=models.CharField(max_length=100)#description of the report
    number_iP_of_d=models.CharField(max_length=200)#number ip of the report 
    type_data = models.CharField(max_length=200)#typ of alert of report
    namber=models.IntegerField(max_length=200)#number of report 


     

class Device (models.Model):
    name=models.CharField(max_length=200)
    descr=models.CharField(max_length=100)
    number_iP=models.CharField(max_length=200)
    connect=models.BooleanField(default=False)
    list_alerts=models.ForeignKey(Alert,on_delete=models.CASCADE)
    list_data=models.ForeignKey(Data,on_delete=models.CASCADE)
