from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import CustomerProfileForm
from orders.models import Order
from django.core.mail import send_mail
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, email=form.cleaned_data.get('email'))
            login(request, user)
            
            try:
                send_mail(
                    'Welcome to BrightonGlow!',
                    'Thank you for registering!',
                    'Visit our website to explore our full range of skincare!'
                    'brightonglowskincare@gmail.com',
                    [form.cleaned_data.get('email')],
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, "Registration successful, but email failed to send.")
                print(f"EMAIL ERROR: {e}")

            return redirect('home')

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
    else:
        form = CustomerProfileForm(instance=customer) 
    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).exclude(status="PENDING").order_by('-created_at')
    return render(request, 'accounts/profile.html', {'orders': orders})

@login_required
def view_orders(request):
    orders = request.user.customer.order_set.all()  # Get the logged-in user's orders
    return render(request, 'accounts/orders.html', {'orders': orders})

