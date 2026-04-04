from django.urls import path
from .views import (
    HomePageAPIView,
    HeroSectionPublicAPIView,
    AboutSectionPublicAPIView,
    BrandLogoListPublicAPIView,
    SkillListPublicAPIView,
    ExperienceSectionPublicAPIView,
    ExperienceItemListPublicAPIView,
    TestimonialsSectionPublicAPIView,
    TestimonialListPublicAPIView,
    FeaturedTestimonialListPublicAPIView,
    ProjectsShowcaseSectionPublicAPIView,
    BlogSectionPublicAPIView,
    ContactSectionPublicAPIView,
    SocialLinkListPublicAPIView,
    ContactInfoPublicAPIView,
    ContactMessageCreateAPIView,

    HeroSectionManageAPIView,
    HeroSectionManageDetailAPIView,
    AboutSectionManageAPIView,
    AboutSectionManageDetailAPIView,
    BrandLogoManageAPIView,
    BrandLogoManageDetailAPIView,
    SkillManageAPIView,
    SkillManageDetailAPIView,
    ExperienceSectionManageAPIView,
    ExperienceSectionManageDetailAPIView,
    ExperienceItemManageAPIView,
    ExperienceItemManageDetailAPIView,
    TestimonialsSectionManageAPIView,
    TestimonialsSectionManageDetailAPIView,
    TestimonialManageAPIView,
    TestimonialManageDetailAPIView,
    ProjectsShowcaseSectionManageAPIView,
    ProjectsShowcaseSectionManageDetailAPIView,
    BlogSectionManageAPIView,
    BlogSectionManageDetailAPIView,
    ContactSectionManageAPIView,
    ContactSectionManageDetailAPIView,
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
    path("brand-logos/", BrandLogoListPublicAPIView.as_view(), name="core-brand-logos"),
    path("skills/", SkillListPublicAPIView.as_view(), name="core-skills"),
    path("experience-section/", ExperienceSectionPublicAPIView.as_view(), name="core-experience-section"),
    path("experience-items/", ExperienceItemListPublicAPIView.as_view(), name="core-experience-items"),
    path("testimonials-section/", TestimonialsSectionPublicAPIView.as_view(), name="core-testimonials-section"),
    path("testimonials/", TestimonialListPublicAPIView.as_view(), name="core-testimonials"),
    path("testimonials/featured/", FeaturedTestimonialListPublicAPIView.as_view(), name="core-featured-testimonials"),
    path("projects-showcase-section/", ProjectsShowcaseSectionPublicAPIView.as_view(), name="core-projects-showcase-section"),
    path("blog-section/", BlogSectionPublicAPIView.as_view(), name="core-blog-section"),
    path("contact-section/", ContactSectionPublicAPIView.as_view(), name="core-contact-section"),
    path("social-links/", SocialLinkListPublicAPIView.as_view(), name="core-social-links"),
    path("contact-info/", ContactInfoPublicAPIView.as_view(), name="core-contact-info"),
    path("contact/", ContactMessageCreateAPIView.as_view(), name="core-contact-message-create"),

    # Manage APIs
    path("manage/hero/", HeroSectionManageAPIView.as_view(), name="manage-hero-list-create"),
    path("manage/hero/<int:pk>/", HeroSectionManageDetailAPIView.as_view(), name="manage-hero-detail"),

    path("manage/about/", AboutSectionManageAPIView.as_view(), name="manage-about-list-create"),
    path("manage/about/<int:pk>/", AboutSectionManageDetailAPIView.as_view(), name="manage-about-detail"),

    path("manage/brand-logos/", BrandLogoManageAPIView.as_view(), name="manage-brand-logos-list-create"),
    path("manage/brand-logos/<int:pk>/", BrandLogoManageDetailAPIView.as_view(), name="manage-brand-logos-detail"),

    path("manage/skills/", SkillManageAPIView.as_view(), name="manage-skills-list-create"),
    path("manage/skills/<int:pk>/", SkillManageDetailAPIView.as_view(), name="manage-skills-detail"),

    path("manage/experience-section/", ExperienceSectionManageAPIView.as_view(), name="manage-experience-section-list-create"),
    path("manage/experience-section/<int:pk>/", ExperienceSectionManageDetailAPIView.as_view(), name="manage-experience-section-detail"),

    path("manage/experience-items/", ExperienceItemManageAPIView.as_view(), name="manage-experience-items-list-create"),
    path("manage/experience-items/<int:pk>/", ExperienceItemManageDetailAPIView.as_view(), name="manage-experience-items-detail"),

    path("manage/testimonials-section/", TestimonialsSectionManageAPIView.as_view(), name="manage-testimonials-section-list-create"),
    path("manage/testimonials-section/<int:pk>/", TestimonialsSectionManageDetailAPIView.as_view(), name="manage-testimonials-section-detail"),

    path("manage/testimonials/", TestimonialManageAPIView.as_view(), name="manage-testimonials-list-create"),
    path("manage/testimonials/<int:pk>/", TestimonialManageDetailAPIView.as_view(), name="manage-testimonials-detail"),

    path("manage/projects-showcase-section/", ProjectsShowcaseSectionManageAPIView.as_view(), name="manage-projects-showcase-section-list-create"),
    path("manage/projects-showcase-section/<int:pk>/", ProjectsShowcaseSectionManageDetailAPIView.as_view(), name="manage-projects-showcase-section-detail"),

    path("manage/blog-section/", BlogSectionManageAPIView.as_view(), name="manage-blog-section-list-create"),
    path("manage/blog-section/<int:pk>/", BlogSectionManageDetailAPIView.as_view(), name="manage-blog-section-detail"),

    path("manage/contact-section/", ContactSectionManageAPIView.as_view(), name="manage-contact-section-list-create"),
    path("manage/contact-section/<int:pk>/", ContactSectionManageDetailAPIView.as_view(), name="manage-contact-section-detail"),

    path("manage/social-links/", SocialLinkManageAPIView.as_view(), name="manage-social-links-list-create"),
    path("manage/social-links/<int:pk>/", SocialLinkManageDetailAPIView.as_view(), name="manage-social-links-detail"),

    path("manage/contact-info/", ContactInfoManageAPIView.as_view(), name="manage-contact-info-list-create"),
    path("manage/contact-info/<int:pk>/", ContactInfoManageDetailAPIView.as_view(), name="manage-contact-info-detail"),

    path("manage/contact-messages/", ContactMessageManageAPIView.as_view(), name="manage-contact-messages"),
    path("manage/contact-messages/<int:pk>/", ContactMessageManageDetailAPIView.as_view(), name="manage-contact-message-detail"),
]