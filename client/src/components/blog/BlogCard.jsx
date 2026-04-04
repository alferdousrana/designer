import { Link } from "react-router-dom";

function formatDate(dateString) {
  if (!dateString) return "June 18, 2021";

  const date = new Date(dateString);
  if (Number.isNaN(date.getTime())) return "June 18, 2021";

  return date.toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
  });
}

function getBlogImage(item) {
  return (
    item?.featuredImage ||
    item?.coverImage ||
    item?.featured_image ||
    item?.cover_image ||
    ""
  );
}

function getBlogDate(item) {
  return item?.publishedAt || item?.published_at || "";
}

function getBlogAuthor(item) {
  return item?.authorName || item?.author_name || "Admin";
}

function getBlogExcerpt(item) {
  return item?.excerpt || "";
}

function getBlogCategory(item) {
  return item?.categoryName || item?.category?.name || "";
}

function BlogCard({ item }) {
  const image = getBlogImage(item);
  const publishedDate = getBlogDate(item);
  const author = getBlogAuthor(item);
  const excerpt = getBlogExcerpt(item);
  const category = getBlogCategory(item);

  return (
    <article className="blog-card">
      <Link to={`/blog/${item.slug}`} className="blog-card-image-link">
        <img src={image} alt={item.title} className="blog-image" />
      </Link>

      <div className="blog-card-content">
        {category && <p className="blog-card-category">{category}</p>}

        <h2 className="blog-card-title">
          <Link to={`/blog/${item.slug}`}>{item.title}</Link>
        </h2>

        <p className="blog-card-meta">
          {formatDate(publishedDate)} / {author}
        </p>

        {excerpt && <p className="blog-card-excerpt">{excerpt}</p>}
      </div>
    </article>
  );
}

export default BlogCard;