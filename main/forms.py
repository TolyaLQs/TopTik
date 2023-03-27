from django.forms.models import ModelForm
from .models import PostLike


class AddLikePost(ModelForm):

    class Meta(ModelForm):
        model = PostLike
        fields = ('user', 'post')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = ''

