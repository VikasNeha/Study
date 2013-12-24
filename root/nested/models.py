from django.db import models
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'Country'


class State(models.Model):
    country = models.ForeignKey(Country)
    state_name = models.CharField(max_length=50, blank=False)
    state_abbr = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return self.state_name

    class Meta:
        verbose_name_plural = 'State'


class PRV_Product_Category(models.Model):
    CATEGORY_STATUS = Choices((1, 'ACTIVE'), (0, 'INACTIVE'))

    category_name = models.CharField(max_length=100, blank=False)
    category_description = models.TextField(max_length=500, blank=True)
    category_active = models.IntegerField(choices=CATEGORY_STATUS, default=1)

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'PRV Product Category'


class Buyer(models.Model):
    BUYER_SUB_ALLOW = Choices((1, 'ALLOWED'), (0, 'NOT_ALLOWED'))
    FOR_FREE_STATE = Choices((1, 'YES'), (0, 'NO'))

    buyer_name = models.CharField(max_length=100, blank=False)
    login_link = models.CharField(max_length=400, blank=True)
    register_link = models.CharField(max_length=400, blank=True)
    buyer_intro = models.TextField(blank=True)
    for_free = models.IntegerField(choices=FOR_FREE_STATE, default=0)
    submission_allowed = models.IntegerField(choices=BUYER_SUB_ALLOW, default=1)
    buyer_state = models.ForeignKey(State)
    buyer_country = models.ForeignKey(Country)
    prod_category = models.ManyToManyField(PRV_Product_Category, related_name='buyer_prod_category')

    def __unicode__(self):
        return self.buyer_name

    class Meta:
        verbose_name_plural = 'Buyer'


class BuyerSellCode(models.Model):
    buyer = models.ForeignKey(Buyer)
    CATEGORY_OF_CODE_CHOICES = Choices("NAICS", "UNSPC", "SIC")
    category_of_code = models.CharField(choices=CATEGORY_OF_CODE_CHOICES, max_length=10)
    TYPE_OF_CODE_CHOICES = Choices("BUY", "SELL")
    type_of_code = models.CharField(choices=TYPE_OF_CODE_CHOICES, max_length=10)
    code = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Buyer Sell Code'


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='media/avatar', blank=True, null=True)

    def __unicode__(self):
        return self.supplier_name

    class Meta:
        verbose_name_plural = 'Supplier'


class SupplierSubmission(models.Model):
    supplier = models.ForeignKey(Supplier)
    buyer = models.ForeignKey(Buyer, related_name='submitted_buyer')
    submission_date = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.supplier.supplier_name

    class Meta:
        verbose_name_plural = 'Supplier Submission'


#============== Models for supplier info page =======================

class Section(models.Model):
    section_name = models.CharField(max_length=25)
    display_order = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.section_name

    class Meta:
        verbose_name_plural = 'Section'


class FieldMetaInfo(models.Model):
    field_name = models.CharField(max_length=50)
    section = models.ForeignKey(Section)
    FIELD_TYPE = Choices("Text", "image", "Date","Checkbox", "Email", "textarea", "select", "multi-select", "radio", "file")
    field_type = models.CharField(choices=FIELD_TYPE, max_length=25)
    DEPENDENT = Choices((0,'No'), (1,'Yes'))
    is_dependent = models.IntegerField(choices=DEPENDENT, default=0)
    dependent_field = models.ForeignKey('self',null=True,blank=True)
    options = models.CharField(max_length=200,blank=True)
    display_order = models.IntegerField()

    def __unicode__(self):
        return self.field_name

    class Meta:
        verbose_name_plural = 'FieldMetaInfo'


class BuyerAdditionalField(models.Model):
    field_name = models.CharField(max_length=50)
    section = models.ForeignKey(Section)
    FIELD_TYPE = Choices("Text","Date","Checkbox", "Email", "Textarea")
    field_type = models.CharField(choices=FIELD_TYPE, max_length=25)
    DEPENDENT = Choices((0,'No'), (1,'Yes'))
    is_dependent = models.IntegerField(choices=DEPENDENT, default=0)
    dependent_field = models.ForeignKey('self',null=True,blank=True)
    options = models.CharField(max_length=200,blank=True)
    display_order = models.IntegerField()
    buyer = models.ForeignKey(Buyer)
    REQUIRED = Choices((0,'No'), (1,'Yes'))
    is_required = models.IntegerField(choices=REQUIRED, default=0)

    def __unicode__(self):
        return self.buyer.buyer_name + " / " + self.field_name

    class Meta:
        verbose_name_plural = 'BuyerAdditionalField'


class BuyerCommonField(models.Model):
    buyer = models.ForeignKey(Buyer)
    field = models.ForeignKey(FieldMetaInfo)
    REQUIRED = Choices((0,'No'), (1,'Yes'))
    is_required = models.IntegerField(choices=REQUIRED, default=0)

    def __unicode__(self):
        return self.buyer.buyer_name + "/"+ self.field.field_name

    class Meta:
        verbose_name_plural = 'BuyerCommonField'


class AdditionalFieldData(models.Model):
    supplier = models.ForeignKey(Supplier)
    field = models.ForeignKey(BuyerAdditionalField)
    field_value = models.CharField(max_length=200)

    def __unicode__(self):
        return self.field.field_name

    class Meta:
        verbose_name_plural = 'AdditionalFieldData'


class SupplierInfo(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    add1 = models.NullBooleanField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='avatar/', blank=True, null=True)
    attachment = models.FileField(upload_to='attachment/', blank=True, null=True)

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'SupplierInfo'




