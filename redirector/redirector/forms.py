from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ExtendedUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'