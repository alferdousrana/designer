import { useEffect, useState } from "react";
import { getBlogs } from "../services/api/blogApi";

function toArray(value) {
  if (Array.isArray(value)) return value;
  return [];
}

function normalizeBlog(item) {
  return {
    id: item.id,
    title: item.title || "",
    slug: item.slug || "",
    categoryName: item?.category?.name || "",
    authorName: item.author_name || "",
    excerpt: item.excerpt || "",
    featuredImage: item.featured_image || item.cover_image || "",
    coverImage: item.cover_image || item.featured_image || "",
    readTime: item.read_time || 0,
    viewCount: item.view_count || 0,
    keywords: item.keywords || "",
    isFeatured: Boolean(item.is_featured),
    isHighlighted: Boolean(item.is_highlighted),
    publishedAt: item.published_at || "",
    order: item.order || 0,
    raw: item,
  };
}

export default function useBlogs(page = 1) {
  const [blogs, setBlogs] = useState([]);
  const [pagination, setPagination] = useState({
    count: 0,
    next: null,
    previous: null,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    async function loadBlogs() {
      try {
        setLoading(true);
        setError("");

        const response = await getBlogs(page);
        const results = toArray(response?.results).map(normalizeBlog);

        if (!ignore) {
          setBlogs(results);
          setPagination({
            count: response?.count || results.length,
            next: response?.next || null,
            previous: response?.previous || null,
          });
        }
      } catch (err) {
        if (!ignore) {
          setError("Failed to load blog posts.");
          setBlogs([]);
          setPagination({
            count: 0,
            next: null,
            previous: null,
          });
        }
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    }

    loadBlogs();

    return () => {
      ignore = true;
    };
  }, [page]);

  return { blogs, pagination, loading, error };
}