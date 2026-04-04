from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .models import (
    HeroSection,
    AboutSection,
    BrandLogo,
    Skill,
    ExperienceSection,
    ExperienceItem,
    TestimonialsSection,
    Testimonial,
    ProjectsShowcaseSection,
    BlogSection,
    ContactSection,
    SocialLink,
    ContactInfo,
    ContactMessage,
)
from .serializers import (
    HeroSectionSerializer,
    AboutSectionSerializer,
    BrandLogoSerializer,
    SkillSerializer,
    ExperienceSectionSerializer,
    ExperienceItemSerializer,
    TestimonialsSectionSerializer,
    TestimonialSerializer,
    ProjectsShowcaseSectionSerializer,
    BlogSectionSerializer,
    ContactSectionSerializer,
    SocialLinkSerializer,
    ContactInfoSerializer,
    ContactMessageSerializer,
    ContactMessageAdminSerializer,
    HomePageSerializer,
)


# =========================
# Reusable mixin
# =========================

class SingleInstanceCreateRestrictionMixin:
    model = None
    error_message = "Only one instance is allowed for this resource."

    def perform_create(self, serializer):
        if self.model is None:
            raise ValidationError({"detail": "Model is not configured for this view."})

        if self.model.objects.exists():
            raise ValidationError({"detail": self.error_message})

        serializer.save()


# =========================
# Public APIs
# =========================

@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get homepage content",
        description="Returns all active homepage sections in a single response.",
    )
)
class HomePageAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = HomePageSerializer

    def get(self, request, *args, **kwargs):
        data = {
            "hero": HeroSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "about": AboutSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "brand_logos": BrandLogo.objects.filter(is_active=True).order_by("order", "id"),
            "skills": Skill.objects.filter(is_active=True).order_by("order", "id"),
            "experience_section": ExperienceSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "experience_items": ExperienceItem.objects.filter(is_active=True).order_by("order", "id"),
            "testimonials_section": TestimonialsSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "testimonials": Testimonial.objects.filter(is_active=True).order_by("order", "id"),
            "projects_showcase_section": ProjectsShowcaseSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "blog_section": BlogSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "contact_section": ContactSection.objects.filter(is_active=True).order_by("-updated_at").first(),
            "social_links": SocialLink.objects.filter(is_active=True).order_by("order", "id"),
            "contact_info": ContactInfo.objects.filter(is_active=True).order_by("-updated_at").first(),
        }
        serializer = self.get_serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active hero section",
    )
)
class HeroSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = HeroSectionSerializer

    def get_object(self):
        return HeroSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active about section",
    )
)
class AboutSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return AboutSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List active brand logos",
        parameters=[
            OpenApiParameter(name="ordering", required=False, type=str, description="order, created_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class BrandLogoListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BrandLogoSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "id"]

    def get_queryset(self):
        return BrandLogo.objects.filter(is_active=True).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List active skills",
        parameters=[
            OpenApiParameter(name="search", required=False, type=str, description="Search by skill title or description"),
            OpenApiParameter(name="ordering", required=False, type=str, description="order, title, created_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class SkillListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SkillSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["title", "description", "number", "project_link_text"]
    ordering_fields = ["order", "title", "created_at"]
    ordering = ["order", "id"]

    def get_queryset(self):
        return Skill.objects.filter(is_active=True).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active experience section",
    )
)
class ExperienceSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExperienceSectionSerializer

    def get_object(self):
        return ExperienceSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List active experience items",
        parameters=[
            OpenApiParameter(name="search", required=False, type=str, description="Search experience items"),
            OpenApiParameter(name="ordering", required=False, type=str, description="order, year, title, created_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class ExperienceItemListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExperienceItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["year", "title", "description"]
    ordering_fields = ["order", "year", "title", "created_at"]
    ordering = ["order", "id"]

    def get_queryset(self):
        return ExperienceItem.objects.filter(is_active=True).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active testimonials section",
    )
)
class TestimonialsSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestimonialsSectionSerializer

    def get_object(self):
        return TestimonialsSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List active testimonials",
        parameters=[
            OpenApiParameter(name="is_featured", required=False, type=bool, description="Filter by featured status"),
            OpenApiParameter(name="rating", required=False, type=int, description="Filter by rating"),
            OpenApiParameter(name="search", required=False, type=str, description="Search testimonials"),
            OpenApiParameter(name="ordering", required=False, type=str, description="order, rating, created_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class TestimonialListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestimonialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_featured", "rating"]
    search_fields = ["client_name", "client_role", "client_company", "review"]
    ordering_fields = ["order", "rating", "created_at"]
    ordering = ["order", "id"]

    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List featured testimonials",
    )
)
class FeaturedTestimonialListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(
            is_active=True,
            is_featured=True,
        ).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active projects showcase section",
    )
)
class ProjectsShowcaseSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectsShowcaseSectionSerializer

    def get_object(self):
        return ProjectsShowcaseSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active blog section",
    )
)
class BlogSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogSectionSerializer

    def get_object(self):
        return BlogSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active contact section",
    )
)
class ContactSectionPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSectionSerializer

    def get_object(self):
        return ContactSection.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="List active social links",
        parameters=[
            OpenApiParameter(name="platform", required=False, type=str, description="Filter by social platform"),
            OpenApiParameter(name="ordering", required=False, type=str, description="order, created_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class SocialLinkListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SocialLinkSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["platform"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "id"]

    def get_queryset(self):
        return SocialLink.objects.filter(is_active=True).order_by("order", "id")


@extend_schema_view(
    get=extend_schema(
        tags=["Core Public"],
        summary="Get active contact info",
    )
)
class ContactInfoPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.filter(is_active=True).order_by("-updated_at").first()


@extend_schema_view(
    post=extend_schema(
        tags=["Core Public"],
        summary="Submit contact message",
        description="Public endpoint for website contact form submission.",
    )
)
class ContactMessageCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        response_data = {
            "message": "Your message has been sent successfully.",
            "data": ContactMessageSerializer(instance).data,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


# =========================
# Dashboard / Manage APIs
# =========================

@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List hero sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create hero section"),
)
class HeroSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = HeroSectionSerializer
    queryset = HeroSection.objects.all().order_by("-updated_at")
    model = HeroSection
    error_message = "Hero Section already exists. You can only update the existing one."
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve hero section"),
    put=extend_schema(tags=["Core Manage"], summary="Update hero section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update hero section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete hero section"),
)
class HeroSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = HeroSectionSerializer
    queryset = HeroSection.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List about sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create about section"),
)
class AboutSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AboutSectionSerializer
    queryset = AboutSection.objects.all().order_by("-updated_at")
    model = AboutSection
    error_message = "About Section already exists. You can only update the existing one."
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve about section"),
    put=extend_schema(tags=["Core Manage"], summary="Update about section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update about section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete about section"),
)
class AboutSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AboutSectionSerializer
    queryset = AboutSection.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List brand logos"),
    post=extend_schema(tags=["Core Manage"], summary="Create brand logo"),
)
class BrandLogoManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandLogoSerializer
    queryset = BrandLogo.objects.all().order_by("order", "id")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "id"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve brand logo"),
    put=extend_schema(tags=["Core Manage"], summary="Update brand logo"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update brand logo"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete brand logo"),
)
class BrandLogoManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandLogoSerializer
    queryset = BrandLogo.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List skills"),
    post=extend_schema(tags=["Core Manage"], summary="Create skill"),
)
class SkillManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all().order_by("order", "id")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["title", "description", "number", "project_link_text"]
    ordering_fields = ["order", "title", "created_at"]
    ordering = ["order", "id"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve skill"),
    put=extend_schema(tags=["Core Manage"], summary="Update skill"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update skill"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete skill"),
)
class SkillManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List experience sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create experience section"),
)
class ExperienceSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ExperienceSectionSerializer
    queryset = ExperienceSection.objects.all().order_by("-updated_at")
    model = ExperienceSection
    error_message = "Experience Section already exists. You can only update the existing one."
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve experience section"),
    put=extend_schema(tags=["Core Manage"], summary="Update experience section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update experience section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete experience section"),
)
class ExperienceSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ExperienceSectionSerializer
    queryset = ExperienceSection.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List experience items"),
    post=extend_schema(tags=["Core Manage"], summary="Create experience item"),
)
class ExperienceItemManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ExperienceItemSerializer
    queryset = ExperienceItem.objects.all().order_by("order", "id")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["year", "title", "description"]
    ordering_fields = ["order", "year", "title", "created_at"]
    ordering = ["order", "id"]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve experience item"),
    put=extend_schema(tags=["Core Manage"], summary="Update experience item"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update experience item"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete experience item"),
)
class ExperienceItemManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ExperienceItemSerializer
    queryset = ExperienceItem.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List testimonials sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create testimonials section"),
)
class TestimonialsSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TestimonialsSectionSerializer
    queryset = TestimonialsSection.objects.all().order_by("-updated_at")
    model = TestimonialsSection
    error_message = "Testimonials Section already exists. You can only update the existing one."


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve testimonials section"),
    put=extend_schema(tags=["Core Manage"], summary="Update testimonials section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update testimonials section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete testimonials section"),
)
class TestimonialsSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TestimonialsSectionSerializer
    queryset = TestimonialsSection.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List testimonials"),
    post=extend_schema(tags=["Core Manage"], summary="Create testimonial"),
)
class TestimonialManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all().order_by("order", "id")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_featured", "rating", "is_active"]
    search_fields = ["client_name", "client_role", "client_company", "review"]
    ordering_fields = ["order", "rating", "created_at"]
    ordering = ["order", "id"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve testimonial"),
    put=extend_schema(tags=["Core Manage"], summary="Update testimonial"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update testimonial"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete testimonial"),
)
class TestimonialManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List projects showcase sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create projects showcase section"),
)
class ProjectsShowcaseSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProjectsShowcaseSectionSerializer
    queryset = ProjectsShowcaseSection.objects.all().order_by("-updated_at")
    model = ProjectsShowcaseSection
    error_message = "Projects Showcase Section already exists. You can only update the existing one."


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve projects showcase section"),
    put=extend_schema(tags=["Core Manage"], summary="Update projects showcase section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update projects showcase section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete projects showcase section"),
)
class ProjectsShowcaseSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProjectsShowcaseSectionSerializer
    queryset = ProjectsShowcaseSection.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List blog sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create blog section"),
)
class BlogSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BlogSectionSerializer
    queryset = BlogSection.objects.all().order_by("-updated_at")
    model = BlogSection
    error_message = "Blog Section already exists. You can only update the existing one."


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve blog section"),
    put=extend_schema(tags=["Core Manage"], summary="Update blog section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update blog section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete blog section"),
)
class BlogSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BlogSectionSerializer
    queryset = BlogSection.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List contact sections"),
    post=extend_schema(tags=["Core Manage"], summary="Create contact section"),
)
class ContactSectionManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactSectionSerializer
    queryset = ContactSection.objects.all().order_by("-updated_at")
    model = ContactSection
    error_message = "Contact Section already exists. You can only update the existing one."


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve contact section"),
    put=extend_schema(tags=["Core Manage"], summary="Update contact section"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update contact section"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete contact section"),
)
class ContactSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactSectionSerializer
    queryset = ContactSection.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List social links"),
    post=extend_schema(tags=["Core Manage"], summary="Create social link"),
)
class SocialLinkManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SocialLinkSerializer
    queryset = SocialLink.objects.all().order_by("order", "id")
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["platform", "is_active"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "id"]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve social link"),
    put=extend_schema(tags=["Core Manage"], summary="Update social link"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update social link"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete social link"),
)
class SocialLinkManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SocialLinkSerializer
    queryset = SocialLink.objects.all()


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="List contact info"),
    post=extend_schema(tags=["Core Manage"], summary="Create contact info"),
)
class ContactInfoManageAPIView(SingleInstanceCreateRestrictionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all().order_by("-updated_at")
    model = ContactInfo
    error_message = "Contact Info already exists. You can only update the existing one."


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve contact info"),
    put=extend_schema(tags=["Core Manage"], summary="Update contact info"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update contact info"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete contact info"),
)
class ContactInfoManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()


@extend_schema_view(
    get=extend_schema(
        tags=["Core Manage"],
        summary="List contact messages",
        parameters=[
            OpenApiParameter(name="status", required=False, type=str, description="Filter by message status"),
            OpenApiParameter(name="is_read", required=False, type=bool, description="Filter by read status"),
            OpenApiParameter(name="search", required=False, type=str, description="Search messages"),
            OpenApiParameter(name="ordering", required=False, type=str, description="created_at, updated_at"),
            OpenApiParameter(name="page", required=False, type=int, description="Page number"),
        ],
    )
)
class ContactMessageManageAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactMessageAdminSerializer
    queryset = ContactMessage.objects.all().order_by("-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "is_read"]
    search_fields = [
        "full_name",
        "email",
        "subject",
        "message",
        "company_name",
        "project_type",
    ]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]


@extend_schema_view(
    get=extend_schema(tags=["Core Manage"], summary="Retrieve contact message"),
    put=extend_schema(tags=["Core Manage"], summary="Update contact message"),
    patch=extend_schema(tags=["Core Manage"], summary="Partial update contact message"),
    delete=extend_schema(tags=["Core Manage"], summary="Delete contact message"),
)
class ContactMessageManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactMessageAdminSerializer
    queryset = ContactMessage.objects.all()