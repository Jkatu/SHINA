from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("new_series", views.new_series, name="series-create"),
    path("new_post", views.new_post, name="post-create"),
    path("<series>", views.series, name="series"),
    path("<series>/update", views.series_update, name="series_update"),
    path("<series>/delete", views.series_delete, name="series_delete"),
    path("<series>/<article>", views.article, name="article"),
    path("<series>/<article>/update", views.article_update, name="article_update"),
    path("<series>/<article>/delete", views.article_delete, name="article_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)