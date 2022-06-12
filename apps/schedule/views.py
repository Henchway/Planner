from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.schedule.forms import ScheduleModelForm
from apps.schedule.models import Schedule


class ScheduleListView(ListView):
    template_name = 'schedule/schedule_list.html'
    queryset = Schedule.objects.all()


class ScheduleDetailView(DetailView):
    template_name = 'schedule/schedule_detail.html'
    queryset = Schedule.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Schedule, id=id_)


class ScheduleDeleteView(DeleteView):
    template_name = 'schedule/schedule_delete.html'
    queryset = Schedule.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Schedule, id=id_)

    def get_success_url(self):
        return reverse('schedule:schedule-list')


class ScheduleCreateView(CreateView):
    template_name = 'schedule/schedule_create.html'
    form_class = ScheduleModelForm
    queryset = Schedule.objects.all()

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class ScheduleUpdateView(UpdateView):
    template_name = 'schedule/schedule_create.html'
    form_class = ScheduleModelForm
    queryset = Schedule.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Schedule, id=id_)
