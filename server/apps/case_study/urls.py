from django.urls import path
from .views import (
    CaseStudyListPublicAPIView,
    FeaturedCaseStudyListPublicAPIView,
    CaseStudyDetailPublicAPIView,
    CaseStudyManageAPIView,
    CaseStudyManageDetailAPIView,
    CaseStudyImageManageAPIView,
    CaseStudyImageManageDetailAPIView,
    CaseStudySectionManageAPIView,
    CaseStudySectionManageDetailAPIView,
    CaseStudyMetricManageAPIView,
    CaseStudyMetricManageDetailAPIView,
)

urlpatterns = [
    # Public APIs
    path("", CaseStudyListPublicAPIView.as_view(), name="case-study-public-list"),
    path("featured/", FeaturedCaseStudyListPublicAPIView.as_view(), name="case-study-public-featured"),
    path("<slug:slug>/", CaseStudyDetailPublicAPIView.as_view(), name="case-study-public-detail"),

    # Manage APIs
    path("manage/case-studies/", CaseStudyManageAPIView.as_view(), name="case-study-manage-list-create"),
    path("manage/case-studies/<int:pk>/", CaseStudyManageDetailAPIView.as_view(), name="case-study-manage-detail"),

    path("manage/gallery/", CaseStudyImageManageAPIView.as_view(), name="case-study-manage-gallery"),
    path("manage/gallery/<int:pk>/", CaseStudyImageManageDetailAPIView.as_view(), name="case-study-manage-gallery-detail"),

    path("manage/sections/", CaseStudySectionManageAPIView.as_view(), name="case-study-manage-sections"),
    path("manage/sections/<int:pk>/", CaseStudySectionManageDetailAPIView.as_view(), name="case-study-manage-section-detail"),

    path("manage/metrics/", CaseStudyMetricManageAPIView.as_view(), name="case-study-manage-metrics"),
    path("manage/metrics/<int:pk>/", CaseStudyMetricManageDetailAPIView.as_view(), name="case-study-manage-metric-detail"),
]