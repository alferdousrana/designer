import "./BlogSection.css";
import { fallbackBlogs } from "../../data/fallbackBlogs";

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

function BlogSection({ blogs }) {
  const safeBlogs = normalizeBlogsData(blogs);

  return (
    <section className="blog-section" id="blog">
      <div className="container">
        <div className="blog-heading">
          <p className="blog-eyebrow">👌 LATEST ARTICLES</p>
          <h2 className="blog-title">
            <span className="blog-title-light">My Blog</span>
            <span className="blog-title-accent"> For You</span>
          </h2>
        </div>

        <div className="blog-grid">
          {safeBlogs.map((blog) => (
            <article className="blog-card" key={blog.id}>
              <a href={`/blog/${blog.slug}`} className="blog-image-link">
                <img src={blog.image} alt={blog.title} className="blog-image" />
              </a>

              <div className="blog-content">
                <h3 className="blog-card-title">
                  <a href={`/blog/${blog.slug}`}>{blog.title}</a>
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