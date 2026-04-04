import { fetchJson } from "./apiClient";
import { fallbackCaseStudies } from "../../data/fallbackCaseStudies";

export function getCaseStudies(page = 1) {
  return fetchJson(`/api/case-studies/?page=${page}`);
}

export async function getCaseStudyDetails(slug) {
  try {
    return await fetchJson(`/api/case-studies/${slug}/`);
  } catch (error) {
    const fallbackItem = fallbackCaseStudies.find((item) => item.slug === slug);

    if (fallbackItem) {
      return fallbackItem;
    }

    throw error;
  }
}