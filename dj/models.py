from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DJ(models.Model):
    MEMBER_TYPE_CHOICES = [
        ('S',"Student"),
        ('C',"Community Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_card_number = models.BigIntegerField(blank=True,null=True)
    graduation_year = models.IntegerField(blank=True,null=True)
    member_type = models.CharField(max_length=1,choices=MEMBER_TYPE_CHOICES,blank=True,null=True)
    is_e_board = models.BooleanField(default=False)
    cr2_cleared = models.BooleanField(default=False)
    availibility = models.ManyToManyField("ShowSlot",related_name="availibility",blank=True)
    preferred_shows = models.ManyToManyField("ShowSlot",related_name="preferred_shows",blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

class Clearance(models.Model):
    DJ = models.ForeignKey('DJ',on_delete=models.CASCADE)
    date = models.DateField()
    valid_until = models.DateField()
    
    def __str__(self):
        return self.DJ.__str__()+" "+str(self.date)+" "+str(self.valid_until)

class StationService(models.Model):
    DJ = models.ForeignKey('DJ', on_delete=models.CASCADE)
    year = models.IntegerField();
    hours = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.DJ.__str__()+" "+str(self.year)+"-"+str(self.hours)

class ShowSlot(models.Model):
    DAY_CHOICES = [
        ('M',"Monday"),
        ('T',"Tuesday"),
        ('W',"Wednesday"),
        ('R',"Thursday"),
        ('F',"Friday"),
        ('S',"Saturday"),
        ('U',"Sunday"),
    ]
    time_on = models.TimeField()
    time_off = models.TimeField()
    day_of_week = models.CharField(max_length=1,choices=DAY_CHOICES)
    
    def __str__(self):
        return self.day_of_week+" "+str(self.time_on)+"-"+str(self.time_off)