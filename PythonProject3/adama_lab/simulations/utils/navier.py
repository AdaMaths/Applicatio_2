from django.shortcuts import render
from .utils import navier

def navier_view(request):
    result = None
    if request.method == "POST":
        Re = float(request.POST.get("reynolds"))
        v0 = float(request.POST.get("vitesse"))
        result = navier.simulation(Re, v0)
    return render(request, "navier.html", {"result": result})