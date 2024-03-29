from django.db import models
from store.models import product,Variation

# Create your models here.
class Cart(models.Model):
  cart_id=models.CharField(max_length=255,blank=True)
  date_added=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.cart_id
class CartItem(models.Model):
  Product=models.ForeignKey(product, on_delete=models.CASCADE)
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  quantity=models.IntegerField()
  is_active=models.BooleanField(default=True)
  variations=models.ManyToManyField(Variation,blank=True)
  
  def sub_total(self):
    return self.Product.price * self.quantity

  def __unicode__(self):
    return self.Product
