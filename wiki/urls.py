from django.urls import path
from . import views

urlpatterns = [
     path('', views.PostListView.as_view(), name='postmodel_list'),
     path('post/<slug:slug>', views.PostDetailView.as_view(), name='postmodel_detail'),
     path('post-update/<slug:slug>', views.PostEditView.as_view(), name='postmodel_update'),
     path('post-create/', views.PostCreateView.as_view(), name='postmodel_create'),
     path('post-delete/<slug:slug>', views.PostDeleteView.as_view(), name='postmodel_delete'),
     path('group-create/', views.GroupCreateView.as_view(), name='groupmodel_create'),
     path('group-update/<int:pk>', views.GroupEditView.as_view(), name='groupmodel_update'),
     path('group-delete/<int:pk>', views.GroupDeleteView.as_view(), name='groupmodel_delete'),
     path('phone-create/', views.PhoneCreateView.as_view(), name='phonemodel_create'),
     path('phone-update/<int:pk>', views.PhoneEditView.as_view(), name='phonemodel_update'),
     path('phone-delete/<int:pk>', views.PhoneDeleteView.as_view(), name='phonemodel_delete'),
     path("search/", views.SearchView.as_view(), name='search'),
]
