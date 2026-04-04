import { fetchJson } from "./apiClient";
import { fallbackBlogs } from "../../data/fallbackBlogs";

function getFallbackBlogBySlug(slug) {
  return fallbackBlogs.find((item) => item.slug === slug) || null;
}

function buildFallbackBlogDetails(item) {
  if (!item) return null;

  const coverImage = item.cover_image || item.featured_image || "";
  const excerpt = item.excerpt || "";
  const categoryName = item?.category?.name || "Blog Category";
  const authorName = item.author_name || "Admin";

  return {
    ...item,
    content:
      item.content ||
      `<p>${excerpt}</p><p>This blog post presents a clean editorial layout with strong typography, readable spacing, and visually balanced content structure for a modern personal portfolio website.</p><p>The article is prepared so the frontend can be locked first and later updated automatically when backend content is available.</p>`,
    keywords_list: item.keywords_list || item.keywords || item.title || "",
    gallery: item.gallery || [
      {
        id: 1,
        image: coverImage,
        caption: `${item.title} cover image`,
        alt_text: item.title,
        order: 1,
        is_active: true,
      },
      {
        id: 2,
        image: item.featured_image || coverImage,
        caption: `${item.title} blog preview`,
        alt_text: item.title,
        order: 2,
        is_active: true,
      },
    ],
    sections: item.sections || [
      {
        id: 1,
        title: "Introduction",
        content:
          "<p>This section introduces the core idea of the article and helps establish the context, purpose, and reader expectation for the rest of the content.</p>",
        image: coverImage,
        order: 1,
        is_active: true,
      },
      {
        id: 2,
        title: "Key Insights",
        content:
          "<p>This section expands on the main topic with supporting details, examples, and practical insights in a content-first format.</p>",
        image: item.featured_image || coverImage,
        order: 2,
        is_active: true,
      },
    ],
    author_name: authorName,
    excerpt,
    cover_image: coverImage,
    featured_image: item.featured_image || coverImage,
    category: item.category || {
      id: 0,
      name: categoryName,
      slug: "blog-category",
      description: "",
      order: 1,
      is_active: true,
    },
    tags: item.tags || [],
  };
}

export async function getBlogs(page = 1) {
  try {
    return await fetchJson(`/api/blog/?page=${page}`);
  } catch (error) {
    return {
      count: fallbackBlogs.length,
      next: null,
      previous: null,
      results: fallbackBlogs,
    };
  }
}

export async function getBlogDetails(slug) {
  try {
    return await fetchJson(`/api/blog/${slug}/`);
  } catch (error) {
    const fallbackItem = getFallbackBlogBySlug(slug);

    if (fallbackItem) {
      return buildFallbackBlogDetails(fallbackItem);
    }

    throw error;
  }
}