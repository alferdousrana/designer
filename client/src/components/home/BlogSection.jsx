import "./BlogSection.css";
import { fallbackBlogs } from "../../data/fallbackBlogs";
import { Link } from "react-router-dom";

function getBlogImage(blog) {
  return blog?.featured_image || blog?.cover_image || "";
}

function formatBlogDate(dateString) {
  if (!dateString) return "February 7, 2022";

  const date = new Date(dateString);
  if (Number.isNaN(date.getTime())) return "February 7, 2022";

  return date.toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
  });
}

function normalizeBlogsData(blogs) {
  const items = Array.isArray(blogs)
    ? blogs
    : Array.isArray(blogs?.results)
    ? blogs.results
    : [];

  if (items.length === 0) {
    return fallbackBlogs;
  }

  const mapped = items
    .filter((item) => item?.is_active !== false && item?.is_featured !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      title: item.title || "Untitled Blog",
      slug: item.slug || `blog-${index + 1}`,
      published_at: item.published_at || "",
      image: getBlogImage(item),
      excerpt: item.excerpt || "",
      author_name: item.author_name || "Admin",
      category_name: item?.category?.name || "Blog",
      read_time: item.read_time ?? 0,
      order: item.order ?? index + 1,
      is_active: item.is_active ?? true,
      is_featured: item.is_featured ?? true,
    }))
    .sort((a, b) => a.order - b.order);

  return mapped.length ? mapped : fallbackBlogs;
}

function normalizeBlogSectionData(blogSection) {
  if (!blogSection || blogSection?.is_active === false) {
    return {
      eyebrow: "LATEST ARTICLES",
      title_light: "My Blog",
      title_accent: "For You",
      max_items: 4,
    };
  }

  return {
    eyebrow: blogSection.eyebrow || "LATEST ARTICLES",
    title_light: blogSection.title_light || "My Blog",
    title_accent: blogSection.title_accent || "For You",
    max_items: blogSection.max_items || 4,
  };
}

function BlogSection({ blogSection, blogs }) {
  const safeSection = normalizeBlogSectionData(blogSection);
  const safeBlogs = normalizeBlogsData(blogs);
  const visibleBlogs = safeBlogs.slice(0, safeSection.max_items);

  return (
    <section className="blog-section" id="blog">
      <div className="container">
        <div className="blog-heading">
          <p className="blog-eyebrow">{safeSection.eyebrow}</p>

          <h2 className="blog-title">
            <span className="blog-title-light">{safeSection.title_light}</span>
            <span className="blog-title-accent">
              {" "}
              {safeSection.title_accent}
            </span>
          </h2>
        </div>

        <div className="blog-grid">
          {visibleBlogs.map((blog) => (
            <article className="blog-card" key={blog.id}>
              <Link to={`/blog/${blog.slug}`} className="blog-image-link">
                <img src={blog.image} alt={blog.title} className="blog-image" />
              </Link>

              <div className="blog-content">
                <h3 className="blog-card-title">
                  <Link to={`/blog/${blog.slug}`}>{blog.title}</Link>
                </h3>

                <p className="blog-date">{formatBlogDate(blog.published_at)}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default BlogSection;