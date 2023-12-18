from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('email','password1','password2')
        model = CustomUser

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].label = "Email Address"

