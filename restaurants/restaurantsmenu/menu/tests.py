from django.test import TestCase
from .models import Item,Section,Modifiers


class SectionTestCase(TestCase):
    def setUp(self):
        Section.objects.create(name = "Dinner", description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")

    def test_item_info(self):
        qs = Section.objects.all()
        self.assertEqual(qs.count(),1)

class ItemTestCase(TestCase):
    def setUp(self):
        self.section=Section.objects.create(name = "Dinner", description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")
        Item.objects.create(section=self.section,name="pizza",description="Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough",price= "200")

    def test_item_info(self):
        qs = Item.objects.all()
        self.assertEqual(qs.count(),1)

        
        
class ModifiersTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name = "Dinner", description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")
        self.item = Item.objects.create(section=self.section,name="pizza",description="Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough",price= "200")
        self.modifiers = Modifiers.objects.create(name="extra spicy", description="NongShim Shin Ramyum Super Spicy Noodle Soup Korean style instant noodles are easy to make and ready in a couple of minutes. These noodles have a great taste", price="20")

    def test_item_info(self):
        self.modifiers.item.set([self.item.pk])
        qs = Modifiers.objects.all()
        self.assertEqual(qs.count(),1)
