from django.contrib import admin
from .models import Post, Tag, Comment, PostLike, PostTag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_tag', 'date_add', 'active')
    readonly_fields = ['img_tag']
    list_filter = ('date_add', 'title', 'active')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('date_add', 'post', 'author', 'text', 'img_tag', 'active')
    readonly_fields = ['img_tag']
    list_filter = ('date_add', 'post', 'author', 'active')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostLike)
admin.site.register(PostTag)
