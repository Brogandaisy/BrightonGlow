from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import CustomerProfileForm



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, email=form.cleaned_data.get('email'))  # Save email to Customer
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def update_profile(request):
    customer = request.user.customer  
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')  
        form = CustomerProfileForm(instance=customer)
    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def view_orders(request):
    orders = request.user.customer.order_set.all()  # Get the logged-in user's orders
    return render(request, 'accounts/orders.html', {'orders': orders})