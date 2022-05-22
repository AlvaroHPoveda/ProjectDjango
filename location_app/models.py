from django.db import models
import uuid
from catalog_app.models import Category
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    @property
    def title_author(self):
        return f"{self.title} | {self.author}"

class Rack(models.Model):
    number = models.IntegerField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    location = models.ForeignKey(Book, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location} | {self.number}"

    @property
    def title_uuid(self) -> dict:
        return {
            "number": self.number,
            "uuid": self.uuid
        }

class RackItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.id} | {self.category.cover} | {self.category.owner.email}"

@receiver(post_save, sender=RackItem)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        rack_item = instance
        rack_id = rack_item.rack.id
        rack = Rack.objects.get(pk=rack_id)
        rack.available = False
        rack.save()

@receiver(post_delete, sender=RackItem)
def update_status_rack(sender, instance,**kwargs):  
    rack_item = instance
    rack_id = rack_item.rack.id
    rack = Rack.objects.get(pk=rack_id)
    rack.available = True
    rack.save()