from django.contrib import admin

from .models import Truck, IceCreamFlavor, IceCream , ShavedIce, Snackbar

admin.site.register(Truck)
admin.site.register(IceCreamFlavor)
admin.site.register(IceCream)
admin.site.register(ShavedIce)
admin.site.register(Snackbar)