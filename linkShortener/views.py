from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from .models import Url
# Create your views here.


class UrlList(LoginRequiredMixin, ListView):
    model = Url
    template_name = 'linkShortener/url_list.html'
    context_object_name = 'urls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = context['urls'].filter(user=self.request.user)
        context['count'] = context['urls'].count()

        search = self.request.GET.get('search')
        if search:
            context['urls'] = context['urls'].filter(
                shortUrl__icontains=search)
        context['search_value'] = search
        return context


def redirectUrl(request, shortUrl):
    newLink = get_object_or_404(Url, pk=shortUrl).longUrl
    return redirect(newLink)


class UpdateUrl(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ListView):
    model = Url
    fields = ['longUrl']
    template_name = "linkShortener/url_update.html"
    success_url = reverse_lazy('url')
    context_object_name = "urls"

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)  # noqa: E501


class DeleteUrl(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Url
    context_object_name = 'url'
    success_url = reverse_lazy('url')
    template_name = 'linkShortener/url_delete.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)  # noqa: E501


class CreateUrl(LoginRequiredMixin, CreateView):
    model = Url
    fields = ['longUrl', 'shortUrl']
    success_url = reverse_lazy('url')
    template_name = 'linkShortener/url_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateUrl, self).form_valid(form)
