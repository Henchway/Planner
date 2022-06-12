from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.day.forms import DayModelForm
from apps.day.models import Day


class DayListView(ListView):
    template_name = 'day/day_list.html'
    queryset = Day.objects.all()


class DayDetailView(DetailView):
    template_name = 'day/day_detail.html'
    queryset = Day.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Day, id=id_)


class DayDeleteView(DeleteView):
    template_name = 'day/day_delete.html'
    queryset = Day.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Day, id=id_)

    def get_success_url(self):
        return reverse('schedule:schedule-list')


class DayCreateView(CreateView):
    template_name = 'day/day_create.html'
    form_class = DayModelForm
    queryset = Day.objects.all()

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class DayUpdateView(UpdateView):
    template_name = 'day/day_create.html'
    form_class = DayModelForm
    queryset = Day.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Day, id=id_)
