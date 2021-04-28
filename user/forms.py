from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'avatar', 'sex')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
            field.help_text = ''


class ChangeUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'name', 'sex', 'about_user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ChangeUserAvatarForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field == 'avatar':
                field = '/user/ava.png'

