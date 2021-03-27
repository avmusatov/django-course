from django.db.models import *


class Pet(Model):
    name = CharField(max_length=80)
    kind = CharField(max_length=80)
    age = CharField(max_length=10)
    description = TextField(max_length=4096)
    sex = CharField(max_length=10)
    sterilization = BooleanField()
    toilet = BooleanField()

    def __str__(self):
        return str(self.name)

class Leadership(Model):
    name = CharField(max_length=80)
    position = CharField(max_length=80)
    description = CharField(max_length=4096)

    def __str__(self):
        return str(self.name)

class Donation(Model):
    amount = PositiveIntegerField()
    message = CharField(max_length=4096)
    date = DateTimeField('donation date', auto_now_add=True)
    email = EmailField()
    contact_name = CharField(max_length=80)

    def __str__(self):
        return str(self.contact_name)