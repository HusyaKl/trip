from django.db import models

from user.models import Account

class Place(models.Model):
    CATEGORIES_CHOISES = [
        ('coffee_shop', 'Кофейня'),
        ('bar', 'Бар'),
        ('restaurant', 'Ресторан'),
        ('museum', 'Музей'),
        ('landmark', 'Достопримечательность'),
        ('park', 'Парк'),
        ('gallery', 'Галерея')
    ]

    category = models.CharField(max_length=20, choices=CATEGORIES_CHOISES)
    name = models.CharField(max_length=30)
    description = models.TextField()
    metrostation = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=50)
    url = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Mark(models.Model):
    MARKS = [
          (1, '1'),
          (2, '2'),
          (3, '3'),
          (4, '4'),
          (5, '5')
      ]
  
    username = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    mark = models.SmallIntegerField(choices=MARKS)
    category = models.CharField(max_length=100, default='')

class Review(models.Model):
    MARKS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100, default='')
    place = models.CharField(max_length=100, default='')
    mark = models.SmallIntegerField(choices=MARKS)
    body = models.TextField(default='')

    def __str__(self):
        return self.username, self.place

class LikedTrip(models.Model):

    title = models.CharField(max_length=30)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.title



