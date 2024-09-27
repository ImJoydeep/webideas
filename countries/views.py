from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, City
from .forms import CountryForm, CityForm

def toggle_country_status(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if country.status == 'A':
        country.status = 'I'
    elif country.status == 'I':
        country.status = 'A'
    country.save()
    return redirect('country_list')

def toggle_city_status(request, pk):
    city = get_object_or_404(City, pk=pk)
    if city.status == 'A':
        city.status = 'I'
    elif city.status == 'I':
        city.status = 'A'
    else:
        city.status = 'A'
    city.save()
    return redirect('country_detail', pk=city.country.pk)

def country_list(request):
    countries = Country.objects.exclude(country_archive=True)
    return render(request, 'index.html', {'countries': countries})

def archived_country_list(request):
    archived_countries = Country.objects.filter(country_archive=True)
    return render(request, 'archived_country_list.html', {'archived_countries': archived_countries})


def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm()
    return render(request, 'country_form.html', {'form': form})

def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'country_form.html', {'form': form})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    return redirect('country_list')

def country_archive(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.country_archive = True
    country.save()
    return redirect('country_list')

def country_restore_archive(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.country_archive = False
    country.save()
    return redirect('archived_countries')

def city_create(request):
    countries = Country.objects.filter(status='A')
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return redirect('country_detail',pk=city.country.pk)
    else:
        form = CityForm()
    
    context = {
        'form': form,
        'countries': countries
    }
    return render(request, 'city_form.html', context)

def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('country_detail',pk=city.country.pk)
    else:
        form = CityForm(instance=city)
    
    return render(request, 'city_form.html', {'form': form, 'city': city}) 

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('country_detail', pk=city.country.pk)


# Archive a city
def city_archive(request, pk):
    city = get_object_or_404(City, pk=pk)
    if not city.city_archive:
        city.city_archive = True
        city.save()
    return redirect('country_detail',pk=city.country.pk)

def city_restore_archive(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.city_archive = False
    city.save()
    return redirect('country_detail', pk=city.country.pk)



def country_detail(request, pk):
    # Retrieve the country by primary key (pk)
    country = get_object_or_404(Country, pk=pk)
    archived_cities = City.objects.filter(country=country,city_archive=True)
    cities = country.cities.filter(city_archive=False)
    context = {
        'country': country,
        'cities': cities,
        'archived_cities': archived_cities,
    }
    return render(request, 'country_detail.html', context)