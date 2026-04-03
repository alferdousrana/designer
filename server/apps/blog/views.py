from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .models import (
    BlogCategory,
    BlogTag,
    BlogPost,
    BlogImage,
    BlogSection,
    PublishStatus,
)
from .serializers import (
    BlogCategorySerializer,
    BlogTagSerializer,
    BlogPostListSerializer,
    BlogPostDetailSerializer,
    BlogPostWriteSerializer,
    BlogCategoryWriteSerializer,
    BlogTagWriteSerializer,
    BlogImageSerializer,
    BlogImageWriteSerializer,
    BlogSectionSerializer,
    BlogSectionWriteSerializer,
)


@extend_schema_view(
    get=extend_schema(
        tags=["Blog Public"],
        summary="List published blog posts",
        parameters=[
            OpenApiParameter(name="category", description="Category slug", required=False, type=str),
            OpenApiParameter(name="is_featured", description="true / false", required=False, type=bool),
            OpenApiParameter(name="is_highlighted", description="true / false", required=False, type=bool),
            OpenApiParameter(name="search", description="Search by title, excerpt, content, author, keywords", required=False, type=str),
            OpenApiParameter(name="ordering", description="order, -created_at, title, read_time, view_count", required=False, type=str),
            OpenApiParameter(name="page", description="Page number", required=False, type=int),
        ],
    )
)
class BlogPostListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "excerpt", "content", "author_name", "keywords"]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]

    def get_queryset(self):
        queryset = BlogPost.objects.filter(
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
        tags=["Blog Public"],
        summary="Get blog post details",
        description="Returns a single published blog post with nested category, tags, gallery, and sections. Also increments view_count.",
    )
)
class BlogPostDetailPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
        ).select_related("category").prefetch_related(
            "tags",
            "gallery",
            "sections",
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        BlogPost.objects.filter(pk=instance.pk).update(view_count=F("view_count") + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(tags=["Blog Public"], summary="List active blog categories"),
)
class BlogCategoryListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.filter(is_active=True).order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(tags=["Blog Public"], summary="List active blog tags"),
)
class BlogTagListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogTagSerializer
    queryset = BlogTag.objects.filter(is_active=True).order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(tags=["Blog Public"], summary="List featured blog posts"),
)
class FeaturedBlogPostListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostListSerializer

    def get_queryset(self):
        return BlogPost.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
            is_featured=True,
        ).select_related("category").prefetch_related("tags").order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="List blog categories"),
    post=extend_schema(tags=["Blog Manage"], summary="Create blog category"),
)
class BlogCategoryManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogCategory.objects.all().order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "slug", "description"]
    ordering_fields = ["order", "created_at", "name"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogCategoryWriteSerializer
        return BlogCategorySerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="Retrieve blog category"),
    put=extend_schema(tags=["Blog Manage"], summary="Update blog category"),
    patch=extend_schema(tags=["Blog Manage"], summary="Partial update blog category"),
    delete=extend_schema(tags=["Blog Manage"], summary="Delete blog category"),
)
class BlogCategoryManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogCategory.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogCategoryWriteSerializer
        return BlogCategorySerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="List blog tags"),
    post=extend_schema(tags=["Blog Manage"], summary="Create blog tag"),
)
class BlogTagManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogTag.objects.all().order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "slug"]
    ordering_fields = ["order", "created_at", "name"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogTagWriteSerializer
        return BlogTagSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="Retrieve blog tag"),
    put=extend_schema(tags=["Blog Manage"], summary="Update blog tag"),
    patch=extend_schema(tags=["Blog Manage"], summary="Partial update blog tag"),
    delete=extend_schema(tags=["Blog Manage"], summary="Delete blog tag"),
)
class BlogTagManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogTag.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogTagWriteSerializer
        return BlogTagSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="List blog posts"),
    post=extend_schema(tags=["Blog Manage"], summary="Create blog post"),
)
class BlogPostManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogPost.objects.all().select_related("category").prefetch_related("tags").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "is_active", "is_featured", "is_highlighted", "category"]
    search_fields = ["title", "slug", "excerpt", "content", "author_name", "keywords"]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogPostWriteSerializer
        return BlogPostListSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="Retrieve blog post"),
    put=extend_schema(tags=["Blog Manage"], summary="Update blog post"),
    patch=extend_schema(tags=["Blog Manage"], summary="Partial update blog post"),
    delete=extend_schema(tags=["Blog Manage"], summary="Delete blog post"),
)
class BlogPostManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogPost.objects.all().select_related("category").prefetch_related("tags", "gallery", "sections")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogPostWriteSerializer
        return BlogPostDetailSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="List blog gallery items"),
    post=extend_schema(tags=["Blog Manage"], summary="Create blog gallery item"),
)
class BlogImageManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogImage.objects.all().select_related("post").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["post", "is_active"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogImageWriteSerializer
        return BlogImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="Retrieve blog gallery item"),
    put=extend_schema(tags=["Blog Manage"], summary="Update blog gallery item"),
    patch=extend_schema(tags=["Blog Manage"], summary="Partial update blog gallery item"),
    delete=extend_schema(tags=["Blog Manage"], summary="Delete blog gallery item"),
)
class BlogImageManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogImage.objects.all().select_related("post")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogImageWriteSerializer
        return BlogImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="List blog sections"),
    post=extend_schema(tags=["Blog Manage"], summary="Create blog section"),
)
class BlogSectionManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogSection.objects.all().select_related("post").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["post", "is_active"]
    search_fields = ["title", "content"]
    ordering_fields = ["order", "created_at", "title"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogSectionWriteSerializer
        return BlogSectionSerializer


@extend_schema_view(
    get=extend_schema(tags=["Blog Manage"], summary="Retrieve blog section"),
    put=extend_schema(tags=["Blog Manage"], summary="Update blog section"),
    patch=extend_schema(tags=["Blog Manage"], summary="Partial update blog section"),
    delete=extend_schema(tags=["Blog Manage"], summary="Delete blog section"),
)
class BlogSectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogSection.objects.all().select_related("post")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogSectionWriteSerializer
        return BlogSectionSerializer