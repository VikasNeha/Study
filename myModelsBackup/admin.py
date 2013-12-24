from django.contrib import admin

from prv.models import *


class BuyerSellCodeInLine(admin.TabularInline):
    model = BuyerSellCode
    extra = 1


class BuyerCommomFieldInLine(admin.TabularInline):
    model = BuyerCommonField
    extra = 1


class BuyerAdmin(admin.ModelAdmin):
    inlines = [BuyerSellCodeInLine, BuyerCommomFieldInLine]


class SupplierSubmissionInLine(admin.StackedInline):
    model = SupplierSubmission
    extra = 0


class SupplierAdmin(admin.ModelAdmin):
    inlines = [SupplierSubmissionInLine]

admin.site.register(Country)
admin.site.register(State)
admin.site.register(PRV_Product_Category)

admin.site.register(Buyer, BuyerAdmin)
#admin.site.register(BuyerSellCode)
admin.site.register(Supplier, SupplierAdmin)
#admin.site.register(SupplierSubmission)

# models for supplier info page

admin.site.register(Section)
admin.site.register(FieldMetaInfo)
admin.site.register(BuyerAdditionalField)
admin.site.register(BuyerCommonField)
admin.site.register(AdditionalFieldData)
admin.site.register(SupplierInfo)
