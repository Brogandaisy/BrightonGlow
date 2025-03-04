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
                messages.error(
                    request,
                    "A user with that email already exists. Please try again."
                )
                return render(
                    request, 'accounts/register.html', {'form': form}
                    )

            # Create user
            user = form.save()
            Customer.objects.create(user=user, email=email)
            login(request, user)

            try:
                send_mail(
                    'Welcome to BrightonGlow!',
                    'Thank you for registering!',
                    'brightonglowskincare@gmail.com',
                    [email],
                    fail_silently=False,
                )
            except Exception:
                messages.error(
                    request, "Successful, but email failed to send."
                    )

            return redirect('profile')

        else:
            messages.error(
                request, "There were errors in your form. Please correct them."
                )
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

            return render(request, 'accounts/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def update_profile(request):
    """Allows users to update their profile information including wishlist."""
    customer = request.user.customer

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            wishlist_products = form.cleaned_data.get('wishlist')
            customer.wishlist.set(wishlist_products)
            form.save()
            messages.success(
                request, "Your profile has been updated successfully!"
                )
            return redirect('profile')
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def profile(request):
    """Displays the user's profile, order history, and wishlist."""
    customer = request.user.customer
    orders = (
        Order.objects.filter(user=request.user)
        .exclude(status="PENDING")
        .order_by('-created_at')
    )
    wishlist_items = customer.wishlist.all()

    return render(request, 'accounts/profile.html', {
        'orders': orders,
        'wishlist_items': wishlist_items
    })


@login_required
def view_orders(request):
    """Shows all orders made by the logged-in user."""
    orders = request.user.customer.order_set.all()
    return render(request, 'accounts/orders.html', {'orders': orders})
