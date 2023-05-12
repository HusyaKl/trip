# Generated by Django 4.1.7 on 2023-05-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendation', '0003_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('coffee_shop', 'Кофейня'), ('bar', 'Бар'), ('restaurant', 'Ресторан'), ('museum', 'Музей'), ('landmark', 'Достопримечательность'), ('park', 'Парк'), ('gallery', 'Галерея')], max_length=20),
        ),
    ]
