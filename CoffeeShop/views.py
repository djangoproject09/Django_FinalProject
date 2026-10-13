from django.shortcuts import render

SHOP = {
    'name': 'Velvet Crema',
    'tagline': 'Smooth coffee. Warm corners. Fresh pastries.',
    'address': 'Your shop address here',
    'phone': '0900 000 0000',
    'hours': 'Daily, 8:00 AM to 8:00 PM',
}

MENU = [    
    {'name': 'Americano', 'type': 'Coffee', 'price': 90, 'image':'Americano.jpg'},
    {'name': 'Capuccino', 'type': 'Coffee', 'price': 110, 'image':'Capuccino.jpg'},
    {'name': 'Caffe Latte', 'type': 'Non-Coffee', 'price': 120, 'image':'Caffe_Latte.jpg'},
    {'name': 'Matcha Latte', 'type': 'Coffee', 'price': 130, 'image':'Matcha_Latte.jpg'},
    {'name': 'Butter Croissant', 'type': 'Pastry', 'price': 80, 'image':'Butter_Croissant.jpg'},
    {'name': 'Cheesecake Slice', 'type': 'Pastry', 'price': 120, 'image':'Cheesecake_Slice.jpg'},
]

PHOTOS = [
    {'images':'Americano.jpg'},
       {'images':'Capuccino.jpg'},
                {'images':'Butter_Croissant.jpg'},
                   
]

def home(request):
    return render(request, 'home.html', {'shop': SHOP, 'FEATURED': MENU[:3]})


def menu(request):
    return render(request, 'menu.html', {'shop': SHOP, 'menu': MENU})


def about(request):
    return render(request, 'about.html', {'shop': SHOP})


def gallery(request):
    return render(request, 'gallery.html', {'shop': SHOP, 'photos': PHOTOS})


def contact(request):
    return render(request, 'contact.html', {'shop': SHOP})
