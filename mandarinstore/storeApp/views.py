from django.shortcuts import render
from django.http import HttpResponse
from storeApp.models import Product, Contact

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        'user' : 'Brandon',
        'message' : 'Largo de aqui!',
        'special_offers' : special_offers,
        'product_list' : product_list,
        'special_offers_2' : [
            {
                'name' : 'Mascarilla hidratante de sábila',
                'cost' : 14.00,
                'image' : 'storeApp/img/mascarilla.png'
            },
            {
                'name' : 'Consola de videojuegos portátil XE150',
                'cost' : 450.00,
                'image' : 'storeApp/img/consola.png'
            },
            {
                'name' : 'Reloj de pulsera gótico de Snoopy',
                'cost' : 160.00,
                'image' : 'storeApp/img/reloj.png'
            },
            {
                'name' : 'Camisa para caballero de algodón',
                'cost' : 200.00,
                'image' : 'storeApp/img/camisa.png'
            },
            {
                'name' : 'Peluche de Batman tamaño real',
                'cost' : 150.00,
                'image' : 'storeApp/img/peluche.png'
            },
        ],
        'products' : [
            'Mascarilla hidratante de sábila',
            'Consola de videojuegos portátil XE150',
            'Reloj de pulsera gótico de Snoopy',
            'Camisa para caballero de algodón',
            'Peluche de Batman tamaño real',
        ],
    }
    return render(request, 'storeApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django!")

def about(request):
    contacts = Contact.objects.filter(active=True)
    my_context = {
        'contacts' : contacts
    }
    return render(request, 'storeApp/about.html', context=my_context)