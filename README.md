# BrightonGLOW

[View Live Project](https://brightonglow-a60ca67bc04b.herokuapp.com/)

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Agile Framework and Planning](#Agile-Framework-and-Planning)
4. [Payments & Stripe Integration](#payments-&-stripe-integration)
5. [Authentication & User Management](#Authentication-&-User-Management)
6. [Database & Data Management](#Database-&-Data-Management)
7. [Deployment](#Deployment)
8. [Testing](#Testing)
9. [Bugs & Debugging Process](#Bugs-&-Debugging-Process)
10. [Marketing & SEO](#Marketing-&-SEO)
11. [Future Features](#Future-Features)
12. [References & Credits](#References-&-Credits)

## About Brighton Glow
Brighton Glow is an online skincare website offering a curated selection of skincare products, inspired by the fresh and natural vibe of Brighton. Their goal is to make it easy for people to find skincare products that help them feel confident and look their best. They believe in keeping things simple and accessible, offering products that fit into your everyday routine and leave your skin glowing.

Customers can browse products by category (moisturisers, serums, masks, gift sets, etc.), filter by skin type, and add multiple products to their shopping bag. The platform provides a seamless check-out experience powered by Stripe, allowing secure transactions using webhooks. Registered users can log in to view their orders and update their details.

The site is built using Django and deployed via Heroku, utilising MySQL as the database and AWS for media storage.

### BrightonGLOW Visuals and Features
![BrightonGLOW](/static/images/readme/bghome.png)

Featured Products on the home page which choose 3 products from the catalogue at random.
![BrightonGLOW Featured Products](/static/images/readme/bgfeatured.png)
Information image and text blurb on the homepage, with a review and clickable link (CTA) to shop skincare.
![BrightonGLOW Homepage Information](/static/images/readme/bginfo.png)
Footer, displaying on all pages. Includes navigation to view pages from the nav bar, sign up to an email newsletter and visit social pages.
![BrightonGLOW Footer ](/static/images/readme/bgfooter.png)
NavBar with dropdown menu for shop categories and shop all products. NavBar links to contact and about pages. Plus shopping bag icons, login and register icons. Changes to Profile and Logout if user is authenticated.
![BrightonGLOW Navbar Features](/static/images/readme/bgnav.png)
All products page displaying all products in the shop.
![BrightonGLOW All Products](/static/images/readme/bgallproducts.png)
On the All Products page, there is a filter for Skin Types where you can filter products best for your skin type.
![BrightonGLOW SkinType Filter](/static/images/readme/bgfilter.png)
Product detail pages, displaying skin care type, description and price. Buttons to add more 1 or more products to your shopping bag.
![BrightonGLOW Product Page](/static/images/readme/bgproduct.png)
Product categories, including moisturisers, serums and masks.
![BrightonGLOW Categories ](/static/images/readme/bgcategory.png)
Shopping bag, listing all the products added to the bag ready for checkout. Delete, add and remove products.
![BrightonGLOW Shopping Bag](/static/images/readme/bgbag.png)
Checkout Page for payment and shipping information.
![BrightonGLOW Checkout and Stripe Payment](/static/images/readme/bgstripe.png)
About Us Page, with another featured products pop up for CTA.
![BrightonGLOW About Page](static/images/readme/bgabout.png)
Contact Us page including a contact form to ask for help or submit a question. 
![BrightonGLOW Contact Page and Form](/static/images/readme/bgcontact.png)

#### Branding
BrightonGlow’s branding is warm, modern, and minimal, with the use of white backgrounds enhancing the contrast of rich brown tones, creating a clean and natural feel. The use of rounded edges throughout the design adds softness and approachability, reinforcing a welcoming user experience. Typography is a key part of the brand identity—Shrikhand gives the titles a retro but warming feel, while Comfortaa keeps body text easy to read and visually balanced.

Product photography is simple and uncluttered, ensuring the focus remains on the products themselves. Images feature a diverse range of skin types, ages, and backgrounds, reflecting inclusivity and making the brand accessible to all.

The overall design is intentional and refined, combining subtle details with a clean layout to create a premium yet user-friendly experience.

#### Colour Pallette
Colour pallette used for Brighton GLOW, created by Coolers.co website
![BrightonGLOW Colour Pallette](/static/images/readme/bgcolours.png)

# Features

## E-Commerce Functionalities
#### - Browse Products by Category: Users can explore skincare products categorised into serums, masks, gift sets, and more.

This function retrieves all products within a specific category, which have been uploaded with a category and managed through Django Admin, and displays them on the category detail page.

      def category_detail(request, category_name):
          """Displays products belonging to a specific category."""
          
          category = get_object_or_404(Category, name=category_name)
          products = Product.objects.filter(category=category)
      
          return render(request, 'products/category_detail.html', {
              'category': category,
              'products': products
          })
  
#### - Filter Products by Skin Type: Users can refine their search by selecting products suited for oily, dry, combination, or sensitive skin.

#### - Shopping Bag & Checkout: Users can add multiple items to their shopping bag, modify quantities, and proceed to a secure checkout using Stripe.

This function adds a product to the shopping bag, updates the total price, and saves the data in the session. It retrieves the product by its ID, gets the selected quantity (defaulting to 1 if not specified), and then updates the bag before redirecting to the shopping bag detail page.

      def add_to_bag(request, product_id):
          """Adds a product to the shopping bag and updates total price."""
          
          bag = Bag(request)
          product = get_object_or_404(Product, id=product_id)
          quantity = int(request.POST.get('quantity', 1))  
      
          bag.add(product=product, quantity=quantity)
          request.session['total'] = bag.get_total_price()
      
          return redirect('bag_detail')

This JavaScript element enables users to increase or decrease the product quantity before adding it to their shopping bag. 

        <script>
        let quantity = 1;
        function increment() {
            quantity++;
            document.getElementById('quantity').innerText = quantity;
            document.getElementById('quantity-input').value = quantity;
        }
        function decrement() {
            if (quantity > 1) {
                quantity--;
                document.getElementById('quantity').innerText = quantity;
                document.getElementById('quantity-input').value = quantity;
            }
        }
        </script>


#### - Order History: Registered users can log in to view their order history.

The Profile view function retrieves and displays the user's profile and order history, ensuring only logged-in users can access it by using the @login_required decorator; it filters the Order model to fetch only the logged-in user's orders, excludes those with a "PENDING" status, sorts them by most recent first, and passes the data to the profile.html template for rendering.

      @login_required
      def profile(request):
          """Displays the user's profile and order history."""
          orders = Order.objects.filter(user=request.user).exclude(status="PENDING").order_by('-  created_at')
          return render(request, 'accounts/profile.html', {'orders': orders})

## Authentication & User Accounts
#### - User Registration & Welcome Email: New users can create a free user account and they will receive an automatic email upon signing up, welcoming them to BrightonGLOW.

I set up Django’s built-in email service using Gmail’s SMTP server by configuring the necessary settings in settings.py, allowing the system to automatically send a welcome email to new users upon registration, ensuring they receive a confirmation message from brightonglowskincare@gmail.com as soon as their account is created.

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

#### - Login & Logout: Users can log in to access their profile, order history, and profile information.

#### - Role-Based Access: There are two user types: Customers (regular users) and Admin/Staff/Superusers (who can manage products and orders).

#### - Conditional Navbar: The navbar dynamically updates depending on whether the user is logged in or out.

## Payments & Checkout
#### - Stripe Integration: Customers can securely pay for their orders using Stripe Payments.

This function creates a Stripe checkout session, specifying payment details, shipping options, and metadata, including the order ID, before redirecting the user to Stripe for secure payment processing.

        # Create Stripe checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            currency="gbp",
            line_items=line_items,
            metadata={'order_id': order.id},
            customer_email=email if email else None,
            shipping_address_collection={"allowed_countries": ["GB"]},
            shipping_options=[{
                "shipping_rate_data": {
                    "display_name": "Standard Shipping, 2-3 Working Days",
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 300, "currency": "gbp"}
                }
            }],
            success_url=request.build_absolute_uri(reverse('payment_success')),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )

        order.stripe_payment_intent = session.id
        order.save()

#### - Webhook Handling: Stripe webhooks are used to validate payments and update order status in real-time.

#### - Order Confirmation: Users receive an order confirmation email after a successful purchase.

#### - Guests can checkout and pay with stripe as a guest, or a logged in user. The email address box is pre-filled when the user is logged in and is required to input when the customer is checking out as a guest.

This part of the checkout function checks if the user is logged in and includes their email if available; if not, it allows them to check out as a guest without an account.

        def checkout(request):
            """Handles the checkout process and creates a Stripe session."""
            
            total = float(request.session.get('total', 0))
        
            if not isinstance(total, (int, float)) or total <= 0:
                return redirect('payment_error')
        
            try:
                bag = Bag(request)
                user = request.user if request.user.is_authenticated else None
                email = request.user.email if request.user.is_authenticated else None

## CRUD Functionality

Logged-in users have full CRUD (Create, Read, Update, Delete) functionality for managing their shopping experience and account details. For example:

#### Create: Users can add products to their shopping bag, create an account, and place orders.

#### Read: Users can browse product details, filter by category or skin type, and view their order history in their profile.

#### Update: Users can edit their account details, adjust product quantities in their shopping bag, and update their shipping information before checkout.

#### Delete: Users can remove items from their shopping bag or request order cancellations (if applicable).

Only admin users have enhanced privileges, such as adding, editing, or deleting products, managing orders, and accessing the Django admin panel to oversee customer transactions.

## Bootstrap 

I used Bootstrap throughout the project to create a responsive, structured, and visually consistent website. Below are the key ways Bootstrap was implemented:

- Navbar: A sticky, responsive navigation bar that collapses on smaller screens and dynamically updates based on user authentication.
- Grid Layout: The Bootstrap grid system (col-md-*) ensures product listings and layouts adjust for different screen sizes.
- Modals: Used for viewing order details without leaving the page.
- Alerts & Messages: Bootstrap alert components provide feedback for actions like user registration and form validation.
- Buttons & Forms: Styled with Bootstrap’s btn and form-control classes to maintain consistency.

#### Example: Bootstrap Modal for Order Details

![BrightonGLOW Logged in User Order Details](/static/images/readme/bgordermodal.png)

# Agile Framework and Planning

To manage my project efficiently, I implemented an Agile development process using GitHub Projects and Issues.

- User Stories & Acceptance Criteria: Each functionality was broken down into User Stories, ensuring clear objectives and usability.

- Prioritisation: Stories were assigned labels such as "Must Have", "Should Have", and "Nice to Have" to focus on the most crucial features first.

- Kanban Workflow: I created a 3-stage board:
To Do – Newly created tasks.
In Progress – Actively being developed.
Done – Completed and tested tasks.

- Automated Tracking: When a new issue was linked to the Brighton Glow Project, it automatically moved into the To Do section. As work progressed, I manually updated its status.

### Examples of User Stories:

##### Front-End: Checkout (Must Have)
As a user, I want to pay for my selected items so that I can complete my purchase.

Acceptance Criteria:

A checkout page displays a summary of the shopping bag and a form for entering payment and shipping details.
Payments are processed securely using Stripe, and the user is shown a confirmation message upon success.

##### Front-End: User Authentication (Must Have)
User Authentication
As a user, I want to create an account and log in.

Acceptance Criteria:

Registration and login pages are functional and validate user input.
Logged-in users see a logout button in the navigation bar.

![BrightonGLOW Agile Planning Examples](/static/images/readme/bgagileplanning.png)

## Wireframes 

# Payments & Stripe Integration

I intregated Stripe into the website, which ensures customers can seamlessly checkout using card payments while maintaining security through webhooks and API keys.

### 1. Setting Up Stripe API Keys

Environment Variables (.env) store sensitive Stripe credentials:
STRIPE_SECRET_KEY=your_secret_key
STRIPE_PUBLIC_KEY=your_public_key
STRIPE_WEBHOOK_SECRET=your_webhook_secret

These keys are loaded in settings.py:

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

### 2. Checkout Process

When a user proceeds to checkout:

- A total order price is retrieved from the session.
- A new order is created in the database (Order model).
- The shopping bag items are converted into Stripe line items.
- A Stripe Checkout Session is created:

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                mode='payment',
                currency="gbp",
                line_items=line_items,
                metadata={'order_id': order.id},
                customer_email=email if email else None,
                success_url=request.build_absolute_uri(reverse('payment_success')),
                cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
            )
The user is then redirected to Stripe’s payment page.

### 3. Webhook for Payment Confirmation

- Stripe sends a webhook event when payment is successful.

The webhook view:
- Validates the event using the Stripe Webhook Secret.
- Extracts the order ID and updates its status to "PAID".
- Sends an email confirmation to the customer.

            if event["type"] == "checkout.session.completed":
                session = event["data"]["object"]
                order_id = session.get('metadata', {}).get('order_id')
                order = Order.objects.get(id=order_id)
                order.status = "PAID"
                order.save()

### 4. Handling Order Completion & Errors
- Success Page: Clears the shopping bag after a successful payment.
- Cancel Page: Marks the order as "CANCELLED" if the user leaves checkout.
- Error Handling: If checkout fails, the user is redirected to an error page.

