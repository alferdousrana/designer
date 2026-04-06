import { fetchJson } from "./apiClient";

// =========================
// Home aggregate API
// =========================
export function getHomePageData() {
  return fetchJson("/api/core/home/");
}

// =========================
// Core single section APIs
// =========================
export function getHeroSection() {
  return fetchJson("/api/core/hero/");
}

export function getAboutSection() {
  return fetchJson("/api/core/about/");
}

export function getBlogSection() {
  return fetchJson("/api/core/blog-section/");
}

export function getContactInfo() {
  return fetchJson("/api/core/contact-info/");
}

export function getContactSection() {
  return fetchJson("/api/core/contact-section/");
}

export function getExperienceSection() {
  return fetchJson("/api/core/experience-section/");
}

export function getProjectsShowcaseSection() {
  return fetchJson("/api/core/projects-showcase-section/");
}

export function getTestimonialsSection() {
  return fetchJson("/api/core/testimonials-section/");
}

// =========================
// Core list APIs
// =========================
export function getBrandLogos() {
  return fetchJson("/api/core/brand-logos/");
}

export function getExperienceItems() {
  return fetchJson("/api/core/experience-items/");
}

export function getSkills() {
  return fetchJson("/api/core/skills/");
}

export function getSocialLinks() {
  return fetchJson("/api/core/social-links/");
}

export function getTestimonials() {
  return fetchJson("/api/core/testimonials/");
}

export function getFeaturedTestimonials() {
  return fetchJson("/api/core/testimonials/featured/");
}

// =========================
// Project / Blog APIs
// =========================
export function getFeaturedProjects() {
  return fetchJson("/api/project/featured/");
}

export function getFeaturedBlogs() {
  return fetchJson("/api/blog/featured/");
}

// =========================
// Contact API
// =========================
export function submitContactForm(payload) {
  return fetchJson("/api/core/contact/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}