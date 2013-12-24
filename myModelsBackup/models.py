from django.db import models
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from django.contrib.auth.models import User
from datetime import date

# Create your models here.



#============== Models for supplier info page =======================

class SupplierInfo(models.Model):
    #============ COMPANY INFORMATION ==============#
    COMP_NAME = models.CharField(max_length=200, blank=True, verbose_name='Legal Company Name')
    COMP_DBA_NAME = models.CharField(max_length=200, blank=True, verbose_name='DBA Company Name')
    COMP_FED_TAX = models.CharField(max_length=50, blank=True, verbose_name='Federal Tax ID')
    COMP_DUNN_STREET = models.CharField(max_length=50, blank=True, verbose_name='Dunn & Brad Street Number')

    #=========== ADDRESS SECTION ============#
    PHYSICAL_ADDRESS = models.CharField(max_length=500, blank=True, verbose_name='Physical Address')
    PHYSICAL_ADDRESS_CITY = models.CharField(max_length=500, blank=True, verbose_name='City')
    PHYSICAL_ADDRESS_STATE = models.CharField(max_length=50, blank=True, verbose_name='State')
    PHYSICAL_ADDRESS_COUNTY = models.CharField(max_length=50, blank=True, verbose_name='County')
    PHYSICAL_ADDRESS_COUNTRY = models.CharField(max_length=50, blank=True, verbose_name='Country')
    PHYSICAL_ADDRESS_ZIP = models.CharField(max_length=50, blank=True, verbose_name='Zip/Postal Code')

    REMITTANCE_ADDRESS = models.CharField(max_length=500, blank=True, verbose_name='Remittance Address')
    REMITTANCE_ADDRESS_CITY = models.CharField(max_length=500, blank=True, verbose_name='City')
    REMITTANCE_ADDRESS_STATE = models.CharField(max_length=50, blank=True, verbose_name='State')
    REMITTANCE_ADDRESS_COUNTY = models.CharField(max_length=50, blank=True, verbose_name='County')
    REMITTANCE_ADDRESS_COUNTRY = models.CharField(max_length=50, blank=True, verbose_name='Country')
    REMITTANCE_ADDRESS_ZIP = models.CharField(max_length=50, blank=True, verbose_name='Zip/Postal Code')

    MAILING_ADDRESS = models.CharField(max_length=500, blank=True, verbose_name='Mailing Address')
    MAILING_ADDRESS_CITY = models.CharField(max_length=500, blank=True, verbose_name='City')
    MAILING_ADDRESS_STATE = models.CharField(max_length=50, blank=True, verbose_name='State')
    MAILING_ADDRESS_COUNTY = models.CharField(max_length=50, blank=True, verbose_name='County')
    MAILING_ADDRESS_COUNTRY = models.CharField(max_length=50, blank=True, verbose_name='Country')
    MAILING_ADDRESS_ZIP = models.CharField(max_length=50, blank=True, verbose_name='Zip/Postal Code')

    COMP_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Company Phone Number')
    COMP_FAX = models.CharField(max_length=20, blank=True, verbose_name='Company Fax Number')
    COMP_URL = models.CharField(max_length=100, blank=True, verbose_name='Company Website (URL)')

    #============== OWNER INFORMATION =============#
    OWNER1_NAME = models.CharField(max_length=100, blank=True, verbose_name='Owner 1 Name', null=True)
    OWNER1_TITLE = models.CharField(max_length=100, blank=True, verbose_name='Owner 1 Title')
    OWNER1_EMAIL = models.EmailField(blank=True, verbose_name='Owner 1 E-Mail')
    OWNER1_GENDER = models.CharField(max_length=10, blank=True, verbose_name='Owner 1 Gender')
    OWNER1_ETHNICITY = models.CharField(max_length=50, blank=True, verbose_name='Owner 1 Ethnicity')
    OWNER1_PERCENT_OWNERSHIP = models.IntegerField(blank=True, verbose_name='Owner 1 % Ownership', null=True)

    OWNER2_NAME = models.CharField(max_length=100, blank=True, verbose_name='Owner 2 Name')
    OWNER2_TITLE = models.CharField(max_length=100, blank=True, verbose_name='Owner 2 Title')
    OWNER2_EMAIL = models.EmailField(blank=True, verbose_name='Owner 2 E-Mail')
    OWNER2_GENDER = models.CharField(max_length=10, blank=True, verbose_name='Owner 2 Gender')
    OWNER2_ETHNICITY = models.CharField(max_length=50, blank=True, verbose_name='Owner 2 Ethnicity')
    OWNER2_PERCENT_OWNERSHIP = models.IntegerField(blank=True, verbose_name='Owner 2 % Ownership', null=True)

    OWNER3_NAME = models.CharField(max_length=100, blank=True, verbose_name='Owner 3 Name')
    OWNER3_TITLE = models.CharField(max_length=100, blank=True, verbose_name='Owner 3 Title')
    OWNER3_EMAIL = models.EmailField(blank=True, verbose_name='Owner 3 E-Mail')
    OWNER3_GENDER = models.CharField(max_length=10, blank=True, verbose_name='Owner 3 Gender')
    OWNER3_ETHNICITY = models.CharField(max_length=50, blank=True, verbose_name='Owner 3 Ethnicity')
    OWNER3_PERCENT_OWNERSHIP = models.IntegerField(blank=True, verbose_name='Owner 3 % Ownership', null=True)

    #========= CONTACT INFORMATION =============#
    PRIMARY_CONT_NAME = models.CharField(max_length=100, blank=True, verbose_name='Primary Contact Name')
    PRIMARY_CONT_TITLE = models.CharField(max_length=50, blank=True, verbose_name='Job Title')
    PRIMARY_CONT_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    PRIMARY_CONT_PHONE_EXT = models.CharField(max_length=20, blank=True, verbose_name='Phone Ext.')
    PRIMARY_CONT_FAX = models.CharField(max_length=20, blank=True, verbose_name='Fax Number')
    PRIMARY_CONT_EMAIL = models.EmailField(blank=True, verbose_name='E-Mail Address')

    SECONDARY_CONT_NAME = models.CharField(max_length=100, blank=True, verbose_name='Secondary Contact Name')
    SECONDARY_CONT_TITLE = models.CharField(max_length=50, blank=True, verbose_name='Job Title')
    SECONDARY_CONT_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    SECONDARY_CONT_PHONE_EXT = models.CharField(max_length=20, blank=True, verbose_name='Phone Ext.')
    SECONDARY_CONT_FAX = models.CharField(max_length=20, blank=True, verbose_name='Fax Number')
    SECONDARY_CONT_EMAIL = models.EmailField(blank=True, verbose_name='E-Mail Address')

    #============= BUSINESS BIOGRAPHY ================#
    IS_COMP_PUBLICLY_TRADED = models.NullBooleanField(verbose_name='Is your company publicly traded?')
    STOCK_TICKET_ID = models.CharField(max_length=50, blank=True, verbose_name='Stock Ticket ID')
    NUM_OF_EMPLOYEES = models.CharField(max_length=10, blank=True, verbose_name='Number Of Employees')
    YEAR_BUSINESS_ESTABLISHED = models.CharField(max_length=4, blank=True, verbose_name='Year Business was Established')
    GEO_AREA_INTERNATIONAL = models.NullBooleanField(verbose_name='Geographical Service Ares: International')
    GEO_AREA_NATIONAL = models.NullBooleanField(verbose_name='Geographical Service Ares: National')
    GEO_AREA_LOCAL = models.NullBooleanField(verbose_name='Geographical Service Ares: Local')
    GEO_AREA_REGIONAL = models.NullBooleanField(verbose_name='Geographical Service Ares: Regional')
    ANNUAL_SALES_LASTYEAR = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                verbose_name='Annual Sales For ' + str(date.today().year - 1))
    ANNUAL_SALES_TWOYEARSAGO = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                   verbose_name='Annual Sales For ' + str(date.today().year - 2))
    ANNUAL_SALES_THREEYEARSAGO = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                     verbose_name='Annual Sales For ' + str(date.today().year - 3))
    PRODUCT_SERVICE_DESC = models.CharField(max_length=500, blank=True,
                                            verbose_name='Describe the Products/Services your company provides')

    #========== BUSINESS REFERENCES ==============#
    REF1_COMP_NAME = models.CharField(max_length=100, blank=True, verbose_name='Reference 1 Company Name')
    REF1_CONTACT_NAME = models.CharField(max_length=100, blank=True, verbose_name='Contact Name')
    REF1_SERVICES_PROVIDED = models.CharField(max_length=50, blank=True, verbose_name='Services Provided')
    REF1_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Phone')
    REF1_EMAIL = models.EmailField(blank=True, verbose_name='Email')

    REF2_COMP_NAME = models.CharField(max_length=100, blank=True, verbose_name='Reference 2 Company Name')
    REF2_CONTACT_NAME = models.CharField(max_length=100, blank=True, verbose_name='Contact Name')
    REF2_SERVICES_PROVIDED = models.CharField(max_length=50, blank=True, verbose_name='Services Provided')
    REF2_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Phone')
    REF2_EMAIL = models.EmailField(blank=True, verbose_name='Email')
    
    REF3_COMP_NAME = models.CharField(max_length=100, blank=True, verbose_name='Reference 3 Company Name')
    REF3_CONTACT_NAME = models.CharField(max_length=100, blank=True, verbose_name='Contact Name')
    REF3_SERVICES_PROVIDED = models.CharField(max_length=50, blank=True, verbose_name='Services Provided')
    REF3_PHONE = models.CharField(max_length=20, blank=True, verbose_name='Phone')
    REF3_EMAIL = models.EmailField(blank=True, verbose_name='Email')

    #========== E-BUSINESS READINESS ==========#
    HAS_ONLINE_CATALOG = models.NullBooleanField(verbose_name='Does your company have an online catalog?')

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'SupplierInfo'




