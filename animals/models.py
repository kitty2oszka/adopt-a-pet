from django.db import models

class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('dog', 'Pies'),
        ('cat', 'Kot'),
        ('other', 'Inne'),
    ]

    name = models.CharField(max_length=70)
    species = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    breed = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    is_adopted = models.BooleanField(default=False)


    def __str__(self):
        return self.name