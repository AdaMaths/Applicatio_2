from django.shortcuts import render
from .utils import navier
from .utils import laser
from .utils import calc_utils
import numpy as np
from .forms import CSVUploadForm
from .utils import data_decision
from django.core.files.storage import default_storage

def navier_view(request):
    result = None
    if request.method == "POST":
        Re = float(request.POST.get("reynolds"))
        v0 = float(request.POST.get("vitesse"))
        result = navier.simulation(Re, v0)
    return render(request, "navier.html", {"result": result})



def laser_view(request):
    result = None
    if request.method == "POST":
        xmin = float(request.POST.get("xmin"))
        xmax = float(request.POST.get("xmax"))
        pas = float(request.POST.get("pas"))
        w0 = float(request.POST.get("w0"))
        longueur = float(request.POST.get("longueur"))
        pertes = float(request.POST.get("pertes"))
        x, y = laser.simulation_laser(xmin, xmax, pas, w0, longueur, pertes)
        result = {"x": x, "y": y}
    return render(request, "laser.html", {"result": result})




def calculs_view(request):
    result = None
    if request.method == "POST":
        calcul_type = request.POST.get("type")

        if calcul_type == "interpolation":
            x_points = list(map(float, request.POST.get("x_points").split(",")))
            y_points = list(map(float, request.POST.get("y_points").split(",")))
            x_eval = float(request.POST.get("x_eval"))
            y_interp = calc_utils.interpolation_lagrange(x_points, y_points, x_eval)
            result = f"Valeur interpolée : {y_interp:.4f}"

        elif calcul_type == "integration":
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            méthode = request.POST.get("methode")
            if méthode == "trapeze":
                integ = calc_utils.integration_trapeze(x, y)
            else:
                integ = calc_utils.integration_simpson(x, y)
            result = f"Valeur de l'intégrale : {integ:.4f}"

        elif calcul_type == "edo":
            f = lambda x, y: x + y
            x0 = 0
            y0 = 1
            h = 0.1
            n = 10
            y_final = calc_utils.euler_explicite(f, x0, y0, h, n)
            result = f"Résultat EDO (Euler explicite) : y({x0 + n * h}) = {y_final:.4f}"

    return render(request, "calculs.html", {"result": result})





def data_science_view(request):
    form = CSVUploadForm()
    stats, image_path = None, None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.cleaned_data['file']
            file_path = default_storage.save(f.name, f)
            full_path = "media/" + file_path
            stats, image_path = data_decision.analyse_csv(full_path)

    return render(request, "data_science.html", {
        "form": form,
        "stats": stats,
        "image_path": "/" + image_path if image_path else None
    })