from django.db import models

from user.models import Account

class Place(models.Model):
    CATEGORIES_CHOISES = [
        ('coffeeshop', 'Кофейня'),
        ('bar', 'Бар'),
        ('restaurant', 'Ресторан'),
        ('museum', 'Музей'),
        ('landmark', 'Достопримечательность')
    ]

    category = models.CharField(max_length=10, choices=CATEGORIES_CHOISES)
    name = models.CharField(max_length=30)
    description = models.TextField()
    metrostation = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    MARKS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    mark = models.SmallIntegerField(choices=MARKS)

    def __str__(self):
        return self.username, self.place

class LikedTrip(models.Model):

    title = models.CharField(max_length=30)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.title



