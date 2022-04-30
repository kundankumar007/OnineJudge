from django.forms import ModelForm
from .models import solution

class solutionForm(ModelForm):
    class Meta:
        model = solution
        fields = '__all__'