from django.contrib import admin

from .models import Subscriptions, User

admin.site.unregister(User)
@admin.register(User)
class UsersProfile(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', )
    list_filter = ('username', 'email',)


@admin.register(Subscriptions)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "author",
    )
