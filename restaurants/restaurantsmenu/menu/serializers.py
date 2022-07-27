from .models import Section,Item,Modifiers
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class SectionSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='name')

    class Meta:
        model = Section
        fields = ['id','title','description']


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def validate(self,data):
        item = Item.objects.values_list('name', flat=True)
        if data['name'] in item:
            raise serializers.ValidationError("Item is already exists")
        return data




class ModifiersSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='name')

    class Meta:
        model = Modifiers
        fields = ['id','title','description','price','item']


class ItemSerializers1(WritableNestedModelSerializer):
    modifiers = ModifiersSerializers(many=True,)
    title = serializers.CharField(source='name')

    class Meta:
        model = Item
        fields = ['id','title',"description",'price','modifiers']



class SectionSerializer1(serializers.ModelSerializer):
    items = ItemSerializers1(many=True, read_only=True)
    title = serializers.CharField(source='name')

    class Meta:
        model = Section
        fields = ['id','title',"description",'items']

