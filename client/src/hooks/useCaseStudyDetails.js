import { useEffect, useState } from "react";
import { getCaseStudyDetails } from "../services/api/caseStudyApi";

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
      altText: item.alt_text || item.caption || "Case study image",
    }));
}

function normalizeCaseStudy(data) {
  if (!data) return null;

  return {
    id: data.id,
    title: data.title || "",
    slug: data.slug || "",
    shortDesc: data.short_desc || "",
    overview: data.overview || "",
    thumbnail: data.thumbnail || "",
    coverImage: data.cover_image || data.thumbnail || "",
    projectName: data.project_name || "",
    clientName: data.client_name || "",
    industry: data.industry || "",
    myRole: data.my_role || "",
    team: data.team || "",
    timeline: data.timeline || "",
    toolsUsed: data.tools_used || "",
    toolsList: splitToList(data.tools_list || data.tools_used),
    challenge: data.challenge || "",
    goal: data.goal || "",
    process: data.process || "",
    solution: data.solution || "",
    outcome: data.outcome || "",
    liveUrl: data.live_url || "",
    prototypeUrl: data.prototype_url || "",
    figmaUrl: data.figma_url || "",
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
    metrics: normalizeMetrics(data.metrics),
  };
}

export default function useCaseStudyDetails(slug) {
  const [caseStudy, setCaseStudy] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    async function loadCaseStudy() {
      try {
        setLoading(true);
        setError("");

        const response = await getCaseStudyDetails(slug);
        const normalized = normalizeCaseStudy(response);

        if (!ignore) {
          setCaseStudy(normalized);
        }
      } catch (err) {
        if (!ignore) {
          setError("Failed to load case study details.");
        }
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    }

    if (slug) {
      loadCaseStudy();
    }

    return () => {
      ignore = true;
    };
  }, [slug]);

  return { caseStudy, loading, error };
}