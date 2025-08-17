from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.breed})"


class Owner(models.Model):
    name = models.CharField(max_length=100)
    dogs = models.ManyToManyField(Dog, related_name="owners")

    def __str__(self):
        return self.name


class Walker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Walk(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.dog.name} walked by {self.walker.name} on {self.date_time}"

