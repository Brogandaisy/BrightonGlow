from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import CustomerProfileForm
from orders.models import Order
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=user, email=email)

            login(request, user)

            subject = "Welcome to BrightonGlow!"
            message = f"Hi {user.username},\n\nThank you for registering at BrightonGlow. We are excited to have you!"
            sender = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, sender, recipient_list, fail_silently=False)

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

