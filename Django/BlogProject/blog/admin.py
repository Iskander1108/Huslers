from django.contrib import admin
from .models import Post, Category, Comment, Tag, Author
from django.utils.safestring import mark_safe


# admin.site.register(Post)
# admin.site.register(Category) 

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ "get_image","id", "title", "category", "discription", "location", "created_at" ]
    search_fields = ["id", "title", "discription", "location"]
    list_filter = ["category", "created_at"]
    
    inlines = [CommentInline]
    
    
   
    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        else:
            return "Not image"
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    search_fields = ["id", "title"]
    list_filter = ["created_at"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "created_at"]
    search_fields = ["id", "first_name", "last_name", "email"]
    list_filter = ["created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ "post","id", "author", "content", "created_at"]
    search_fields = ["id", "post", "author", "content"]
    list_filter = ["created_at"]
    raw_id_fields = ["post", "author"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at"]
    search_fields = ["id", "name"]
    list_filter = ["created_at"]

# from .models import News, Comments



# admin.site.register(News)
# admin.site.register(Comments)

