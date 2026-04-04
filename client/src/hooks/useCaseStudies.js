import { useEffect, useState } from "react";
import { getCaseStudies } from "../services/api/caseStudyApi";
import { fallbackCaseStudies } from "../data/fallbackCaseStudies";

function normalizeCaseStudiesResponse(response) {
  if (Array.isArray(response)) {
    return {
      results: response,
      next: null,
      previous: null,
      count: response.length,
    };
  }

  return {
    results: response?.results || fallbackCaseStudies,
    next: response?.next || null,
    previous: response?.previous || null,
    count: response?.count || fallbackCaseStudies.length,
  };
}

function useCaseStudies(page = 1) {
  const [caseStudies, setCaseStudies] = useState(fallbackCaseStudies);
  const [pagination, setPagination] = useState({
    next: null,
    previous: null,
    count: fallbackCaseStudies.length,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadCaseStudies() {
      try {
        setLoading(true);
        setError("");

        const response = await getCaseStudies(page);
        const normalized = normalizeCaseStudiesResponse(response);

        const safeResults = (normalized.results || [])
          .filter((item) => item?.is_active !== false)
          .sort((a, b) => (a.order ?? 0) - (b.order ?? 0));

        setCaseStudies(safeResults.length ? safeResults : fallbackCaseStudies);
        setPagination({
          next: normalized.next,
          previous: normalized.previous,
          count: normalized.count,
        });
      } catch (err) {
        console.error(err);
        setError("Failed to load case studies. Showing fallback content.");
        setCaseStudies(fallbackCaseStudies);
        setPagination({
          next: null,
          previous: null,
          count: fallbackCaseStudies.length,
        });
      } finally {
        setLoading(false);
      }
    }

    loadCaseStudies();
  }, [page]);

  return {
    caseStudies,
    pagination,
    loading,
    error,
  };
}

export default useCaseStudies;