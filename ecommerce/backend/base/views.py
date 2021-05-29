from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .products import products


# Create your views here.
class MyRoutes(APIView):
    def get(self,request):
        return Response('bonjour')

class ProductList(APIView):
    def get(self,request):
        return Response(products)

class ProductView(APIView):
    def get(self,request,idprod):
        produit=None
        for elmt in products:
            if elmt["_id"]==idprod:
                produit=elmt
                break
        return Response(produit)





