from rest_framework import serializers
from . models  import Truck , IceCream,IceCreamFlavor, ShavedIce, Snackbar

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name','address',)
        model = Truck

class IceCreamFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = IceCreamFlavor

class IceCreamSerializer(serializers.ModelSerializer):
    flavor = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'price','name', 'flavor', 'quantity')
        model = IceCream   

class ShavedIceSerializer(serializers.ModelSerializer): 

    class Meta:
        fields = ('id', 'price','name', 'quantity')
        model = ShavedIce

class SnackbarSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'price','name', 'quantity')
        model = Snackbar

class TruckItemsSerializer(serializers.Serializer):    
    ice_creams = IceCreamSerializer(many=True)
    shaved_ice = ShavedIceSerializer(many=True)
    snackbars = SnackbarSerializer(many=True)     

class TruckinventorySerializer(serializers.Serializer):
    ice_creams = IceCreamSerializer(many=True)
    shaved_ice = ShavedIceSerializer(many=True)
    snackbars = SnackbarSerializer(many=True)  
    moneyEarned = serializers.IntegerField()      