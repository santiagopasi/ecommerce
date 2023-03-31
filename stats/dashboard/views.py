from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Order
from .forms import CreateProduct,CreateOrder
from user.models import Profile
from django.contrib.auth.decorators import login_required

# Get the amount of staff members or profiles with first name created
staff_elements=Profile.objects.all()
staff_counter=0
for staff in staff_elements:
        
    if staff.first_name != "":
        staff_counter=staff_counter+1

# Get the amount of products created
product_elements=Product.objects.all()
last_product= product_elements.last().last_product_added()
product_counter=0
for product in product_elements:
        
    if product.name != "":
        product_counter=product_counter+1
            
# Get the amount of products created by the user

def get_orders(request):

    order_elements=Order.objects.all().filter(staff=request.user)
    order_counter=0
    for order in order_elements:
        order_counter=order_counter+1
            
    return order_counter


@login_required(login_url='user-login')
def dashboard(request):
    
    
    orders = Order.objects.all().filter(staff=request.user)
    order_counter = get_orders(request)
    context={
        'product_elements':product_elements,
        'orders':orders,
        'staff_counter':staff_counter,
        'order_counter':order_counter,
        'product_counter':product_counter,
        'last_product':last_product
    }
    
    
    return render(request,'dashboard/index.html',context)

def index(request):
    
    return render(request,'partials/base.html')
    
@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    #creating the make a product logic
    order_counter = get_orders(request)

    form=CreateProduct()
    
    if request.method == 'POST':
              
        form=CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            
            context= {
                    'items':items,
                    'form':form,
                    'staff_counter':staff_counter,
                    'order_counter':order_counter,
                    'product_counter':product_counter,
                    'last_product':last_product
            }
            return render(request,'dashboard/product.html',context)
        else:
            form=CreateProduct()
            context= {
                    'items':items,
                    'form':form,
                    'staff_counter':staff_counter,
                    'order_counter':order_counter,
                    'product_counter':product_counter,
                    'last_product':last_product 
            }
            return render(request,'dashboard/product.html',context)
    else:

        context= {
            'items':items,
            'form':form,
            'staff_counter':staff_counter,
            'order_counter':order_counter,
            'product_counter':product_counter,
                    'last_product':last_product 
        }
        return render(request,'dashboard/product.html',context)

@login_required(login_url='user-login')
def product_delete(request,pk):
    order_counter=get_orders(request)
    #select a product to delete
    try:
        item = Product.objects.get(id=pk)
        
        message = f'Product {item} has been deleted.'
        #delete the product
        item.delete()
        #get all products
        items=Product.objects.all()

        #create product form
        form=CreateProduct()
        if request.method == 'POST':
            form=CreateProduct(request.POST)
            if form.is_valid():
                form.save()
                messageCreation=f'Product {item} has been added.'
                context= {
                        'messageCreation':messageCreation,
                        'items':items,
                        'form':form,
                        'staff_counter':staff_counter,
                        'order_counter':order_counter,
                        'product_counter':product_counter,
                    'last_product':last_product 
                }
                return render(request,'dashboard/product.html',context)
            else:
                form=CreateProduct()
                context= {
                        'items':items,
                        'form':form,
                        'staff_counter':staff_counter,
                        'order_counter':order_counter,
                        'product_counter':product_counter,
                    'last_product':last_product 
                }
                return render(request,'dashboard/product.html',context)
        else:

            context={
                'message':message,
                'items':items,
                'form':form,
                'staff_counter':staff_counter,
                'order_counter':order_counter,
                'product_counter':product_counter,
                    'last_product':last_product 
            }
            return render(request, 'dashboard/product.html',context)
    except:
    #if there is no product to select
        items=Product.objects.all()

        #create product form
        form=CreateProduct()
        if request.method == 'POST':
            form=CreateProduct(request.POST)
            if form.is_valid():
                form.save()
                context= {
                        'items':items,
                        'form':form,
                        'staff_counter':staff_counter,
                        'order_counter':order_counter,
                        'product_counter':product_counter,
                    'last_product':last_product 
                }
                return render(request,'dashboard/product.html',context)
            else:
                form=CreateProduct()
                context= {
                        'items':items,
                        'form':form,
                        'staff_counter':staff_counter,
                        'order_counter':order_counter,
                        'product_counter':product_counter,
                    'last_product':last_product 
                }
                return render(request,'dashboard/product.html',context)
        else:

            context={
                
                'items':items,
                'form':form,
                'staff_counter':staff_counter,
                'order_counter':order_counter,
                'product_counter':product_counter,
                    'last_product':last_product 
            }
            return render(request, 'dashboard/product.html',context)
        
@login_required(login_url='user-login')
def product_edit(request,pk):
    order_counter=get_orders(request)
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        form=CreateProduct(request.POST,instance=item)

        if form.is_valid():
            print('asdasd')
            form.save()
            
            
            return redirect('product')
    else:
        form=CreateProduct(instance=item)

    context={
    'form':form,
    'order_counter':order_counter,
    'product_counter':product_counter,
                    'last_product':last_product 

    }

    return render(request,'dashboard/product_edit.html',context)

    
@login_required(login_url='user-login')
def order(request):
    order_counter=get_orders(request)
    orders=Order.objects.all()
    
    if request.method == 'POST':
        form=CreateOrder(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user
            order.save()
            form=CreateOrder()

            context={
                'form':form,
                'orders':orders,
                'staff_counter':staff_counter,
                'order_counter':order_counter,
                'product_counter':product_counter,
                    'last_product':last_product 
               
            }
            return render(request,'dashboard/order.html',context)
        else:
            message='There was a problem with your order. Try again.'
            form=CreateOrder()
            context={
                'form':form,
                'message':message,
                'orders':orders,
                'staff_counter':staff_counter,
                'order_counter':order_counter,
                'product_counter':product_counter,
                    'last_product':last_product 
                
            }
            return render(request,'dashboard/order.html',context)
    else:
        form=CreateOrder(instance=request.user)
        context={
            'orders':orders,
            'form':form,
            'staff_counter':staff_counter,
            'order_counter':order_counter,
            'product_counter':product_counter,
                    'last_product':last_product 
            
        }

        return render(request,'dashboard/order.html',context)



def staff(request):
    
    workers = Profile.objects.all()
    if request.user.is_authenticated:
        order_counter=get_orders(request)
        context = {
            'workers':workers,
            'staff_counter':staff_counter,
            'order_counter':order_counter,
            'product_counter':product_counter,
                    'last_product':last_product 
        }
    else:

        
        
        
        context = {
                'workers':workers,
                'staff_counter':staff_counter,
                'product_counter':product_counter,
                    'last_product':last_product 
            }
    
    return render(request,'dashboard/staff.html',context)

def search_product(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        print(searched)
        products = Product.objects.filter(name__contains='a')
        context={
            'searched':searched,
            'products':products
        }
        return render(request,'dashboard/search.html',context)
    else:
        return render(request,'dashboard/search.html')

    