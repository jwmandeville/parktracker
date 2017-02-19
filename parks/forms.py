from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('favorite_park',)

class ProblemForm(forms.Form):
    description = forms.CharField(max_length=150)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
