from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomerProfileForm
from .models import Customer
from orders.models import Order


def register(request):
    """Handles user registration and sends a welcome email."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Check for duplicate email
            if Customer.objects.filter(email=email).exists():
                messages.error(request, "A user with that email already exists. Please use a different email.")
                return render(request, 'accounts/register.html', {'form': form})

            # Create user
            user = form.save()
            Customer.objects.create(user=user, email=email)
            login(request, user)

            try:
                send_mail(
                    'Welcome to BrightonGlow!',
                    'Thank you for registering! Visit our website to explore our full range of skincare!',
                    'brightonglowskincare@gmail.com',
                    [email],
                    fail_silently=False,
                )
            except Exception:
                messages.error(request, "Registration successful, but email failed to send.")

            return redirect('profile')

        else:
            # Handle form errors properly
            messages.error(request, "There were errors in your form. Please correct them.")

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

            # Render the page again with errors instead of causing a 500 error
            return render(request, 'accounts/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def update_profile(request):
    """Allows users to update their profile information."""
    customer = request.user.customer  
    form = CustomerProfileForm(request.POST or None, instance=customer)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile')  

    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def profile(request):
    """Displays the user's profile and order history."""
    orders = Order.objects.filter(user=request.user).exclude(status="PENDING").order_by('-created_at')
    return render(request, 'accounts/profile.html', {'orders': orders})

@login_required
def view_orders(request):
    """Shows all orders made by the logged-in user."""
    orders = request.user.customer.order_set.all()
    return render(request, 'accounts/orders.html', {'orders': orders})
