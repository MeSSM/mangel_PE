from django.contrib import admin

from .models import Balance, Points_table, Reward, Request, best_pic, quote

@admin.register(Balance, Points_table, Reward, Request, best_pic, quote)
class admin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
