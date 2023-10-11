from django.forms import ModelForm
from .models import userModel
 
class UserForm(ModelForm):
    class Meta:
        model = userModel
        fields = '__all__'
        