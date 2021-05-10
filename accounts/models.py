from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name

class Product(models.Model):
	CATEGORY = (
			('Vegitables', 'Vegitables'),
			('Grains', 'Grains'),
			('Fruits','Fruits'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.DecimalField(max_digits=7, decimal_places = 2)
	image = models.ImageField(null=True, blank=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	# description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# tags = models.ManyToManyField(Tag, null = True)
	
	

	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	# product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	# note = models.CharField(max_length=1000, null=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

	@property
	def shipping(self):
		shipping = True
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			pass
		return shipping

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True, blank = True)
	order = models.ForeignKey(Order, blank = True, null=True, on_delete= models.SET_NULL)
	quantity = models.IntegerField(default = 0,null = True, blank = True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAdress(models.Model):

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	order = models.ForeignKey(Order, blank = True, null=True, on_delete= models.SET_NULL)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=False, blank=True)
	zipcode = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.address




	
