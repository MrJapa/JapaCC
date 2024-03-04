from django.contrib import admin
from .models import * 

admin.site.register(CustomUser)
admin.site.register(NyKategori)
admin.site.register(NyRestaurant)
admin.site.register(NyUnderkategori)
admin.site.register(NytMad)
admin.site.register(NyBestilling)


