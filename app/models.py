from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

class sign(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50,default="fname")
    last_name=models.CharField(max_length=40,default="lasname")
    def __str__(self):
        return self.username
    
class frame(models.Model):
    frame_image=models.ImageField(upload_to='statics/images',default="frameImage")
    frame_name=models.CharField(max_length=50,default='square')
    def __str__(self):
        return self.frame_name

class size(models.Model):
    frame_size=models.CharField(max_length=50,default='medium')
    def __str__(self):
        return self.frame_size
    
class color(models.Model):
    frame_color=models.CharField(max_length=50,default='black')
    def __str__(self):
        return self.frame_color
    
class brands(models.Model):
    brand=models.CharField(max_length=50,default='air')
    def __str__(self):
        return self.brand
    
class category(models.Model):
     image1=models.ImageField(upload_to='statics/images',default='b')
     category_name=models.CharField(max_length=50)
     def __str__(self):
         return self.category_name
     
class shape(models.Model):
    image=models.ImageField(upload_to='statics/images',default='a')
    shape_name=models.CharField(max_length=50)
    def __str__(self):
        return self.shape_name


class banner(models.Model):
    banner_head=models.CharField(max_length=60,default='hustlr')
    banner_name=models.CharField(max_length=50)
    banner_image=models.ImageField(upload_to='statics/images',default='b')
    def __str__(self):
        return self.banner_name

class banners(models.Model):
    banners_image=models.ImageField(upload_to='statics/images',default="air")
    banners_name=models.CharField(max_length=50,null=True)
    banner_head=models.CharField(max_length=60,default='Hustlr')

    def __str__(self):
        return self.banners_name
    
class glass(models.Model):
    glass_name=models.CharField(max_length=50)
    def __str__(self):
        return self.glass_name
    
class slider(models.Model):
    image=models.ImageField(upload_to='statics/images',default='i')
    slider_name = models.CharField(max_length=60)
    def __str__(self):
        return self.slider_name
    

class products(models.Model):
    cont=models.CharField(max_length=100,default='z')
    image=models.ImageField(upload_to='statics/images',default='c')
    title=models.CharField(max_length=100,default='d')
    description=models.CharField(max_length=100,default='d')
    price=models.IntegerField(null=True)
    rating=models.CharField(max_length=50,default='d')
    offer=models.CharField(max_length=100,default='d')
    banners_name=models.ForeignKey(banners,related_name='ban_name',on_delete=models.CASCADE,default=10) 
    category_name=models.ForeignKey(category,related_name='categoy_name',on_delete=models.CASCADE,default=5)
    shape_name=models.ForeignKey(shape,related_name='shape_name1',on_delete=models.CASCADE,default=5)
    banner_name=models.ForeignKey(banner,related_name='banner_name1',on_delete=models.CASCADE,default=2)
    glass_name=models.ForeignKey(glass,related_name='glass_name2',on_delete=models.CASCADE,default=5)
    frame_size=models.ForeignKey(size,related_name='size2',on_delete=models.CASCADE,default=20)
    brand=models.ForeignKey(brands,related_name='brand2',on_delete=models.CASCADE,default=10)
    frame_color=models.ForeignKey(color,related_name='color2',on_delete=models.CASCADE,default=40)
    frame_name=models.ForeignKey(frame,related_name='frame2',on_delete=models.CASCADE,default=40)
    slider_name=models.ForeignKey(slider,related_name='s_name',on_delete=models.CASCADE)
    image2=models.ImageField(upload_to='statics/images',default='d')
    image3=models.ImageField(upload_to='statics/images',default='d')
    image4=models.ImageField(upload_to='statics/images',default='d')
    image5=models.ImageField(upload_to='statics/images',default='d')
    image6=models.ImageField(upload_to='statics/images',default='d')
    image7=models.ImageField(upload_to='statics/images',default='d')
    image8=models.ImageField(upload_to='statics/images',default='d')
    image9=models.ImageField(upload_to='statics/images',default='d')
    image10=models.ImageField(upload_to='statics/images',default='d')
    image11=models.ImageField(upload_to='statics/images',default='d')
    pro_d=models.CharField(max_length=200,default='d')
    description1=models.CharField(max_length=100,default='d')
    caption=models.CharField(max_length=200,default='d')
    airess1=models.ImageField(upload_to='statics/images',default='e')
    airess2=models.ImageField(upload_to='statics/images',default='e')
    airess3=models.ImageField(upload_to='statics/images',default='e')
    airess4=models.ImageField(upload_to='statics/images',default='e')
    airess5=models.ImageField(upload_to='statics/images',default='e')
    airess6=models.ImageField(upload_to='statics/images',default='e')
    airess7=models.ImageField(upload_to='statics/images',default='e')
    airess8=models.ImageField(upload_to='statics/images',default='e')

    def __str__(self):
        return self.pro_d


class cart(models.Model):
    pro_d=models.ForeignKey(products,related_name='pro_d1',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(null=True)

class wishlist(models.Model):
    pro_d=models.ForeignKey(products,related_name='pro_d2',on_delete=models.CASCADE)
    price=models.IntegerField(null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    

class contactus(models.Model):
    fname = models.CharField(null=True,blank=True,max_length=50)
    lname = models.CharField(null=True,blank=True,max_length=50)
    email = models.EmailField()
    message = models.TextField(default="A")
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class google(models.Model):
    image=models.ImageField(upload_to='statics/images',default='i')
    
