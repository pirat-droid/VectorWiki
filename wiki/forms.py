from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import PostModel, GroupModel, PhoneModel

class PostForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = PostModel
        fields = ['title', 'img', 'description', 'border']


class GroupForm(forms.ModelForm):

    class Meta:
        model = GroupModel
        fields = ['name', ]

class PhoneForm(forms.ModelForm):

    class Meta:
        model = PhoneModel
        exclude = ['date_create', 'date_update', 'user']

