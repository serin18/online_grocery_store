from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    discount = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class UserProfileTable(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
   
    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.TextField(default={'objects': []}, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
ORDERSTATUS = ((1, "Pending"), (2, "Dispatch"), (3, "On the way"), (4, "Delivered"), (5, "Cancel"), (6, "Return"))
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.TextField(default={'objects': []}, null=True, blank=True)
    total = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=ORDERSTATUS, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
STATUS = ((1, "Read"), (2, "Unread"))
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
# class DeliveryBoy(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=100, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     image = models.FileField(null=True, blank=True)
#     availability = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.user.username

# class DeliveryTask(models.Model):
#     delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
#     booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
#     assigned_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
#     status = models.IntegerField(choices=ORDERSTATUS, default=1)
#     location_latitude = models.FloatField(null=True, blank=True)
#     location_longitude = models.FloatField(null=True, blank=True)
#     delivery_proof = models.FileField(null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.delivery_boy.user.username} - {self.booking}"
    
# class DeliveryCommunication(models.Model):
#     delivery_task = models.ForeignKey(DeliveryTask, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
#     message = models.TextField(null=True, blank=True)
#     sent_at = models.DateTimeField(auto_now_add=True)
#     read_at = models.DateTimeField(null=True, blank=True)
    
#     def __str__(self):
#         return f"From {self.sender.username} to {self.recipient.username} - {self.sent_at}"

# class DeliverySchedule(models.Model):
#     delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     available_hours = models.CharField(max_length=100, null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.delivery_boy.user.username} - {self.start_date} to {self.end_date}"

# class DeliveryPerformance(models.Model):
#     delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
#     total_deliveries = models.IntegerField(default=0)
#     successful_deliveries = models.IntegerField(default=0)
#     rating = models.FloatField(default=0)

    
#     def __str__(self):
#         return self.delivery_boy.user.username






