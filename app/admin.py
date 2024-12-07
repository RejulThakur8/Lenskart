from django.contrib import admin
from .models import sign,products,category,slider,glass,shape,banner,cart,wishlist,google,contactus,frame,banners,size,brands,color
# Register your models here


class productsAdmin(admin.ModelAdmin):
    list_display=['title','description','price','rating','category_name','shape_name','banner_name','glass_name','name']

admin.site.register(sign)
admin.site.register(products,productsAdmin)
admin.site.register(category)
admin.site.register(glass)
admin.site.register(slider)
admin.site.register(shape)
admin.site.register(banner)
admin.site.register(cart)
admin.site.register(wishlist)
admin.site.register(google)
admin.site.register(contactus)
admin.site.register(frame)
admin.site.register(banners)
admin.site.register(size)
admin.site.register(color)
admin.site.register(brands)