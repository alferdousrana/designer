from django.urls import path
from .views import (
    HomePageAPIView,
    HeroSectionPublicAPIView,
    AboutSectionPublicAPIView,
    SkillListPublicAPIView,
    ServiceListPublicAPIView,
    TestimonialListPublicAPIView,
    FeaturedTestimonialListPublicAPIView,
    SocialLinkListPublicAPIView,
    ContactInfoPublicAPIView,
    ContactMessageCreateAPIView,

    HeroSectionManageAPIView,
    HeroSectionManageDetailAPIView,
    AboutSectionManageAPIView,
    AboutSectionManageDetailAPIView,
    SkillManageAPIView,
    SkillManageDetailAPIView,
    ServiceManageAPIView,
    ServiceManageDetailAPIView,
    TestimonialManageAPIView,
    TestimonialManageDetailAPIView,
    SocialLinkManageAPIView,
    SocialLinkManageDetailAPIView,
    ContactInfoManageAPIView,
    ContactInfoManageDetailAPIView,
    ContactMessageManageAPIView,
    ContactMessageManageDetailAPIView,
)

urlpatterns = [
    # Public APIs
    path("home/", HomePageAPIView.as_view(), name="core-home"),
    path("hero/", HeroSectionPublicAPIView.as_view(), name="core-hero"),
    path("about/", AboutSectionPublicAPIView.as_view(), name="core-about"),
    path("skills/", SkillListPublicAPIView.as_view(), name="core-skills"),
    path("services/", ServiceListPublicAPIView.as_view(), name="core-services"),
    path("testimonials/", TestimonialListPublicAPIView.as_view(), name="core-testimonials"),
    path("testimonials/featured/", FeaturedTestimonialListPublicAPIView.as_view(), name="core-featured-testimonials"),
    path("social-links/", SocialLinkListPublicAPIView.as_view(), name="core-social-links"),
    path("contact-info/", ContactInfoPublicAPIView.as_view(), name="core-contact-info"),
    path("contact/", ContactMessageCreateAPIView.as_view(), name="core-contact-message-create"),

    # Manage APIs
    path("manage/hero/", HeroSectionManageAPIView.as_view(), name="manage-hero-list-create"),
    path("manage/hero/<int:pk>/", HeroSectionManageDetailAPIView.as_view(), name="manage-hero-detail"),

    path("manage/about/", AboutSectionManageAPIView.as_view(), name="manage-about-list-create"),
    path("manage/about/<int:pk>/", AboutSectionManageDetailAPIView.as_view(), name="manage-about-detail"),

    path("manage/skills/", SkillManageAPIView.as_view(), name="manage-skills-list-create"),
    path("manage/skills/<int:pk>/", SkillManageDetailAPIView.as_view(), name="manage-skills-detail"),

    path("manage/services/", ServiceManageAPIView.as_view(), name="manage-services-list-create"),
    path("manage/services/<int:pk>/", ServiceManageDetailAPIView.as_view(), name="manage-services-detail"),

    path("manage/testimonials/", TestimonialManageAPIView.as_view(), name="manage-testimonials-list-create"),
    path("manage/testimonials/<int:pk>/", TestimonialManageDetailAPIView.as_view(), name="manage-testimonials-detail"),

    path("manage/social-links/", SocialLinkManageAPIView.as_view(), name="manage-social-links-list-create"),
    path("manage/social-links/<int:pk>/", SocialLinkManageDetailAPIView.as_view(), name="manage-social-links-detail"),

    path("manage/contact-info/", ContactInfoManageAPIView.as_view(), name="manage-contact-info-list-create"),
    path("manage/contact-info/<int:pk>/", ContactInfoManageDetailAPIView.as_view(), name="manage-contact-info-detail"),

    path("manage/contact-messages/", ContactMessageManageAPIView.as_view(), name="manage-contact-messages"),
    path("manage/contact-messages/<int:pk>/", ContactMessageManageDetailAPIView.as_view(), name="manage-contact-message-detail"),
]