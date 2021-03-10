from django.db import models
from django.core.validators import MaxValueValidator
from model_utils.models import TimeStampedModel
#
from apps.accounts.models import User
from .managers import *
from .constants import TYPE_SALE_CHOICES, TYPE_PAYMENT_CHOICES


class Size (models.Model):
    value = models.PositiveSmallIntegerField('Value', validators=[MaxValueValidator(99)], unique=True)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return  str(self.id) +' - '+str(self.value)


class Tax (models.Model):
    name = models.CharField('Name', max_length=10, unique=True)
    value = models.DecimalField('Value', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxs'

    def __str__(self):
        return  str(self.id) +' - '+str(self.name)+ ' - '+str(self.value)


class Brand (models.Model):
    name = models.CharField('Name', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return  str(self.id) +' - '+self.name


class Model (models.Model):
    name = models.CharField('Name', max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        unique_together = ['name', 'brand']

    def __str__(self):
            return  str(self.id) +' - '+self.name+' - '+self.brand.name


class Product (TimeStampedModel):
    barcode = models.CharField('Barcode', primary_key=True, max_length=15, unique=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Model')
    desc = models.CharField('Description', max_length=150, blank=True, null=True)
    purchase_price = models.DecimalField('Purchase Price', max_digits=5, decimal_places=2)
    sale_price = models.DecimalField('Sale Price', max_digits=5, decimal_places=2)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax')
    out_stock = models.BooleanField('Out_Stock', default=False)
    #
    objects = ProductManager

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created']

    def __str__(self):
        return  '['+self.barcode+'] ' +self.model.name +' - '+self.model.brand.name+' ('+str(self.sale_price)+' €)' 


class Item (TimeStampedModel):
    reference = models.CharField('Reference', primary_key=True, max_length=15, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Size')
    heigth = models.DecimalField('Heigth', max_digits=5,  decimal_places=2, blank=True, null=True)
    width = models.DecimalField('Width', max_digits=5, decimal_places=2, blank=True, null=True)
    weigth = models.DecimalField('weigth', max_digits=5, decimal_places=2, blank=True, null=True)
    sold = models.BooleanField('Sold', default=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['-created']

    def __str__(self):
        return  '['+self.reference+'] '+ self.product.model.name +' - '+self.product.model.brand.name+' ('+str(self.size)+') '+'sold='+str(self.sold) 


class Sale (TimeStampedModel):
    type_sale = models.CharField(verbose_name='Type Sale', max_length=20, choices=TYPE_SALE_CHOICES)
    type_payment = models.CharField('Type Payment', max_length=20, choices=TYPE_PAYMENT_CHOICES)
    amount = models.DecimalField('Amount', max_digits=12, decimal_places=2)
    count = models.PositiveSmallIntegerField('Count', validators=[MaxValueValidator(999)])
    closed = models.BooleanField('Closed', default=False)
    anulated = models.BooleanField('Anulated', default=False)
    user_employee = models.ForeignKey(User, related_name='sale_userEmployee', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Employee')
    user_client = models.ForeignKey(User, related_name='sale_userClient', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Client')

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['-created']

    def __str__(self):
        return  '['+str(self.id)+'] '+self.type_payment +' - '+self.type_sale+' ('+str(self.amount)+':'+str(self.count)+') '+'closed='+str(self.closed) 


class SaleItem (models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Sale')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name='Item')

    class Meta:
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'

    def __str__(self):
        return '[Sale id:'+str(self.sale.id)+'] - [Item id:'+str(self.item.reference)+']'


class SaleSend (models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, verbose_name='Sale')
    addres = models.CharField('Addres', max_length=300)
    cp = models.CharField('C.P', max_length=10)
    city = models.CharField('City', max_length=50)
    country = models.CharField('Country', max_length=50)
    phone = models.CharField('Phone', max_length=15)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = 'Sale Send'
        verbose_name_plural = 'Sale Sends'

    def __str__(self):
        return '[Sale id:'+str(self.sale.id)+'] - [Send id:'+str(self.id)+']'