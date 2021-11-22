from django.shortcuts import render


# Create your views here.
def index(request):
    # CountryTravel, CountryMed, CountryHot
    # to get multiple objects: array = {'CountryTravel': CountryTravel, 'CountryMed': CountryMed, ...}
    return render(request, 'index.html')  # , {'Country': Models})
