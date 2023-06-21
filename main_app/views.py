from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    # def get(self, request):
    #     return HttpResponse("Spacecraft Home")
    template_name = "home.html"

class About(TemplateView):
    # def get(self, request):
    #     return HttpResponse("About Page")
    template_name = "about.html"

class Manufacturer:
    def __init__(self, name, image, about):
        self.name = name
        self.image = image
        self.about = about

manufacturers = [
    Manufacturer("Corellian Engineering Corporation", "https://static.wikia.nocookie.net/starwars/images/6/62/Corellian_Engineering_Corporation.svg/revision/latest?cb=20080312040228", "Corellian Engineering Corporation, abbreviated CEC and originally called Corellian Engineering Corps, was one of the three largest starship manufacturers. This corporation was widely considered the most prolific starship manufacturer in the galaxy." ),
    
    Manufacturer("Incom Corporation", "https://static.wikia.nocookie.net/starwars/images/9/92/Incom.svg/revision/latest/scale-to-width-down/999?cb=20230617031313", "The Incom Corporation, formerly known as Torranix Inertial Compensator Corporation,[3] and also referred to as Incom Industries, or more commonly Incom for short, was a Fresia-based corporation known for designing and manufacturing robust, progressively-minded starfighters, airspeeders, and transports. They were renowned for their production of the T-65 X-wing starfighter, which became their logo and, most famously, a key tool and symbol of the Alliance to Restore the Republic during the Galactic Civil War."),

    Manufacturer("Kuat Drive Yards", "https://static.wikia.nocookie.net/starwars/images/0/0d/KDY.svg/revision/latest?cb=20080305080702", "Kuat Drive Yards (KDY) was a starship manufacturer based on the planet Kuat. The main production facility of Kuat Drive Yards was the Kuat Drive Yards Orbital Shipyards, a ring around the planet Kuat. It produced many of the galaxy's most terrifying symbols of Imperial might, including the Imperial-class Star Destroyer, and also produced walkers such as the All Terrain Defense Pod. It had several subsidiaries, with Kuat Vehicles focusing on civilian ground products and Kuat Systems Engineering producing starfighters."),

    Manufacturer("Sienar Fleet Systems", "https://static.wikia.nocookie.net/starwars/images/3/39/Sienar.svg/revision/latest?cb=20080311192948", "Sienar Fleet Systems or SFS (owned by the massive company Santhe/Sienar Technologies) was a major starship manufacturer. Through their Sienar Design Systems subsidiary, they were also responsible for many drive and power systems.")
]

class ManufacturerList(TemplateView):
    template_name = "manufacturer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manufacturers"] = manufacturers
        return context

class Ship:
    def __init__(self, name, image, manufacturer):
        self.name = name
        self.image = image
        self.manufacturer = manufacturer

ships = [
    Ship("X-Wing", "https://static.wikia.nocookie.net/starwars/images/0/00/Xwing-ROOCE.png/revision/latest/scale-to-width-down/1000?cb=20230516042654", "Incom Corporation"),
    Ship("Millenium Falcon", "https://static.wikia.nocookie.net/starwars/images/5/52/Millennium_Falcon_Fathead_TROS.png/revision/latest/scale-to-width-down/1000?cb=20221029015218", "Corellian Engineering Corporation"),
    Ship("A-Wing", "https://static.wikia.nocookie.net/starwars/images/1/13/RZ1-BF2.png/revision/latest/scale-to-width-down/1000?cb=20171005230121", "Kuat Drive Yards"),
    Ship("TIE-Interceptor", "https://static.wikia.nocookie.net/starwars/images/f/f5/TIE_Interceptor_BF.png/revision/latest/scale-to-width-down/1000?cb=20170501054325", "Sienar Fleet Systems"),
]

class ShipList(TemplateView):
    template_name = "ship_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ships"] = ships
        return context