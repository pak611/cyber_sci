
# importing the graph_input model into our form so we can start using it
from django import forms
from .models import Image_Axes
from .models import graph_input
from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    '''this is ModelForm taking in the metadata
    which says that all the fields of the form are going to be based on the model graph_input'''

    #edit_axis = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = graph_input
        fields = '__all__'
        #fields = ['x_min','x_max','y_min','y_max']

        # now lets import this model to our views and send it over to our template



class UploadImageForm(forms.ModelForm): 
  
    class Meta: 
        model = Image_Axes 
        fields = ['image', 'title', 'x_min', 'x_max', 'y_min', 'y_max']
        #fields = '__all__' 

        #def __init__(self, *args, **kwargs):
        #    super(UploadImageForm, self).__init__(*args, **kwargs)
        #    self.fields['title'].required = False


class ConvertImageForm(forms.ModelForm): 
  
    class Meta: 
        model = ConvertImage
        fields = ['filename'] 