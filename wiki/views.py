from allauth.account.views import RedirectAuthenticatedUserMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .models import PostModel, GroupModel, PhoneModel
from .forms import PostForm, GroupForm, PhoneForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class Phone:
    def get_phone(self):
        return GroupModel.objects.all()


class Desk:
    def get_desk(self):
        return PostModel.objects.filter(border=True, draft=True)


class Post:
    def get_post(self):
        return PostModel.objects.filter(border=False, draft=True)


class PostListView(LoginRequiredMixin, ListView, Phone, Post, Desk):
    queryset = PostModel.objects.filter(draft=True, border=False)[:3]
    # template_name = 'wiki/index.html'


class PostDetailView(LoginRequiredMixin, DetailView, Phone, Post):
    model = PostModel
    template_name = 'wiki/detail.html'
    slug_field = 'slug'


class PostCreateView(CreateView, Post, Phone):
    model = PostModel
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView, Phone, Post):
    model = PostModel
    form_class = PostForm


class PostDeleteView(DeleteView, Phone, Post):
    model = PostModel
    success_url = reverse_lazy('postmodel_list')


class GroupCreateView(CreateView, Post, Phone):
    model = GroupModel
    form_class = GroupForm
    template_name = 'wiki/postmodel_form.html'
    success_url = reverse_lazy('postmodel_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupEditView(UpdateView, Phone, Post):
    model = GroupModel
    form_class = GroupForm
    success_url = reverse_lazy('postmodel_list')
    template_name = 'wiki/postmodel_form.html'


class GroupDeleteView(DeleteView, Phone, Post):
    model = GroupModel
    success_url = reverse_lazy('postmodel_list')


class PhoneCreateView(CreateView, Post, Phone):
    model = PhoneModel
    form_class = PhoneForm
    template_name = 'wiki/postmodel_form.html'
    success_url = reverse_lazy('postmodel_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhoneEditView(UpdateView, Phone, Post):
    model = PhoneModel
    form_class = PhoneForm
    success_url = reverse_lazy('postmodel_list')
    template_name = 'wiki/postmodel_form.html'


class PhoneDeleteView(DeleteView, Phone, Post):
    model = PhoneModel
    success_url = reverse_lazy('postmodel_list')


class SearchView(ListView, Phone, Post, LoginRequiredMixin):

    # template_name = 'wiki/search.html'
    paginate_by = 3

    def get_queryset(self): # new
        query = self.request.GET.get('q', None)
        if query is not None:
            object_list = PostModel.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            return object_list
