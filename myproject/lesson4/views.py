import logging

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ClientForm, ItemForm
from .models import Client, Item

logger = logging.getLogger(__name__)

# Create your views here.

def client_form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Error'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email, phone=phone, address=address)
            client.save()
            logger.info(f'Получили: {form.cleaned_data=}')
            message = 'Client saved'
        else:
            form = ClientForm()
            message = 'Fill out form'
    return render(request, 'base_form.html', {'form': form, 'message': message})

def item_form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        message = 'Error'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            item = Item(name=name, description=description, price=price, quantity=quantity, image=image.name)
            item.save()
            logger.info(f'Получили: {name=}, {description=}, {price=}, {quantity=}.')
            message = 'Item saved'
    else:
        form = ItemForm()
        message = 'Fill out form'
    return render(request, 'base_form.html', {'form': form, 'message': message})
        
