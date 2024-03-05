from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    print(Rating.objects.get_or_create(
        restaurant = restaurant,
        user = user,
        rating = 4
    ))
    #this will return 2 things , 1st is rating object , 2nd is True(if object is creted) or false(of object is fetched)
    # so you can write it as 

    rating,creted =  Rating.objects.get_or_create(
        restaurant = restaurant,
        user = user,
        rating = 4
    )

    # this create will bive bool and can be used as if statement
    pprint(connection.queries)

        # restaurant = Restaurant.objects.first()
        # print(restaurant.sales.all())       #sales is the related_name here






    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 2.3,
    #     datetime =  timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 4.3,
    #     datetime =  timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 5.3,
    #     datetime =  timezone.now()
    # )
    
    # restaurant = Restaurant.objects.first()
    # print(restaurant)
    # print(connection.queries)



    # restaurant = Restaurant()
    # restaurant.name = 'My Indian restaurant'
    # restaurant.latitude = 50.2
    # restaurant.longitude = 50.3
    # restaurant.date_opened =  timezone.now()
    # restaurant.restaurant_types = Restaurant.TypeChoice.INDIAN

    # restaurant.save()
    # print('hello')