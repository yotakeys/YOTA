from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from confession.models import Confession

# Create your views here.


class ConfessionList(LoginRequiredMixin, ListView):
    model = Confession
    login_url = 'login'
    template_name = 'confession/confession_list.html'
    context_object_name = "confessions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confessions'] = context['confessions'].filter(
            user=self.request.user)
        context['count'] = context['confessions'].count()

        return context


class ConfessionUrl(UpdateView):
    template_name = 'confession/confession.html'
    model = Confession
    fields = ['answer', 'response']
    context_object_name = "confession"

    def get_success_url(self):
        return reverse_lazy('confessionUrl', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.answer_date = datetime.now()
        form.instance.is_answerred = True
        return super().form_valid(form)


class CreateConfession(LoginRequiredMixin, CreateView):
    model = Confession
    fields = ['slug', 'sender', 'target', 'title', 'message']
    success_url = reverse_lazy('confessionList')
    template_name = 'confession/confession_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateConfession, self).form_valid(form)


class DeleteConfession(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Confession
    context_object_name = 'confession'
    success_url = reverse_lazy('confessionList')
    template_name = 'confession/confession_delete.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)  # noqa: E501


class UpdateConfession(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ListView):
    model = Confession
    fields = ['message']
    template_name = "confession/confession_update.html"
    success_url = reverse_lazy('confessionList')
    context_object_name = "confession"

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)  # noqa: E501
