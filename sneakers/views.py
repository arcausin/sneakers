from multiprocessing import context

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Produit
from .forms import ProduitForm

# Create your views here.

def create(request):
    context = {}

    form = ProduitForm(request.POST or None)

    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/sneakers/')
    
    else:
        form = ProduitForm()
    
    context['form'] = form
    return render(request, "sneakers/create.html", context)

def list_view(request):
    context = {}

    context['dataset'] = Produit.objects.all()
    return render(request, "sneakers/index.html", context)

def detail_view(request, id):
    context = {}

    context["data"] = Produit.objects.get(id = id)

    return render(request, "sneakers/detail.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Produit, id = id)

    form = ProduitForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('/sneakers/')
    
    context["form"] = form

    return render(request, "sneakers/update.html", context)

def delete_view(request, id):
    context = {}

    context["data"] = Produit.objects.get(id = id)

    obj = get_object_or_404(Produit, id = id)

    if request.method == "POST":
        obj.delete()

        return redirect('/sneakers/')
    
    return render(request, "sneakers/delete.html", context)