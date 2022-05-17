from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User


class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'avatar', 'sex')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        i = 0
        for field_name, field in self.fields.items():
            i += 1
            field.widget.attrs['class'] = f'input_control {i}'
            field.help_text = ''
            if field_name == 'name':
                field.widget.attrs['placeholder'] = field.label
                field.label = ''
            if field_name == 'email':
                field.widget.attrs['placeholder'] = field.label
                field.label = ''
            if field_name == 'password1':
                field.widget.attrs['placeholder'] = field.label
                field.label = ''
            if field_name == 'password2':
                field.widget.attrs['placeholder'] = field.label
                field.label = ''
            if field_name == 'sex':
                field.widget.attrs['type'] = 'ratio'
                field.label = ''
            if field_name == 'avatar':
                field.initial = 'user/ava.png'
                field.widget.attrs['placeholder'] = field.label
                field.label = ''


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





