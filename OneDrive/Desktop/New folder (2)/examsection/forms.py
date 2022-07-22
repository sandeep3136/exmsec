from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import *
class RModelForm(ModelForm):


    class Meta:
        model = StaffDetails
        fields = ['branch', 'designation']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

class BModelForm(ModelForm):
    class Meta:
        model = RemunerationDetails
        fields = ['nature_of_work']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        


