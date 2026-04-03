from django.urls import path
from .views import (
    CategoryListPublicAPIView,
    ProjectTagListPublicAPIView,
    ProjectListPublicAPIView,
    FeaturedProjectListPublicAPIView,
    ProjectDetailPublicAPIView,

    CategoryManageAPIView,
    CategoryManageDetailAPIView,
    ProjectTagManageAPIView,
    ProjectTagManageDetailAPIView,
    ProjectManageAPIView,
    ProjectManageDetailAPIView,
    ProjectImageManageAPIView,
    ProjectImageManageDetailAPIView,
    ProjectSectionManageAPIView,
    ProjectSectionManageDetailAPIView,
    ProjectMetricManageAPIView,
    ProjectMetricManageDetailAPIView,
)

urlpatterns = [
    # Public APIs
    path("categories/", CategoryListPublicAPIView.as_view(), name="project-public-categories"),
    path("tags/", ProjectTagListPublicAPIView.as_view(), name="project-public-tags"),
    path("", ProjectListPublicAPIView.as_view(), name="project-public-list"),
    path("featured/", FeaturedProjectListPublicAPIView.as_view(), name="project-public-featured"),
    path("<slug:slug>/", ProjectDetailPublicAPIView.as_view(), name="project-public-detail"),

    # Manage APIs
    path("manage/categories/", CategoryManageAPIView.as_view(), name="project-manage-categories"),
    path("manage/categories/<int:pk>/", CategoryManageDetailAPIView.as_view(), name="project-manage-category-detail"),

    path("manage/tags/", ProjectTagManageAPIView.as_view(), name="project-manage-tags"),
    path("manage/tags/<int:pk>/", ProjectTagManageDetailAPIView.as_view(), name="project-manage-tag-detail"),

    path("manage/projects/", ProjectManageAPIView.as_view(), name="project-manage-projects"),
    path("manage/projects/<int:pk>/", ProjectManageDetailAPIView.as_view(), name="project-manage-project-detail"),

    path("manage/gallery/", ProjectImageManageAPIView.as_view(), name="project-manage-gallery"),
    path("manage/gallery/<int:pk>/", ProjectImageManageDetailAPIView.as_view(), name="project-manage-gallery-detail"),

    path("manage/sections/", ProjectSectionManageAPIView.as_view(), name="project-manage-sections"),
    path("manage/sections/<int:pk>/", ProjectSectionManageDetailAPIView.as_view(), name="project-manage-section-detail"),

    path("manage/metrics/", ProjectMetricManageAPIView.as_view(), name="project-manage-metrics"),
    path("manage/metrics/<int:pk>/", ProjectMetricManageDetailAPIView.as_view(), name="project-manage-metric-detail"),
]