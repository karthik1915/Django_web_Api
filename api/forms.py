from django import forms
from django.forms import ModelForm
from .models import ImagesModel

class UploadImage(ModelForm):
    image_url  = forms.URLInput()
    title = forms.TextInput()
    description = forms.TextInput()
    category = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('anime', 'Anime'),
            ('option2', 'Marvel'),
        ]
    )
    is_safe = forms.CheckboxInput(check_test="true")
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'required': False}),
        label="tags",
        help_text='seperate tags with comma * \' * '
    )
    class Meta:
        model = ImagesModel
        fields = ['image_url','title','description','category','is_safe','tags']