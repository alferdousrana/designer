import { useEffect, useState } from "react";
import { getProjects } from "../services/api/projectApi";

function toArray(value) {
  if (Array.isArray(value)) return value;
  return [];
}

function normalizeProject(item) {
  return {
    id: item.id,
    title: item.title || "",
    slug: item.slug || "",
    shortDesc: item.short_desc || "",
    thumbnail: item.thumbnail || item.cover_image || "",
    coverImage: item.cover_image || item.thumbnail || "",
    categoryName: item?.category?.name || "",
    clientName: item.client_name || "",
    rating: item.rating || "",
    liveUrl: item.live_url || "",
    isFeatured: Boolean(item.is_featured),
    isHighlighted: Boolean(item.is_highlighted),
    publishedAt: item.published_at || "",
    order: item.order || 0,
    raw: item,
  };
}

export default function useProjects(page = 1) {
  const [projects, setProjects] = useState([]);
  const [pagination, setPagination] = useState({
    count: 0,
    next: null,
    previous: null,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    async function loadProjects() {
      try {
        setLoading(true);
        setError("");

        const response = await getProjects(page);
        const results = toArray(response?.results).map(normalizeProject);

        if (!ignore) {
          setProjects(results);
          setPagination({
            count: response?.count || results.length,
            next: response?.next || null,
            previous: response?.previous || null,
          });
        }
      } catch (err) {
        if (!ignore) {
          setError("Failed to load projects.");
          setProjects([]);
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

    loadProjects();

    return () => {
      ignore = true;
    };
  }, [page]);

  return { projects, pagination, loading, error };
}