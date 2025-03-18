#Cargar los elementos necesarios para utilizar los modulos de django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mandarinstore.settings')
import django
django.setup()

#Script para poblar la tabla Contact
from faker import Faker
import random
from storeApp.models import Contact

fake_generator = Faker()

def populate_contacts(n_contacts=5):
    for i in range(n_contacts):
        fake_name = fake_generator.name()
        fake_address = fake_generator.address()
        fake_phone = random.uniform(1000000000,9999999999)
        fake_email = fake_generator.email()
        fake_active = random.random() > 0.5

        contact = Contact.objects.get_or_create(
            full_name = fake_name,
            address = fake_address,
            phone = fake_phone,
            email = fake_email,
            active = fake_active
        )

if __name__ == '__main__':
    print('Empezar a poblar la base de datos.')
    populate_contacts(30)
    print('Finalizado.')