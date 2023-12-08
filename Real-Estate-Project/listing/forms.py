# Assuming this is in forms.py or a file where your forms are defined
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'  # You can also specify the fields explicitly if needed

   
    widgets = {
        'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
    }
