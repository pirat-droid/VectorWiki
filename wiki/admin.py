from django import forms
from django.contrib import admin
from .models import PostModel, GroupModel, PhoneModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = PostModel
        fields = '__all__'

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_create', 'date_update')
    list_filter = ('user', 'date_create', 'date_update')
    search_fields = ('user', 'date_create', 'date_update')
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm


@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date_create', 'date_update')
    list_filter = ('user', 'date_create', 'date_update')
    search_fields = ('user', 'date_create', 'date_update')


@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'user', 'date_create', 'date_update')
    list_filter = ('user', 'date_create', 'date_update')
    search_fields = ('user', 'date_create', 'date_update')

# Register your models here.
