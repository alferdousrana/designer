import { fetchJson } from "./apiClient";
import { fallbackProjects } from "../../data/fallbackProjects";

function getFallbackProjectBySlug(slug) {
  return fallbackProjects.find((item) => item.slug === slug) || null;
}

function buildFallbackProjectDetails(item) {
  if (!item) return null;

  const coverImage = item.cover_image || item.thumbnail || "";
  const shortDesc = item.short_desc || "";
  const categoryName = item?.category?.name || "Project Category";

  return {
    ...item,
    overview:
      item.overview ||
      `<p>${shortDesc}</p><p>This project showcases a polished product design process with strong visual hierarchy, usability improvements, and production-ready interface thinking.</p>`,
    tools_used: item.tools_used || "Figma, FigJam, Photoshop",
    my_role: item.my_role || "Product Designer",
    duration: item.duration || "6 Weeks",
    keywords: item.keywords || `${item.title}, ${categoryName}, Product Design`,
    tags: item.tags || [],
    challenge:
      item.challenge ||
      "<p>The main challenge was to create a modern and conversion-focused experience while keeping the interface simple, elegant, and easy to use.</p>",
    goal:
      item.goal ||
      "<p>The goal was to improve usability, build stronger visual trust, and create a consistent design system for future scaling.</p>",
    process:
      item.process ||
      "<p>The process included discovery, user flow mapping, wireframing, UI exploration, component design, and responsive refinement.</p>",
    solution:
      item.solution ||
      "<p>The final solution introduced a cleaner layout structure, better CTA hierarchy, and more intuitive interaction patterns.</p>",
    outcome:
      item.outcome ||
      "<p>The final concept delivers a more premium digital experience with stronger clarity, usability, and visual consistency.</p>",
    metrics: item.metrics || [
      {
        id: 1,
        label: "Client Rating",
        value: item.rating || "4.8/5",
        order: 1,
        is_active: true,
      },
      {
        id: 2,
        label: "Delivery Time",
        value: item.duration || "6 Weeks",
        order: 2,
        is_active: true,
      },
      {
        id: 3,
        label: "Project Status",
        value: "Completed",
        order: 3,
        is_active: true,
      },
    ],
    gallery: item.gallery || [
      {
        id: 1,
        image: coverImage,
        caption: `${item.title} cover preview`,
        alt_text: item.title,
        order: 1,
        is_active: true,
      },
      {
        id: 2,
        image: item.thumbnail || coverImage,
        caption: `${item.title} showcase`,
        alt_text: item.title,
        order: 2,
        is_active: true,
      },
    ],
    sections: item.sections || [
      {
        id: 1,
        title: "Research & Planning",
        content:
          "<p>We explored the product scope, aligned business needs with user expectations, and structured the main experience flows before moving into UI design.</p>",
        image: coverImage,
        order: 1,
        is_active: true,
      },
      {
        id: 2,
        title: "Design Execution",
        content:
          "<p>The interface direction focused on clean composition, stronger readability, conversion-friendly content blocks, and a premium visual system.</p>",
        image: item.thumbnail || coverImage,
        order: 2,
        is_active: true,
      },
    ],
  };
}

export async function getProjects(page = 1) {
  try {
    return await fetchJson(`/api/project/?page=${page}`);
  } catch (error) {
    return {
      count: fallbackProjects.length,
      next: null,
      previous: null,
      results: fallbackProjects,
    };
  }
}

export async function getProjectDetails(slug) {
  try {
    return await fetchJson(`/api/project/${slug}/`);
  } catch (error) {
    const fallbackItem = getFallbackProjectBySlug(slug);

    if (fallbackItem) {
      return buildFallbackProjectDetails(fallbackItem);
    }

    throw error;
  }
}