from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
    from .forms import CustomForm

    form = CustomForm(request.POST)
    context = {"form": form}
    return render(request, "md/home.html", context)
