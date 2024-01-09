from django.forms import ModelForm
from .models import TaskDetails
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model=TaskDetails
        fields='__all__'
        exclude=['completed_at']
        widgets={
            'taskname':forms.Textarea(attrs={'class':'form-control'}),
            'phases':forms.Select(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}), 
        }
        
class CreateTaskForm(ModelForm):
    class Meta:
        model=TaskDetails
        fields='__all__'
        exclude=['completed_at']
        widgets={
            'taskname':forms.Textarea(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}), 
            
        }
        