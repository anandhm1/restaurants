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

    def to_representation(self, instance):
        rep = super(ItemSerializers, self).to_representation(instance)
        rep['section'] = instance.section.name
        return rep

    def validate(self,data):
        item = Item.objects.values_list('name', flat=True)
        if data['name'] in item:
            raise serializers.ValidationError("Item is already exists")
        return data




class ModifiersSerializers(serializers.ModelSerializer):
    item = serializers.StringRelatedField(many=True, read_only=True)
    title = serializers.CharField(source='name')

    class Meta:
        model = Modifiers
        fields = ['id','title','description','price','item']




class ModifiersSerializers1(serializers.ModelSerializer):
    title = serializers.CharField(source='name')

    class Meta:
        model = Modifiers
        fields = ['id','title','description','price']


class ItemSerializers1(WritableNestedModelSerializer):
    modifiers = ModifiersSerializers1(many=True,)
    title = serializers.CharField(source='name')

    class Meta:
        model = Item
        fields = ['id','title',"description",'price','modifiers']


    def validate(self,data):
        item = Item.objects.values_list('name', flat=True)
        if data['name'] in item:
            raise serializers.ValidationError("Item is already exists")
        return data



class SectionSerializer1(serializers.ModelSerializer):
    items = ItemSerializers1(many=True, read_only=True)
    title = serializers.CharField(source='name')

    class Meta:
        model = Section
        fields = ['id','title',"description",'items']

