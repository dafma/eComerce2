from django.shortcuts import render, Http404
from .models import Question


# Create your views here.
from .forms import UserResponseForm

def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        queryset = Question.objects.all()
        instance = queryset[0]
        context = {
            "form":form,
            "instance":instance,
            #"queryset": queryset,
        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404