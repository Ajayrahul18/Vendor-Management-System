from django.db import models

# Create your models here.
class VendorDetals(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    contact_detail = models.TextField(max_length=200, default='', blank=False)
    addres = models.TextField(max_length=200, default='', blank=False)
    vendor_code = models.CharField(max_length=50, default='', blank=False, unique=True)
    on_time_delivery_rate = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    quality_rating_average = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    average_response_time = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    po_number = models.CharField(max_length=50, default='', blank=False, unique=True)
    vendor = models.ForeignKey(VendorDetals, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    item = models.CharField(max_length=50, default='', blank=False)
    quantity = models.IntegerField(default='', blank=False)
    status = models.CharField(max_length=50, default='', blank=False)
    quantity_rating = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    issue_date = models.DateField()
    acknowledgment_date = models.DateField()

    def __str__(self):
        return self.item

class Performance(models.Model):
    vendor = models.ForeignKey(VendorDetals, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    quality_rating_average = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)
    fulfillment_rate = models.DecimalField(max_digits=7,decimal_places=2, default=0.00, blank=False)

    def __str__(self):
        return (f'{self.vendor} : {self.date}')
    