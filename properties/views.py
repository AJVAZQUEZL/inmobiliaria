from django.shortcuts import render, get_object_or_404, redirect
from .forms import PropertyForm
from .models import Property

def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('property_list')
    else:
        form = PropertyForm()
    properties = Property.objects.all()
    context = {
        "properties": properties,
        "form": form
    }
    return render(request, "properties/property_list.html", context=context)

def update_property(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    context = {
        "form": form
    }
    return render(request, "properties/property_form.html", context=context)

def delete_property(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == "POST":
        property.delete()
        return redirect('property_list')
    return render(request, "properties/property_confirm_delete.html", {"property": property})

