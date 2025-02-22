from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import hashers
from django.contrib import messages
import os



def lo(request):
    g=glass.objects.all()
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password=hashers.make_password(password)

        user = User.objects.filter(email=email)

        if user.exists():
            messages.info(request,'Email Already Exists! Please Enter New Mail')
            return redirect("/lo/",{'data2':g[:5]})
            
        User.objects.create(username=username,email=email,password=password)

        messages.success(request,'Account Created Succesfully')
        

    return render(request,'s.html',{'data2':g[:5]})



def loguser(request): 
    d=category.objects.all()
    sl=slider.objects.all()
    g=glass.objects.all()
    for sd in sl:
        sd.image=os.path.basename(sd.image.url)
    for j in d:
        j.image1=os.path.basename(j.image1.url)
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.warning(request,"Invalid Usename")
            return redirect('/login/')
        # user=sign.objects.filter(email=email,password=password)

        user = authenticate(username = username, password = password)

        print(username,password,user)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login/',{'data1':d,'slider':sl,'data2':g[:5]})
        else:
            login(request, user)
            messages.success(request,"you are lonin successfully")
            return redirect('/home/',{'data1':d,'slider':sl,'data2':g[:5]})

    return render(request,'s.html',{'data1':d,'slider':sl,'data2':g[:5]})

def logout_users(request):
    d=category.objects.all()[:5]
    sl=slider.objects.all()
    g=glass.objects.all()
    for sd in sl:
        sd.image=os.path.basename(sd.image.url)
    for j in d:
        j.image1=os.path.basename(j.image1.url)

    logout(request)
    return render(request,'index.html',{'data1':d,'slider':sl,'data2':g[:4]})

def si(request):
    return render(request,'s.html')

def track(request):
    g=glass.objects.all()
    return render(request,'track.html',{'data2':g[:5]})

def home(request):
    d=category.objects.all()
    sl=slider.objects.all()
    g=glass.objects.all()
    s=shape.objects.all()
    b=banner.objects.exclude(banner_name='default')
    bnr=banners.objects.exclude(banners_name='default')
    print(b)
    print(bnr)
    for shpe in s:
        shpe.image=os.path.basename(shpe.image.name)
    for sd in sl:
        sd.image=os.path.basename(sd.image.url)
    for j in d:
        j.image1=os.path.basename(j.image1.url)
    for i in b:
        i.banner_image=os.path.basename(i.banner_image.url)
    for bn in bnr:
        bn.banners_image=os.path.basename(bn.banners_image.url)
    return render(request,'index.html',{'data1':d[:5],'slider':sl,'data2':g[:5],'data3':s[:4],'data4':b,'data5':bnr})


def pwr(request):
    a=products.objects.all()
    for b in a:
        b.image2=os.path.basename(b.image2.url)
    return render(request,'pw.html',{'data3':a})

def sun(request):
    return render(request,'sungl.html')

def po(request):
    return render(request,'pw.html')


def eyeglass(request):
    if request.method=="POST":
        category1=request.POST.get("category")
        print(category1.title())
        g=glass.objects.all()[:5]
        framee=frame.objects.all()
        bra_nd=brands.objects.all()
        print(bra_nd)
        cat=category.objects.get(category_name=category1.title())
        if cat:
            data=products.objects.filter(category_name=cat)
            print(data)
            for i in data:  
                i.image=os.path.basename(i.image.name)
                print(i.category_name)
            for i in framee:
                i.frame_image=os.path.basename(i.frame_image.url)
        return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framee,'brands':bra_nd})
    return render(request,'pw.html')


def sun(request):
    sung=products.objects.all()
    for s in sung:
        s.image=os.path.basename(s.image.name)
    return render(request,'sungl.html',{'data':sung})
        
def detail(request):
    if request.method=="POST":
        print("hello")
        g=glass.objects.all()
        title1=request.POST.get('title')
        p=products.objects.filter(title=title1)
        print(title1,p)
        for i in p:
            i.image2=os.path.basename(i.image2.name)
            i.image3=os.path.basename(i.image3.name)
            i.image4=os.path.basename(i.image4.name)
            i.image5=os.path.basename(i.image5.name)
            i.image6=os.path.basename(i.image6.name)
            i.image7=os.path.basename(i.image7.name)
            i.image8=os.path.basename(i.image8.name)
            i.image9=os.path.basename(i.image9.name)
            i.image10=os.path.basename(i.image10.name)
            i.image11=os.path.basename(i.image11.name)
            i.airess1=os.path.basename(i.airess1.name)
            i.airess2=os.path.basename(i.airess2.name)
            i.airess3=os.path.basename(i.airess3.name)
            i.airess4=os.path.basename(i.airess4.name)
            i.airess5=os.path.basename(i.airess5.name)
            i.airess6=os.path.basename(i.airess6.name)
            i.airess7=os.path.basename(i.airess7.name)
            i.airess8=os.path.basename(i.airess8.name)
        return render(request,'product detail.html',{'data':p,'data2':g[:5]})
    

def profile(request):
    return render(request,'profile.html')



def round(request):
    if request.method=="POST":
        category1=request.POST.get("shape")
        print(category1)
        s=shape.objects.all()
        g=glass.objects.all()
        cat=shape.objects.get(shape_name=category1)
        if cat:
            data=products.objects.filter(shape_name=cat)
            print(data)
            for i in data:  
                i.image=os.path.basename(i.image.name)
                print(i.shape_name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,'pw.html')

def john(request):
    if request.method=="POST":
        category3=request.POST.get("banner")
        print(category3)
        g=glass.objects.all()
        cat1=banner.objects.get(banner_name=category3)
        print(cat1)
        if cat1: 
            data=products.objects.filter(banner_name=cat1)
            print(data,"hello")
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,('index.html'))
        

def trending(request):
    if request.method=="POST":
        category2=request.POST.get("banner")
        print(category2)
        g=glass.objects.all()
        cat2=banner.objects.get(banner_name=category2)
        print(cat2)
        if cat2: 
            data=products.objects.filter(banner_name=cat2)
            print(data)
            for i in data:
                i.image=os.path.basename(i.image.name)
                print(i.banner_name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,('index.html'))

def framee(request):
    g=glass.objects.all()[:5]
    framees=frame.objects.all()
    bra_nd=brands.objects.all()
    try:
        if request.method=="POST":
            frame_name=request.POST.get("frame_name")
            frame_obj=get_object_or_404(frame, frame_name=frame_name)
            data=products.objects.filter(frame_name=frame_obj)
            for i in data:
                i.image=os.path.basename(i.image.url)
            for i in framees:
                i.frame_image=os.path.basename(i.frame_image.url)
            return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framees,'brands':bra_nd})
    except Exception as e:
        print(f"Error: {e}")
        messages.error(request,"Your Query Does Not Found Please try again!")
        return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framees,'brands':bra_nd})


def sliders(request):
    g=glass.objects.all()
    try:
        if request.method=="POST":
            slider_name=request.POST.get("slider_name")
            slider_obj= get_object_or_404(slider, slider_name=slider_name)
            print(slider_obj)
            data=products.objects.filter(slider_name=slider_obj)
            print(data)
            g=glass.objects.all()
            for i in data:
                i.image=os.path.basename(i.image.url) 
                           
            return render(request,'eyeglasses.html',{'data':data,'data2':g,})
        else:
            messages.error(request,"Invalid request method")
            return render(request,'eyeglasses.html',{'data':data,'data2':g})
    except Exception as e:
        print(f"Error: {e}")
        messages.error(request,"A technical issues occurs, Please try again!")
        return render(request,'eyeglasses.html',{'data':data,'data2':g})
    
def brnd(request):
    g=glass.objects.all()[:5]
    framee=frame.objects.all()
    bra_nd=brands.objects.all()
    try:
        if request.method=="POST":
            brand_name=request.POST.get("brand")
            brand_obj= get_object_or_404(brands, brand=brand_name)
            print(brand_obj)
            data=products.objects.filter(brand=brand_obj)
            print(data)
            g=glass.objects.all()[:5]
            for i in data:
                i.image=os.path.basename(i.image.url) 
            for i in framee:
                i.frame_image=os.path.basename(i.frame_image.url)           
            return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framee,'brands':bra_nd})
        else:
            messages.error(request,"Invalid request method")
            return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framee,'brands':bra_nd})
    except Exception as e:
        print(f"Error: {e}")
        messages.error(request,"A technical issues occurs, Please try again!")
        return render(request,'eyeglasses.html',{'data':data,'data2':g,'frame':framee,'brands':bra_nd})

def ct(request):
    print("hey")
    g=glass.objects.all()[:5]
    if request.method=="POST":
       Cart = products.objects.get(id=request.POST["iid"])
       qyt = request.POST['quantity']
       print(Cart)
       tp=int(Cart.price) * int(qyt)
       cart.objects.create(pro_d=Cart,quantity=qyt,user=request.user,price=tp)
    data=cart.objects.filter(user=request.user)
    Total=0
    for i in data:
          i.pro_d.image=os.path.basename(i.pro_d.image.name)
          Total+=int(i.price)
    return render(request,'cart.html',{'data':data,'Total':Total,'data2':g,})

def remove(request):
    if request.method=="POST":
        name = request.POST.get("pro_d")

        data = cart.objects.filter(pro_d=name, user=request.user)
        data.delete()

        Total=0
        for i  in data:
            Total+=int(i.price)
    return redirect('/cart/')

def wish(request):
    print("wishh")
    g=glass.objects.all()[:5]
    if request.method=="POST":
        wname=request.POST.get('proname')
        print(wname)
        wpro=products.objects.get(pro_d=wname)
        print(wpro)
        price=request.POST.get('price')
        print(price)
        g=glass.objects.all()
        wishlist.objects.create(pro_d=wpro,price=price,user_id=request.user)
    data3=wishlist.objects.filter(user_id=request.user)
    for i in data3:
        i.pro_d.image=os.path.basename(i.pro_d.image.name)
    return render(request,'wishlist.html',{'data':data3,'data2':g})  


def contaact(request):
    g=glass.objects.all()[:5]
    if request.method=="POST":
        fname = request.POST.get("First name")
        lname = request.POST.get("Last name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contactus.objects.create(fname = fname,lname=lname,email=email,message=message,user=request.user)

    return render(request,'contact.html',{'data2':g})

def gogle(request):
    go=google.objects.all()
    for i in go:
        i.image=os.path.basename(i.image.name)
    return render(request,'footer.html',{'data':go})