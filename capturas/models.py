from django.db import models


class Captura(models.Model):
    code = models.CharField(max_length=15)
    code_user = models.CharField(max_length=15)
    active = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=5)
    cpf = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=15)

    def __str__(self):
        return self.code


