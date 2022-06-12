from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import StaffModelForm, StaffDaysOffForm
from .models import Staff


class StaffListView(ListView):
    template_name = 'staff/staff_list.html'
    queryset = Staff.objects.all()


class StaffDetailView(DetailView):
    template_name = 'staff/staff_detail.html'
    queryset = Staff.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Staff, id=id_)


class StaffDeleteView(DeleteView):
    template_name = 'staff/staff_delete.html'
    queryset = Staff.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Staff, id=id_)

    def get_success_url(self):
        return reverse('staff:staff-list')


class StaffCreateView(CreateView):
    template_name = 'staff/staff_create.html'
    form_class = StaffModelForm
    queryset = Staff.objects.all()
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class StaffUpdateView(UpdateView):
    template_name = 'staff/staff_create.html'
    form_class = StaffModelForm
    queryset = Staff.objects.all()

    # override to make it work with "id" instead of "pk"
    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Staff, id=id_)


class StaffDaysOffView(UpdateView):
    template_name = 'staff/staff_days_off.html'
    form_class = StaffDaysOffForm
    queryset = Staff.objects.all()

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Staff, id=id_)

#
# def staff_create_view(request):
#     form = StaffForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = StaffForm()  # re-render to clear out the data
#
#     context = {'form': form}
#     return render(request, "staff/staff_create.html", context)
#
#
# def staff_detail_view(request, id):
#     obj = get_object_or_404(Staff, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "staff/staff_detail.html", context)
#
#
# def staff_update_view(request, id):
#     obj = get_object_or_404(Staff, id=id)
#     form = StaffForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form
#     }
#     return render(request, "staff/staff_create.html", context)
#
#
# def staff_delete_view(request, id):
#     obj = get_object_or_404(Staff, id=id)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('../../')
#     context = {
#         "object": obj
#     }
#     return render(request, "staff/staff_delete.html", context)
#
#
# def staff_list_view(request):
#     queryset = Staff.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "staff/staff_list.html", context)
#
