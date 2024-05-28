import datetime
from django import forms

from app.models import *


# As Topic form object method assoicated with forms we use clean() and clean_element() in forms.py

class TopicForm(forms.ModelForm): # need to create object method inside main class and outside sub class
    class Meta:
        model = Topic
        fields = '__all__'
    
    

class WebpageForm(forms.ModelForm):
    botcatcher = forms.CharField(max_length=10)
    class Meta:
        model = Webpage
        fields = '__all__' 
    def clean(self):
        email = self.cleaned_data['email']
    
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Entered emails not matching') 
        
    def clean_url(self):
        url = self.cleaned_data['url']
    
        if not url.endswith('.in'):
            raise forms.ValidationError('Entered emails not matching') 
    
        

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'

    def clean_date(self):
        date=self.cleaned_data['date']
        if  date > datetime.date.today():
            raise forms.ValidationError("date should be in the past!")