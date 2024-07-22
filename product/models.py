from django.db import models


class Turi(models.Model):
    turi = models.CharField()

    def __str__(self):
        return self.turi


class Fruit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField()
    foydalari = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Vegetables(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField()
    foydalari = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bread(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField()
    foydalari = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Meat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField()
    foydalari = models.CharField(max_length=200)

    def __str__(self):
        return self.name

