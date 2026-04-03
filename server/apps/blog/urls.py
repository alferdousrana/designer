from django.urls import path
from .views import (
    BlogCategoryListPublicAPIView,
    BlogTagListPublicAPIView,
    BlogPostListPublicAPIView,
    FeaturedBlogPostListPublicAPIView,
    BlogPostDetailPublicAPIView,

    BlogCategoryManageAPIView,
    BlogCategoryManageDetailAPIView,
    BlogTagManageAPIView,
    BlogTagManageDetailAPIView,
    BlogPostManageAPIView,
    BlogPostManageDetailAPIView,
    BlogImageManageAPIView,
    BlogImageManageDetailAPIView,
    BlogSectionManageAPIView,
    BlogSectionManageDetailAPIView,
)

urlpatterns = [
    # Public APIs
    path("categories/", BlogCategoryListPublicAPIView.as_view(), name="blog-public-categories"),
    path("tags/", BlogTagListPublicAPIView.as_view(), name="blog-public-tags"),
    path("", BlogPostListPublicAPIView.as_view(), name="blog-public-list"),
    path("featured/", FeaturedBlogPostListPublicAPIView.as_view(), name="blog-public-featured"),
    path("<slug:slug>/", BlogPostDetailPublicAPIView.as_view(), name="blog-public-detail"),

    # Manage APIs
    path("manage/categories/", BlogCategoryManageAPIView.as_view(), name="blog-manage-categories"),
    path("manage/categories/<int:pk>/", BlogCategoryManageDetailAPIView.as_view(), name="blog-manage-category-detail"),

    path("manage/tags/", BlogTagManageAPIView.as_view(), name="blog-manage-tags"),
    path("manage/tags/<int:pk>/", BlogTagManageDetailAPIView.as_view(), name="blog-manage-tag-detail"),

    path("manage/posts/", BlogPostManageAPIView.as_view(), name="blog-manage-posts"),
    path("manage/posts/<int:pk>/", BlogPostManageDetailAPIView.as_view(), name="blog-manage-post-detail"),

    path("manage/gallery/", BlogImageManageAPIView.as_view(), name="blog-manage-gallery"),
    path("manage/gallery/<int:pk>/", BlogImageManageDetailAPIView.as_view(), name="blog-manage-gallery-detail"),

    path("manage/sections/", BlogSectionManageAPIView.as_view(), name="blog-manage-sections"),
    path("manage/sections/<int:pk>/", BlogSectionManageDetailAPIView.as_view(), name="blog-manage-section-detail"),
]