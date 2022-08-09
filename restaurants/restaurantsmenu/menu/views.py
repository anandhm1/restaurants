from django.shortcuts import render
from .serializers import SectionSerializer, ItemSerializer, ModifiersSerializer,SectionMenuSerializer,ItemMenuSerializer
from .models import Section, Item, Modifiers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SectionViews(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class ItemViews(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ModifiersViews(viewsets.ModelViewSet):
    serializer_class = ModifiersSerializer
    queryset = Modifiers.objects.all()



class MenuViews(viewsets.ViewSet):

    def list(self, request):
        std1 = Section.objects.all()
        serializer = SectionMenuSerializer(std1, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def retrieve(self, request, pk):

        try:
            std= Section.objects.get(id=pk)
        except Section.DoesNotExist:
            return Response({'msg':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = SectionMenuSerializer(std)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ItemMapModifiersView(viewsets.ViewSet):
    def retrieve(self, request, pk):

        try:
            std= Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response({'msg':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ItemMenuSerializer(std)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def update(self,request,pk):
        try:
            std=Item.objects.get(id=pk)
            print(std)
        except Item.DoestNotExist:
            return Response({'msg':'record not found'})
        serializer = ItemMenuSerializer(std,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


