from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .models import (
    CaseStudy,
    CaseStudyImage,
    CaseStudySection,
    CaseStudyMetric,
    PublishStatus,
)
from .serializers import (
    CaseStudyListSerializer,
    CaseStudyDetailSerializer,
    CaseStudyWriteSerializer,
    CaseStudyImageSerializer,
    CaseStudyImageWriteSerializer,
    CaseStudySectionSerializer,
    CaseStudySectionWriteSerializer,
    CaseStudyMetricSerializer,
    CaseStudyMetricWriteSerializer,
)


@extend_schema_view(
    get=extend_schema(
        tags=["Case Study Public"],
        summary="List published case studies",
        parameters=[
            OpenApiParameter(name="is_featured", required=False, type=bool),
            OpenApiParameter(name="is_highlighted", required=False, type=bool),
            OpenApiParameter(name="search", required=False, type=str),
            OpenApiParameter(name="ordering", required=False, type=str),
            OpenApiParameter(name="page", required=False, type=int),
        ],
    )
)
class CaseStudyListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CaseStudyListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "title",
        "short_desc",
        "project_name",
        "client_name",
        "industry",
        "my_role",
        "team",
        "timeline",
        "tools_used",
        "keywords",
    ]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]

    def get_queryset(self):
        queryset = CaseStudy.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
        )

        is_featured = self.request.query_params.get("is_featured")
        is_highlighted = self.request.query_params.get("is_highlighted")

        if is_featured is not None:
            queryset = queryset.filter(is_featured=is_featured.lower() == "true")

        if is_highlighted is not None:
            queryset = queryset.filter(is_highlighted=is_highlighted.lower() == "true")

        return queryset


@extend_schema_view(
    get=extend_schema(
        tags=["Case Study Public"],
        summary="Get case study details",
        description="Returns a single published case study with gallery, sections, and metrics. Also increments view_count.",
    )
)
class CaseStudyDetailPublicAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CaseStudyDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return CaseStudy.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
        ).prefetch_related("gallery", "sections", "metrics")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        CaseStudy.objects.filter(pk=instance.pk).update(view_count=F("view_count") + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(tags=["Case Study Public"], summary="List featured case studies"),
)
class FeaturedCaseStudyListPublicAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CaseStudyListSerializer

    def get_queryset(self):
        return CaseStudy.objects.filter(
            is_active=True,
            status=PublishStatus.PUBLISHED,
            is_featured=True,
        ).order_by("order", "-created_at")


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="List case studies"),
    post=extend_schema(tags=["Case Study Manage"], summary="Create case study"),
)
class CaseStudyManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudy.objects.all().order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "is_active", "is_featured", "is_highlighted"]
    search_fields = [
        "title",
        "slug",
        "short_desc",
        "project_name",
        "client_name",
        "industry",
        "my_role",
        "team",
        "timeline",
        "tools_used",
        "keywords",
    ]
    ordering_fields = ["order", "created_at", "title", "read_time", "view_count"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CaseStudyWriteSerializer
        return CaseStudyListSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="Retrieve case study"),
    put=extend_schema(tags=["Case Study Manage"], summary="Update case study"),
    patch=extend_schema(tags=["Case Study Manage"], summary="Partial update case study"),
    delete=extend_schema(tags=["Case Study Manage"], summary="Delete case study"),
)
class CaseStudyManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudy.objects.all().prefetch_related("gallery", "sections", "metrics")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CaseStudyWriteSerializer
        return CaseStudyDetailSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="List gallery items"),
    post=extend_schema(tags=["Case Study Manage"], summary="Create gallery item"),
)
class CaseStudyImageManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudyImage.objects.all().select_related("case_study").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["case_study", "is_active"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CaseStudyImageWriteSerializer
        return CaseStudyImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="Retrieve gallery item"),
    put=extend_schema(tags=["Case Study Manage"], summary="Update gallery item"),
    patch=extend_schema(tags=["Case Study Manage"], summary="Partial update gallery item"),
    delete=extend_schema(tags=["Case Study Manage"], summary="Delete gallery item"),
)
class CaseStudyImageManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudyImage.objects.all().select_related("case_study")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CaseStudyImageWriteSerializer
        return CaseStudyImageSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="List sections"),
    post=extend_schema(tags=["Case Study Manage"], summary="Create section"),
)
class CaseStudySectionManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudySection.objects.all().select_related("case_study").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["case_study", "is_active"]
    search_fields = ["title", "content"]
    ordering_fields = ["order", "created_at", "title"]
    ordering = ["order", "-created_at"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CaseStudySectionWriteSerializer
        return CaseStudySectionSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="Retrieve section"),
    put=extend_schema(tags=["Case Study Manage"], summary="Update section"),
    patch=extend_schema(tags=["Case Study Manage"], summary="Partial update section"),
    delete=extend_schema(tags=["Case Study Manage"], summary="Delete section"),
)
class CaseStudySectionManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudySection.objects.all().select_related("case_study")
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CaseStudySectionWriteSerializer
        return CaseStudySectionSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="List metrics"),
    post=extend_schema(tags=["Case Study Manage"], summary="Create metric"),
)
class CaseStudyMetricManageAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudyMetric.objects.all().select_related("case_study").order_by("order", "-created_at")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["case_study", "is_active"]
    search_fields = ["label", "value"]
    ordering_fields = ["order", "created_at", "label"]
    ordering = ["order", "-created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CaseStudyMetricWriteSerializer
        return CaseStudyMetricSerializer


@extend_schema_view(
    get=extend_schema(tags=["Case Study Manage"], summary="Retrieve metric"),
    put=extend_schema(tags=["Case Study Manage"], summary="Update metric"),
    patch=extend_schema(tags=["Case Study Manage"], summary="Partial update metric"),
    delete=extend_schema(tags=["Case Study Manage"], summary="Delete metric"),
)
class CaseStudyMetricManageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CaseStudyMetric.objects.all().select_related("case_study")

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CaseStudyMetricWriteSerializer
        return CaseStudyMetricSerializer