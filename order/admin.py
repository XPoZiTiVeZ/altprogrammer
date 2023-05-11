from django.contrib import admin
from .models import Services, Orders, Chats, ChatMessages

admin.site.register(Services)
admin.site.register(Orders)
admin.site.register(Chats)
admin.site.register(ChatMessages)