from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Customer
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)  # ✅ Create a linked Customer profile
            login(request, user)  # ✅ Log the user in after registration
            return redirect('home')  
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def view_orders(request):
    orders = request.user.customer.order_set.all()  # Get the logged-in user's orders
    return render(request, 'accounts/orders.html', {'orders': orders})