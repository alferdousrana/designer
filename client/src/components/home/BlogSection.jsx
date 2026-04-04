import "./BlogSection.css";
import { fallbackBlogs } from "../../data/fallbackBlogs";
import { Link } from "react-router-dom";

function getBlogImage(blog) {
  return (
    blog?.featured_image ||
    blog?.cover_image ||
    blog?.gallery?.find((item) => item?.is_active !== false)?.image ||
    ""
  );
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
  if (!Array.isArray(blogs) || blogs.length === 0) {
    return fallbackBlogs;
  }

  const mapped = blogs
    .filter((item) => item?.is_active !== false && item?.is_featured !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      title: item.title || "Untitled Blog",
      slug: item.slug || `blog-${index + 1}`,
      published_at: item.published_at || "",
      image: getBlogImage(item),
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
      eyebrow: "👌 LATEST ARTICLES",
      title_light: "My Blog",
      title_accent: "For You",
    };
  }

  return {
    eyebrow: blogSection.eyebrow || "👌 LATEST ARTICLES",
    title_light: blogSection.title_light || "My Blog",
    title_accent: blogSection.title_accent || "For You",
  };
}

function BlogSection({ blogSection, blogs }) {
  const safeSection = normalizeBlogSectionData(blogSection);
  const safeBlogs = normalizeBlogsData(blogs);

  return (
    <section className="blog-section" id="blog">
      <div className="container">
        <div className="blog-heading">
          <p className="blog-eyebrow">{safeSection.eyebrow}</p>
          <h2 className="blog-title">
            <span className="blog-title-light">{safeSection.title_light}</span>
            <span className="blog-title-accent"> {safeSection.title_accent}</span>
          </h2>
        </div>

        <div className="blog-grid">
          {safeBlogs.map((blog) => (
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