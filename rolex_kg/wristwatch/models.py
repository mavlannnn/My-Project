from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Watch(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='watch_images/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} - {self.model}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Watch)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"


class Rating(models.Model):
    product = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(Watch, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], help_text="Rate the item with 0 to 6 stars")

    def __str__(self):
        return f"{self.product} - {self.user} - {self.stars} stars"


class Review(models.Model):
    author = models.CharField(max_length=16)
    test = models.TextField()
    product = models.ForeignKey(Brand, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.test}'


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    available_items = models.ManyToManyField(Watch)
    sales_history = models.ManyToManyField(Order)

    def __str__(self):
        return self.store_name
