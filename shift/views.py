from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shift.forms import ShiftModelForm
from shift.models import Shift


class ShiftListView(ListView):
    template_name = 'shift/shift_list.html'
    queryset = Shift.objects.all()


class ShiftDetailView(DetailView):
    template_name = 'shift/shift_detail.html'
    queryset = Shift.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Shift, id=id_)


class ShiftDeleteView(DeleteView):
    template_name = 'shift/shift_delete.html'
    queryset = Shift.objects.all()
    
    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Shift, id=id_)

    def get_success_url(self):
        return reverse('shift:shift-list')


class ShiftCreateView(CreateView):
    template_name = 'shift/shift_create.html'
    form_class = ShiftModelForm
    queryset = Shift.objects.all()

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class ShiftUpdateView(UpdateView):
    template_name = 'shift/shift_create.html'
    form_class = ShiftModelForm
    queryset = Shift.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Shift, id=id_)
