from django.contrib import admin

from .models import Bid, Listing,WatchList, Comment, User
# Register your models here.

admin.site.register(Bid)
admin.site.register(WatchList)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Listing)
