import { useEffect, useState } from "react";
import { getProjectDetails } from "../services/api/projectApi";

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

function normalizeMetrics(metrics) {
  return toArray(metrics)
    .filter((item) => item?.is_active !== false)
    .sort((a, b) => (a.order || 0) - (b.order || 0))
    .map((item) => ({
      id: item.id,
      label: item.label || "",
      value: item.value || "",
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

function normalizeGallery(gallery) {
  return toArray(gallery)
    .filter((item) => item?.is_active !== false)
    .sort((a, b) => (a.order || 0) - (b.order || 0))
    .map((item) => ({
      id: item.id,
      image: item.image || "",
      caption: item.caption || "",
      altText: item.alt_text || item.caption || "Project image",
    }));
}

function normalizeProject(data) {
  if (!data) return null;

  return {
    id: data.id,
    title: data.title || "",
    slug: data.slug || "",
    shortDesc: data.short_desc || "",
    overview: data.overview || "",
    thumbnail: data.thumbnail || "",
    coverImage: data.cover_image || data.thumbnail || "",
    categoryName: data?.category?.name || "",
    categorySlug: data?.category?.slug || "",
    tags: toArray(data.tags),
    toolsUsed: data.tools_used || "",
    toolsList: splitToList(data.tools_used),
    myRole: data.my_role || "",
    duration: data.duration || "",
    clientName: data.client_name || "",
    liveUrl: data.live_url || "",
    behanceUrl: data.behance_url || "",
    githubUrl: data.github_url || "",
    figmaUrl: data.figma_url || "",
    readTime: data.read_time || 0,
    viewCount: data.view_count || 0,
    keywords: data.keywords || "",
    keywordList: splitToList(data.keywords),
    challenge: data.challenge || "",
    goal: data.goal || "",
    process: data.process || "",
    solution: data.solution || "",
    outcome: data.outcome || "",
    status: data.status || "",
    publishedAt: data.published_at || "",
    seoTitle: data.seo_title || "",
    seoDescription: data.seo_description || "",
    metrics: normalizeMetrics(data.metrics),
    gallery: normalizeGallery(data.gallery),
    sections: normalizeSections(data.sections),
  };
}

export default function useProjectDetails(slug) {
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    async function loadProject() {
      try {
        setLoading(true);
        setError("");

        const response = await getProjectDetails(slug);
        const normalized = normalizeProject(response);

        if (!ignore) {
          setProject(normalized);
        }
      } catch (err) {
        if (!ignore) {
          setError("Failed to load project details.");
        }
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    }

    if (slug) {
      loadProject();
    }

    return () => {
      ignore = true;
    };
  }, [slug]);

  return { project, loading, error };
}