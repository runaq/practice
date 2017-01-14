from django.contrib import admin
from .models import Post, Comment, Color

class PostAdmin(admin.ModelAdmin):
	list_filter = ('color',)
	list_display = ('title', 'color','image_img', 'published_date', )

	
class ColorAdmin(admin.ModelAdmin):
	search_fields = ('name_color', )
	
admin.site.register(Post, PostAdmin)
radio_fields = {"choises": admin.HORIZONTAL}
admin.site.register(Comment)
admin.site.register(Color,  ColorAdmin)

