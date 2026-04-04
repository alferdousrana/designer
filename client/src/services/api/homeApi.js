import { fetchJson } from "./apiClient";

export function getHomePageData() {
  return fetchJson("/api/core/home/");
}

export function getFeaturedProjects() {
  return fetchJson("/api/project/featured/");
}

export function getFeaturedBlogs() {
  return fetchJson("/api/blog/featured/");
}

export function submitContactForm(payload) {
  return fetchJson("/api/core/contact/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}