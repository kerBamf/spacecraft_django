from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Manufacturer, Spacecraft

# Create your views here.

class Home(TemplateView):
    # def get(self, request):
    #     return HttpResponse("Spacecraft Home")
    template_name = "home.html"

class About(TemplateView):
    # def get(self, request):
    #     return HttpResponse("About Page")
    template_name = "about.html"

class ManufacturerList(TemplateView):
    template_name = "manufacturer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["manufacturers"] = Manufacturer.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["manufacturers"] = Manufacturer.objects.all()
            context["header"] = "Major Shipwrights"
        return context
    
class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = ['name', 'image', 'about', 'verified_manufacturer',]
    template_name = "manufacturer_create.html"
    success_url = "/shipwrights/"

class ManufacturerDetail(DetailView):
    model = Manufacturer
    template_name = "manufacturer_detail.html"

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = ['name', 'image', 'about', 'verified_manufacturer',]
    template_name = "manufacturer_update.html"
    success_url = "/shipwrights/"

class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = "manufacturer_delete_confirmation.html"
    success_url = '/shipwrights/'

class ShipList(TemplateView):
    template_name = "ship_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ships"] = Spacecraft.objects.all()
        return context
    
class SpacecraftCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        image = request.POST.get('image')
        manufacturer = Manufacturer.objects.get(pk=pk)
        Spacecraft.objects.create(name=name, image=image, manufacturer=manufacturer)
        return redirect ('manufacturer_detail', pk=pk)