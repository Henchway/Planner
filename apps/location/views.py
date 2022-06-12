from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import LocationModelForm
from .models import Location


class LocationListView(ListView):
    template_name = 'location/location_list.html'
    queryset = Location.objects.all()


class LocationDetailView(DetailView):
    template_name = 'location/location_detail.html'
    queryset = Location.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Location, id=id_)


class LocationDeleteView(DeleteView):
    template_name = 'location/location_delete.html'
    queryset = Location.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Location, id=id_)

    def get_success_url(self):
        return reverse('schedule:schedule-list')


class LocationCreateView(CreateView):
    template_name = 'location/location_create.html'
    form_class = LocationModelForm
    queryset = Location.objects.all()

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class LocationUpdateView(UpdateView):
    template_name = 'location/location_create.html'
    form_class = LocationModelForm
    queryset = Location.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Location, id=id_)
