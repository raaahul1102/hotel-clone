from accounts.models import Hotel, HotelVendor, Ameneties
from accounts.templates.utils.sendEmail import generate_slug

from faker import Faker
import random

fake = Faker()

def generate_fake_hotel(total_hotels = 100):
    hotels = []
    for _ in range(total_hotels):
        hotel_name = fake.company() + " Hotel"
        hotel_description = fake.text(max_nb_chars=200)
        hotel_price = round(random.uniform(1000, 5000), 2)  # e.g. ₹1000–₹5000
        hotel_offer_price = round(hotel_price * random.uniform(0.6, 0.9), 2)  # 10–40% off
        hotel_location = fake.address().replace("\n", ", ")
        amenity_ids = random.sample(range(8, 14), random.randint(4, 6))

        hotel_vendor = HotelVendor.objects.get(id = 16)
        hotel_obj = Hotel.objects.create(
            hotel_name = hotel_name,
            hotel_description = hotel_description,
            hotel_slug = generate_slug(hotel_name),
            hotel_owner = hotel_vendor,
            hotel_price = hotel_price,
            hotel_offer_price = hotel_offer_price,
            hotel_location = hotel_location,
        )

        for id in amenity_ids:
            amenity = Ameneties.objects.get(id = id)
            hotel_obj.ameneties.add(amenity)
            hotel_obj.save()

        hotels.append(hotel_obj)
    Hotel.objects.bulk_create(hotels)