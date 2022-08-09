from django.test import TestCase
from .models import Item, Section, Modifiers
from rest_framework import status


class SectionTestCase(TestCase):
    def setUp(self):
        Section.objects.create(name="Dinner",
                                      description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")

    def test_item_info(self):
        qs = Section.objects.all()
        self.assertEqual(qs.count(), 1)


    def test_section_post(self):
        data = {"title": "Chicken",
                "description": "topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high"}
        response = self.client.post("/api/section/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Section.objects.count(), 2)

    def test_section_get(self):
        response = self.client.get("/api/section/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        response = self.client.get('/api/section/1/')
        self.assertEqual(response.data, {'id': 1, "title": "Dinner",
                                         "description": "topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high"})

    def test_section_update(self):
        data = {"id":1,"title": "Chicken1","description": "topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high"}
        response = self.client.put("/api/section/1/", data,format="multipart",content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_section_delete(self):
        response = self.client.delete("/api/section/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class ItemTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name="Dinner",
                                              description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")
        self.item = Item.objects.create(section=self.section, name="pizza",
                            description="Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough",
                            price="200")

    def test_item_info(self):
        qs = Item.objects.all()
        self.assertEqual(qs.count(), 1)





class ModifiersTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name="Dinner",
                                              description="topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high")
        self.item = Item.objects.create(section=self.section, name="pizza",
                                        description="Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough",
                                        price="200")
        self.modifiers = Modifiers.objects.create(name="extra spicy",
                                                  description="NongShim Shin Ramyum Super Spicy Noodle Soup Korean style instant noodles are easy to make and ready in a couple of minutes. These noodles have a great taste",
                                                  price="20")

    def test_item_info(self):
        self.modifiers.item.set([self.item.pk])
        qs = Modifiers.objects.all()
        self.assertEqual(qs.count(), 1)

