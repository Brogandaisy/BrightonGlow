from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
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
                return render
            (request, 'accounts/register.html', {'form': form})

            # Create user
            user = form.save()
            Customer.objects.create(user=user, email=email)
            login(request, user)

            try:
                send_mail(
                    'Welcome to BrightonGlow!',
                    'Thank you for registering!',
                    'Visit our website to explore our full range of skincare!',
                    'brogandaisy@gmail.com',
                    [email],
                    fail_silently=False,
                )
            except Exception:
                messages.error
                (request, "Registration successful, but email failed to send.")

            return redirect('profile')

        else:
            # Handle form errors properly
            messages.error
            (request, "There were errors in your form. Please correct them.")

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
    customer, created = Customer.objects.get_or_create(user=request.user)
    form = CustomerProfileForm(request.POST or None, instance=customer)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def profile(request):
    """Displays the user's profile and order history."""
    orders = (
        Order.objects.filter(user=request.user)
        .exclude(status="PENDING")
        .order_by('-created_at')
    )

    customer = getattr(request.user, "customer", None)

    return render(
        request,
        'accounts/profile.html',
        {
            'orders': orders,
            'customer': customer
        }
    )


@login_required
def view_orders(request):
    """Shows all orders made by the logged-in user."""
    orders = request.user.customer.order_set.all()
    return render(request, 'accounts/orders.html', {'orders': orders})


@login_required
def delete_account(request):
    """Allows a logged-in user to delete their account and logs them out."""
    if request.method == 'POST':
        user = request.user
        logout(request)  # log the user out before deleting the account
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return render(request, 'accounts/delete_account.html')
