from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "my_test": "This is about us",
        "my_number": 1234,
        "my_list": [123,123,123]
    }
    #    return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", my_context)
