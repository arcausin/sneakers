from multiprocessing import context

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .forms import QuestionForm

# Create your views here.

def create(request):
    context = {}

    form = QuestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/crud/')
    
    context['form'] = form
    return render(request, "crud/create.html", context)

def list_view(request):
    context = {}

    context['dataset'] = Question.objects.all()
    return render(request, "crud/index.html", context)

def detail_view(request, id):
    context = {}

    context["data"] = Question.objects.get(id = id)

    return render(request, "crud/detail.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Question, id = id)

    form = QuestionForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('/crud/')
    
    context["form"] = form

    return render(request, "crud/update.html", context)

def delete_view(request, id):
    context = {}

    context["data"] = Question.objects.get(id = id)

    obj = get_object_or_404(Question, id = id)

    if request.method == "POST":
        obj.delete()

        return redirect('/crud/')
    
    return render(request, "crud/delete.html", context)