from django import forms
from django.db import models
from django.core import validators



# Create Normal functions and Built in validators in models.py file -->validating field beacause models not associated with forms we cannot use  clean and clean_element here 

#normal Functions
def validate_for_z(value):
    if value[0]=='z':
        raise forms.ValidationError('started with a')
    
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validate_for_z])
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])

    def __str__(self):
        return self.author