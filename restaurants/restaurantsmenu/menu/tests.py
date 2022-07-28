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
