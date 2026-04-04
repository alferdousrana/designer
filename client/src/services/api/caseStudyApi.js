import { fetchJson } from "./apiClient";

export function getCaseStudies(page = 1) {
  return fetchJson(`/api/case-studies/?page=${page}`);
}