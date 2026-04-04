import { useEffect, useState } from "react";
import { getBlogDetails } from "../services/api/blogApi";

function toArray(value) {
  if (Array.isArray(value)) return value;
  return [];
}

function splitToList(value) {
  if (!value || typeof value !== "string") return [];
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function normalizeGallery(gallery) {
  return toArray(gallery)
    .filter((item) => item?.is_active !== false)
    .sort((a, b) => (a.order || 0) - (b.order || 0))
    .map((item) => ({
      id: item.id,
      image: item.image || "",
      caption: item.caption || "",
      altText: item.alt_text || item.caption || "Blog image",
    }));
}

function normalizeSections(sections) {
  return toArray(sections)
    .filter((item) => item?.is_active !== false)
    .sort((a, b) => (a.order || 0) - (b.order || 0))
    .map((item) => ({
      id: item.id,
      title: item.title || "",
      content: item.content || "",
      image: item.image || "",
    }));
}

function normalizeBlog(data) {
  if (!data) return null;

  return {
    id: data.id,
    title: data.title || "",
    slug: data.slug || "",
    categoryName: data?.category?.name || "",
    categorySlug: data?.category?.slug || "",
    tags: toArray(data.tags),
    authorName: data.author_name || "",
    excerpt: data.excerpt || "",
    content: data.content || "",
    featuredImage: data.featured_image || data.cover_image || "",
    coverImage: data.cover_image || data.featured_image || "",
    readTime: data.read_time || 0,
    viewCount: data.view_count || 0,
    keywords: data.keywords || "",
    keywordList: splitToList(data.keywords_list || data.keywords),
    isFeatured: Boolean(data.is_featured),
    isHighlighted: Boolean(data.is_highlighted),
    status: data.status || "",
    publishedAt: data.published_at || "",
    seoTitle: data.seo_title || "",
    seoDescription: data.seo_description || "",
    gallery: normalizeGallery(data.gallery),
    sections: normalizeSections(data.sections),
  };
}

export default function useBlogDetails(slug) {
  const [blog, setBlog] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    async function loadBlog() {
      try {
        setLoading(true);
        setError("");

        const response = await getBlogDetails(slug);
        const normalized = normalizeBlog(response);

        if (!ignore) {
          setBlog(normalized);
        }
      } catch (err) {
        if (!ignore) {
          setError("Failed to load blog details.");
        }
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    }

    if (slug) {
      loadBlog();
    }

    return () => {
      ignore = true;
    };
  }, [slug]);

  return { blog, loading, error };
}