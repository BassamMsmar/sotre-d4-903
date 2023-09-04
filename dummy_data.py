import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random

from product.models import Brand, Product



def seed_brand(n):
    fake = Faker()
    images = ['1.png', '4.png','5.png','6.png','7.png']

    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(0,4)]}'
        )
    print(f'Seed {n} Brand Successfully')


def seed_product(n):
    fake = Faker()
    images = ['1.png', '4.png','5.png','6.png','7.png']
    flags = ['New','Sale','Feature']

    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(0,4)]}',
            price = round(random.uniform(20.99, 99.99), 2),
            sku = random.randint(1000, 100000),
            subtitle = fake.text(max_nb_chars=100),
            description = fake.text(max_nb_chars=2000),
            quantity = random.randint(1, 24),
            flag = flags[random.randint(0,2)],
            brand = Brand.objects.get(id=random.randint(5,100))



        )
    print(f'Seed  {n} Product Successfully')



def create_fake_date():
    answer = input('If you want create 150 brand and 2000 products press "y" or any kay to exit :  ')
    if answer == 'y':
        seed_brand(150)
        seed_product(2000)
    else :
        print('Exit....')


create_fake_date()
            