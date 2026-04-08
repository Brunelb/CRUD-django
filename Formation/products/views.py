from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Products
from .forms import ProductForm , RowProductForm


# Create your views here.
def product_list(request, *args, **kwargs):
    product = Products.objects.all()
    context = {
        'products':product
    }
    return render(request, 'products/detail.html',context)

# def product_create(request):
#     form = ProductForm(request.POST or None)
#     message = ""
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#         message = "Bien reçu"
#     return render(request, 'products/create.html', {'form': form, 'message': message })

# def product_update(request,my_id):
#     try:
#         obj = Products.objects.get(id=my_id)
#     except Products.DoesNotExist:
#         return render (request,'products/error404.html')
#     form = ProductForm(request.POST or None, instance=obj)
#     message = ""
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#         message = "modification Bien reçu"
#     return render(request, 'products/update.html', {'form': form, 'message': message })

def product_update(request, my_id):
    try:
        obj = Products.objects.get(id=my_id)
    except Products.DoesNotExist:
        return render(request, 'products/error404.html')

    form = ProductForm(request.POST or None, instance=obj)
    message = ""

    if form.is_valid():
        form.save()
        message = "Modification bien reçue"

    return render(request, 'products/update.html', {
        'form': form,
        'message': message,
        'obj': obj
    })


def product_create(request):
    form = RowProductForm()
    message = ""
    if request.method == "POST":
        form = RowProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Products.objects.create(**form.cleaned_data)
            new.save()
            form = RowProductForm()
            message = "Bien reçu"
    return render(request, 'products/create.html',{'form':form,'message': message })


def product_table(request):
    obj=Products.objects.all()
    return render(request, 'products/table.html', {'obj':obj})

def product_delete(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    name = obj.name
    if request.method == "POST":
        obj.delete()
        return redirect ('product_table')
    return render(request,'products/delete.html',{'name':name})