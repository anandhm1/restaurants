from django.shortcuts import render
from .serializers import SectionSerializers, ItemSerializers, ModifiersSerializers,SectionSerializer1,ItemSerializers1
from .models import Section, Item, Modifiers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SectionViews(viewsets.ModelViewSet):
    serializer_class = SectionSerializers
    queryset = Section.objects.all()


class ItemViews(viewsets.ModelViewSet):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()


class ModifiersViews(viewsets.ModelViewSet):
    serializer_class = ModifiersSerializers
    queryset = Modifiers.objects.all()



class MenuViews(viewsets.ViewSet):

    def list(self, request):
        std1 = Section.objects.all()
        serializer = SectionSerializer1(std1, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def retrieve(self, request, pk):

        try:
            std= Section.objects.get(id=pk)
        except Section.DoesNotExist:
            return Response({'msg':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = SectionSerializer1(std)
        return Response(serializer.data,status=status.HTTP_200_OK)

class IteamMapModifiersViews(viewsets.ViewSet):
    def retrieve(self, request, pk):

        try:
            std= Modifiers.objects.get(id=pk)
        except Modifiers.DoesNotExist:
            return Response({'msg':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ModifiersSerializers(std)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def update(self,request,pk):
        try:
            std=Modifiers.objects.get(id=pk)
            print(std)
        except Modifiers.DoestNotExist:
            return Response({'msg':'record not found'})
        serializer = ModifiersSerializers(std,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NestIteamMapModifiersViews(viewsets.ModelViewSet):
    serializer_class = ItemSerializers1
    queryset = Item.objects.all()