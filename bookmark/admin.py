from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.

# 데코레이터 패턴을 사용하지 않는 방법
# admin.site.register(Bookmark, BookmarkAdmin)


# 위에 코드와 아래 @, class랑 동일
@admin.register(Bookmark)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

