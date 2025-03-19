from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')  # Render the home page


from .models import Customer, Product, Sale
from .forms import CustomerForm, ProductForm, SaleForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'core/customer_list.html', {'customers': customers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'core/sale_list.html', {'sales': sales})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'core/add_customer.html', {'form': form})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {'form': form})

def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'core/add_sale.html', {'form': form})