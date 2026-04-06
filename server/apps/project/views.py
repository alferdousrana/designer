from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.response import Response

from .models import (
    Category,
    ProjectTag,
    Project,
    ProjectImage,
    ProjectSection,
    ProjectMetric,
    PublishStatus,
)
from .serializers import (
    CategorySerializer,
    ProjectTagSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectWriteSerializer,
    CategoryWriteSerializer,
    ProjectTagWriteSerializer,
    ProjectImageSerializer,
    ProjectImageWriteSerializer,
    ProjectSectionSerializer,
    ProjectSectionWriteSerializer,
    ProjectMetricSerializer,
    ProjectMetricWriteSerializer,
)


# =========================
# Public APIs
# =========================

@extend_schema_view(
    get=extend_schema(
        tags=["Project Public"],
        summary="List published projects",
        description="Returns public published and active projects with filtering, search, ordering, and pagination.",
        parameters=[
            OpenApiParameter(name="category", description="Category slug", required=False, type=str),
            OpenApiParameter(name="is_featured", description="true / false", required=False, type=bool),
            OpenApiParameter(name="is_highlighted", description="true / false", required=False, type=bool),
            OpenApiParameter(name="search", description="Search by title, short_desc, tools_used, client_name, my_role, keywords", required=False, type=str),
            OpenApiParameter(name="ordering", description="order, -created_at, title, read_time, view_count", required=False, type=str),
            OpenApiParameter(name="page", description="Page number", required=False, type=int),
        ],
    )
)
class ProjectListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
    "title","short_desc","overview","challenge","goal","process","solution" "outcome","tools_used","client_name","my_role","keywords"]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]

    def get_queryset(self):
        queryset = Project.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
        ).select_related("category").prefetch_related("tags")

        category_slug = self.request.query_params.get("category")
        is_featured = self.request.query_params.get("is_featured")
        is_highlighted = self.request.query_params.get("is_highlighted")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if is_featured is not None:
            queryset = queryset.filter(is_featured=is_featured.lower() == "true")

        if is_highlighted is not None:
            queryset = queryset.filter(is_highlighted=is_highlighted.lower() == "true")

        return queryset


@extend_schema_view(
    get=extend_schema(
        tags=["Project Public"],
        summary="Get project details",
        description="Returns a single published project with nested category, tags, gallery, sections, and metrics. Also increments view_count.",
    )
)
class ProjectDetailPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
        ).select_related("category").prefetch_related(
            "tags",
            "gallery",
            "sections",
            "metrics",
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Project.objects.filter(pk=instance.pk).update(view_count=F("view_count") + 1)
        instance.refresh_from_db()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(
        tags=["Project Public"],
        summary="List active categories",
    )
)
class CategoryListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True).order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(
        tags=["Project Public"],
        summary="List active project tags",
    )
)
class ProjectTagListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectTagSerializer
    queryset = ProjectTag.objects.filter(is_active=True).order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(
        tags=["Project Public"],
        summary="List featured projects",
    )
)
class FeaturedProjectListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        return Project.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
            is_featured=True,
        ).select_related("category").prefetch_related("tags").order_by("order", "-created_at")


# =========================
# Manage APIs
# =========================

@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List categories"),
    post=extend_schema(tags=["Project Manage"], summary="Create category"),
)
class CategoryManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all().order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "slug", "description"]
    ordering_fields = ["order", "created_at", "name"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CategoryWriteSerializer
        return CategorySerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve category"),
    put=extend_schema(tags=["Project Manage"], summary="Update category"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update category"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete category"),
)
class CategoryManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CategoryWriteSerializer
        return CategorySerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List project tags"),
    post=extend_schema(tags=["Project Manage"], summary="Create project tag"),
)
class ProjectTagManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectTag.objects.all().order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "slug"]
    ordering_fields = ["order", "created_at", "name"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectTagWriteSerializer
        return ProjectTagSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve project tag"),
    put=extend_schema(tags=["Project Manage"], summary="Update project tag"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update project tag"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete project tag"),
)
class ProjectTagManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectTag.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProjectTagWriteSerializer
        return ProjectTagSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List projects"),
    post=extend_schema(tags=["Project Manage"], summary="Create project"),
)
class ProjectManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Project.objects.all().select_related("category").prefetch_related("tags").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "is_active", "is_featured", "is_highlighted", "category"]
    search_fields = [
    "title",
    "slug",
    "short_desc",
    "overview",
    "challenge",
    "goal",
    "process",
    "solution",
    "outcome",
    "tools_used",
    "client_name",
    "my_role",
    "keywords",
]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectWriteSerializer
        return ProjectListSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve project"),
    put=extend_schema(tags=["Project Manage"], summary="Update project"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update project"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete project"),
)
class ProjectManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Project.objects.all().select_related("category").prefetch_related("tags", "gallery", "sections", "metrics")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProjectWriteSerializer
        return ProjectDetailSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List project gallery items"),
    post=extend_schema(tags=["Project Manage"], summary="Create project gallery item"),
)
class ProjectImageManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectImage.objects.all().select_related("project").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["project", "is_active"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectImageWriteSerializer
        return ProjectImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve project gallery item"),
    put=extend_schema(tags=["Project Manage"], summary="Update project gallery item"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update project gallery item"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete project gallery item"),
)
class ProjectImageManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectImage.objects.all().select_related("project")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProjectImageWriteSerializer
        return ProjectImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List project sections"),
    post=extend_schema(tags=["Project Manage"], summary="Create project section"),
)
class ProjectSectionManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectSection.objects.all().select_related("project").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["project", "is_active"]
    search_fields = ["title", "content"]
    ordering_fields = ["order", "created_at", "title"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectSectionWriteSerializer
        return ProjectSectionSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve project section"),
    put=extend_schema(tags=["Project Manage"], summary="Update project section"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update project section"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete project section"),
)
class ProjectSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectSection.objects.all().select_related("project")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProjectSectionWriteSerializer
        return ProjectSectionSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="List project metrics"),
    post=extend_schema(tags=["Project Manage"], summary="Create project metric"),
)
class ProjectMetricManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectMetric.objects.all().select_related("project").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["project", "is_active"]
    search_fields = ["label", "value"]
    ordering_fields = ["order", "created_at", "label"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectMetricWriteSerializer
        return ProjectMetricSerializer


@extend_schema_view(
    get=extend_schema(tags=["Project Manage"], summary="Retrieve project metric"),
    put=extend_schema(tags=["Project Manage"], summary="Update project metric"),
    patch=extend_schema(tags=["Project Manage"], summary="Partial update project metric"),
    delete=extend_schema(tags=["Project Manage"], summary="Delete project metric"),
)
class ProjectMetricManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ProjectMetric.objects.all().select_related("project")

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProjectMetricWriteSerializer
        return ProjectMetricSerializer