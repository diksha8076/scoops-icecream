from django.shortcuts import render, redirect

def home(request):
    flavors = [
        {"name": "Strawberry", "description": "Sweet and fruity, made with real..."},
        {"name": "Pistachio", "description": "Nutty, creamy pistachio made with..."},
        {"name": "Vanilla Bean", "description": "Classic vanilla bean real made..."},
    ]
    return render(request, 'shop/home.html', {'flavors': flavors})

def flavors(request):
    all_flavors = [
        {"name": "Vanilla Bean", "price": "₹149", "img": "vanilla.jpeg", "desc": "Classic vanilla goodness"},
        {"name": "Pistachio", "price": "₹179", "img": "pistachio.jpeg", "desc": "Nutty creamy flavor"},
        {"name": "Strawberry", "price": "₹159", "img": "strawberry.jpeg", "desc": "Sweet strawberry love"},
        {"name": "Chocolate", "price": "₹189", "img": "chocolate.jpeg", "desc": "Rich Belgian chocolate"},
        {"name": "Mango Sorbet", "price": "₹139", "img": "mango.jpg", "desc": "Tropical mango blast"},
        {"name": "Kulfi", "price": "₹129", "img": "kulfi.jpeg", "desc": "Desi kesar pista kulfi"},
    ]
    return render(request, 'shop/flavors.html', {'all_flavors': all_flavors})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def add_to_cart(request, flavor_name):
    cart = request.session.get('cart', {})
    cart[flavor_name] = cart.get(flavor_name, 0) + 1
    request.session['cart'] = cart
    return redirect('flavors')

def cart_view(request):
    cart = request.session.get('cart', {})
    return render(request, 'shop/cart.html', {'cart': cart, 'total_items': sum(cart.values())})

def remove_from_cart(request, flavor_name):
    cart = request.session.get('cart', {})
    if flavor_name in cart:
        del cart[flavor_name]
    request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    request.session['cart'] = {}
    return render(request, 'shop/success.html')