from django.contrib import admin
from .models import Problem,Product,Company, DatabaseCredential
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("id",)
        form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
        return form

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("id",)
        form = super(ProblemAdmin, self).get_form(request, obj, **kwargs)
        return form

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("id",)
        form = super(CompanyAdmin, self).get_form(request, obj, **kwargs)
        return form

@admin.register(DatabaseCredential)
class DatabaseCredentialAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("id",)
        form = super(DatabaseCredentialAdmin, self).get_form(request, obj, **kwargs)
        return form



