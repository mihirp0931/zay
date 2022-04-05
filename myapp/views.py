from django.shortcuts import render,redirect
from .models import Contact,User,Product,Whishlist,Cart,Transaction
from django.conf import settings
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def shop(request):
    products=Product.objects.all()
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def collection_men(request):
    products=Product.objects.filter(product_collection="men")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def collection_women(request):
    products=Product.objects.filter(product_collection="women")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def collection_Kids(request):
    products=Product.objects.filter(product_collection="kids")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def category_cloth(request):
    products=Product.objects.filter(product_category="cloth")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def category_footware(request):
    products=Product.objects.filter(product_category="footwear")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def category_watchs(request):
    products=Product.objects.filter(product_category="watchs")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def category_accessoies(request):
    products=Product.objects.filter(product_category="accessoies")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def size_s(request):
    products=Product.objects.filter(product_size="s")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def size_m(request):
    products=Product.objects.filter(product_size="m")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def size_l(request):
    products=Product.objects.filter(product_size="l")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})


def size_xl(request):
    products=Product.objects.filter(product_size="xl")
    men=len(Product.objects.filter(product_collection="men"))
    women=len(Product.objects.filter(product_collection="women"))
    kids=len(Product.objects.filter(product_collection="kids"))
    cloth=len(Product.objects.filter(product_category="cloth"))
    footwear=len(Product.objects.filter(product_category="footwear"))
    watchs=len(Product.objects.filter(product_category="watchs"))
    accessoies=len(Product.objects.filter(product_category="accessoies"))
    s=len(Product.objects.filter(product_size="s"))
    m=len(Product.objects.filter(product_size="m"))
    l=len(Product.objects.filter(product_size="l"))
    xl=len(Product.objects.filter(product_size="xl"))
    return render(request,'shop.html',{'products':products,'men':men,'women':women,'kids':kids,'cloth':cloth,'footwear':footwear,'watchs':watchs,'accessoies':accessoies,'s':s,'m':m,'l':l,'xl':xl})

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
            )
        msg="contact saved successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')

def signin(request):
    if request.method=="POST":
        try:
            user=User.objects.get(
                email=request.POST['email'],
                password=request.POST['password'],
                )
            if user.usertype=="user":
                request.session['email']=user.email
                request.session['name']=user.name
                whishlists=Whishlist.objects.filter(user=user)
                request.session['whishlist_count']=len(whishlists)
                carts=Cart.objects.filter(user=user)
                request.session['cart_count']=len(carts)
                return render(request,'index.html')
            else :
                request.session['email']=user.email
                request.session['name']=user.name
                return render(request,'seller_index.html')
        except:
            msg="email or password is incorrect "
            return render(request,'signin.html',{'msg':msg})
    else:
        return render(request,'signin.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['name']
        return render(request,'signin.html')
    except:    
        return render(request,'signin.html')


def register(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="email already registered"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['password2']:
                User.objects.create(
                    usertype=request.POST['usertype'],
                    name=request.POST['name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    )
                msg="user register successfully"
                return render(request,'register.html',{'msg':msg})
            else:
                msg="password and confirmpassword does not matched"
                return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')

def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if user.usertype=="user":
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['new_password2']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="password and confirm password does not matched" 
                    return render(request,'change_password.html',{'msg':msg})
            else:
                msg="old password does not matched" 
                return render(request,'change_password.html',{'msg':msg})
        else:
            return render(request,'change_password.html')
    else:
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['new_password2']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="password and confirm password does not matched" 
                    return render(request,'seller_change_password.html',{'msg':msg})
            else:
                msg="old password does not matched" 
                return render(request,'seller_change_password.html',{'msg':msg})
        else:
            return render(request,'seller_change_password.html')

def seller_index(request):
    return render(request,'seller_index.html')


def add_product(request):
    if request.method=="POST":
        product_seller=User.objects.get(email=request.session['email'])
        Product.objects.create(
            product_seller=product_seller,
            product_collection=request.POST['product_collection'],
            product_category=request.POST['product_category'],
            product_size=request.POST['product_size'],
            product_price=request.POST['product_price'],
            product_discription=request.POST['product_discription'],
            product_image=request.FILES['product_image'],
            )
        msg="Product added successfully"
        return render(request,'add_product.html',{'msg':msg})
    else:
        return render(request,'add_product.html')


def view_product(request):
    product_seller=User.objects.get(email=request.session['email'])
    products=Product.objects.filter(product_seller=product_seller)
    return render(request,'view_product.html',{'products':products})


def edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
            product.product_collection=request.POST['product_collection']
            product.product_category=request.POST['product_category']
            product.product_size=request.POST['product_size']
            product.product_price=request.POST['product_price']
            product.product_discription=request.POST['product_discription']
            try:
                product.product_image=request.FILES['product_image']
            except:
                pass
            product.save()
            return render(request,'edit_product.html',{'product':product}) 

    else:
        return render(request,'edit_product.html',{'product':product})


def delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('view_product')

def shop_single(request,pk):
    whishlist_flag=False
    cart_flag=False
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    try:
        Whishlist.objects.get(user=user,product=product)
        whishlist_flag=True
    except:
        pass

    try:
        Cart.objects.get(user=user,product=product,payment_status='pending')
        cart_flag=True
    except:
        pass
    return render(request,'shop_single.html',{'product':product,'whishlist_flag':whishlist_flag,'cart_flag':cart_flag})


def whishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Whishlist.objects.create(
            user=user,
            product=product
        )
    return redirect('whishlist2')

def whishlist2(request):
    user=User.objects.get(email=request.session['email'])
    whishlists=Whishlist.objects.filter(user=user)
    request.session['whishlist_count']=len(whishlists)
    return render(request,'wishlist.html',{'whishlists':whishlists})


def delete_from_whishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    whishlist=Whishlist.objects.filter(user=user,product=product)
    whishlist.delete()
    return redirect('whishlist2')



def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
            user=user,
            product=product,
            product_price=product.product_price,
            product_qty=1,
            total_price=product.product_price
        )
    return redirect('cart')

def cart(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status="pending")
    for i in carts:
        net_price=net_price+i.total_price
        request.session['cart_count']=len(carts)
    return render(request,'cart.html',{'carts':carts,'net_price':net_price})


def delete_from_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user,product=product)
    cart.delete()
    return redirect('cart')


def change_qty(request):
    cart=Cart.objects.get(pk=request.POST['cid'])
    product_qty=int(request.POST['product_qty'])
    cart.product_qty=product_qty
    cart.total_price=cart.product_price*product_qty
    cart.save()
    return redirect('cart')




def initiate_payment(request):
    user=User.objects.get(email=request.session['email'])
    try:
       
        amount = int(request.POST['amount'])
       
    except:
        return render(request, 'pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=user,amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://localhost:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()
    carts=Cart.objects.filter(user=user)
    for i in carts:
        i.payment_status="paid"
        i.save()
        
    carts=Cart.objects.filter(user=user,payment_status="pending")
    request.session['cart_count']=len(carts)
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'callback.html', context=received_data)
        return render(request, 'callback.html', context=received_data)

def my_orders(request):
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status='paid')
    return render(request,'my_orders.html',{'carts':carts})

def validate_signup(request):
    email=request.GET.get('email')
    data={
        'is_taken':User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


