from rest_framework import generics
from collections import namedtuple
from rest_framework.views import APIView
from rest_framework.response import Response

from . models  import Truck , IceCream, ShavedIce, Snackbar
from . serializers import TruckSerializer , TruckItemsSerializer , TruckinventorySerializer



product_mapping = {"ice_cream":IceCream, "shaved_ice":ShavedIce, "snackbar": Snackbar }

class ListTruck(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class DetailTruck(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class TruckItems (APIView):
    def get(self, request, pk):
        """
        Return all items from truck.
        """
        truck_id = self.kwargs['pk']
        ice_creams = IceCream.objects.filter(truck=truck_id, quantity__gt = 0)
        shaved_ice = ShavedIce.objects.filter(truck=truck_id, quantity__gt = 0)
        snackbars = Snackbar.objects.filter(truck=truck_id, quantity__gt = 0)

        Items = namedtuple('items', ('ice_creams', 'shaved_ice','snackbars'))

        items  = Items(
            ice_creams=ice_creams,
            shaved_ice=shaved_ice,
            snackbars = snackbars
        )
        serializer = TruckItemsSerializer(items)
        return Response(serializer.data,)

class TruckItemsBuy (APIView):
    def post(self, request):
        """
        Buy an items from truck.
        """
        truck_id = request.data['truck']
        product = request.data['product']
        product_id = request.data['id']
        product_qs = product_mapping[product].objects.filter(truck=truck_id, id = product_id, quantity__gt = 0)
        if product_qs :
            product = product_qs[0]
            product.sold +=1
            product.quantity-=1
            product.save()
            return Response("ENJOY!")
        else :
            return Response("SORRY!")    

class Truckinventory(APIView):
    def get(self, request, pk):
        """
        Return all items from truck.
        """
        truck_id = self.kwargs['pk']
        ice_creams = IceCream.objects.filter(truck=truck_id)
        shaved_ice = ShavedIce.objects.filter(truck=truck_id)
        snackbars = Snackbar.objects.filter(truck=truck_id)
        total = 0
        for ice_cream in ice_creams:
            total+=int(ice_cream.price)*ice_cream.sold
        for shavedice in shaved_ice:
            total+=int(shavedice.price)*shavedice.sold
        for snackbar in snackbars:
            total+=int(snackbar.price)*snackbar.sold        

        Items = namedtuple('items', ('ice_creams', 'shaved_ice','snackbars', 'moneyEarned'))

        items  = Items(
            ice_creams=ice_creams,
            shaved_ice=shaved_ice,
            snackbars = snackbars,
            moneyEarned = total
        )
        serializer = TruckinventorySerializer(items, )
        return Response(serializer.data,)        
