import { useMemo } from "react";
import { Link, useParams } from "react-router-dom";
import useBlogDetails from "../../hooks/useBlogDetails";
import "./BlogDetailsPage.css";

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

function getPlainText(htmlString) {
  if (!htmlString) return "";
  return htmlString.replace(/<[^>]*>/g, "").trim();
}

function getSafeHtml(content) {
  if (!content) return { __html: "" };
  const hasHtmlTag = /<\/?[a-z][\s\S]*>/i.test(content);
  return { __html: hasHtmlTag ? content : `<p>${content}</p>` };
}

function buildTableOfContents(blog) {
  const items = [];

  if (blog?.content) {
    items.push({ id: "content", label: "Content" });
  }

  blog?.sections?.forEach((section) => {
    items.push({
      id: `section-${section.id}`,
      label: section.title || "Section",
    });
  });

  return items;
}

function GalleryItem({ item }) {
  return (
    <figure className="blog-gallery-item">
      <img src={item.image} alt={item.altText} />
      {item.caption && <figcaption>{item.caption}</figcaption>}
    </figure>
  );
}

function ContentSection({ id, title, content, image }) {
  const plainText = getPlainText(content);

  if (!title && !plainText && !image) return null;

  return (
    <section id={id} className="blog-content-block">
      {title && <h2 className="blog-section-title">{title}</h2>}

      {plainText && (
        <div
          className="blog-rich-text"
          dangerouslySetInnerHTML={getSafeHtml(content)}
        />
      )}

      {image && (
        <div className="blog-inline-image">
          <img src={image} alt={title || "Blog section"} />
        </div>
      )}
    </section>
  );
}

function BlogDetailsPage() {
  const { slug } = useParams();
  const { blog, loading, error } = useBlogDetails(slug);

  const tableOfContents = useMemo(() => buildTableOfContents(blog), [blog]);

  if (loading) {
    return (
      <main className="blog-details-page">
        <div className="container page-state">
          <p>Loading blog details...</p>
        </div>
      </main>
    );
  }

  if (error || !blog) {
    return (
      <main className="blog-details-page">
        <div className="container page-state">
          <p>{error || "Blog post not found."}</p>
        </div>
      </main>
    );
  }

  return (
    <main className="blog-details-page">
      <section className="blog-details-hero">
        <div className="container blog-details-shell">
          <div className="blog-details-header">
            <div className="blog-details-breadcrumb">
              <Link to="/">Home</Link>
              <span>/</span>
              <Link to="/blog">Blog</Link>
              <span>/</span>
              <span>{blog.title}</span>
            </div>

            {blog.categoryName && (
              <p className="blog-details-category">{blog.categoryName}</p>
            )}

            <h1 className="blog-details-title">{blog.title}</h1>

            <div className="blog-details-meta">
              <span>By {blog.authorName || "Admin"}</span>
              <span>•</span>
              <span>{formatDate(blog.publishedAt)}</span>
              {blog.readTime ? (
                <>
                  <span>•</span>
                  <span>{blog.readTime} min read</span>
                </>
              ) : null}
            </div>

            {blog.excerpt && (
              <p className="blog-details-summary">{blog.excerpt}</p>
            )}
          </div>

          {blog.coverImage && (
            <div className="blog-cover-wrap">
              <img
                src={blog.coverImage}
                alt={blog.title}
                className="blog-cover-image"
              />
            </div>
          )}
        </div>
      </section>

      <section className="blog-body-section">
        <div className="container blog-details-shell">
          <aside className="blog-sidebar">
            {tableOfContents.length > 0 && (
              <div className="blog-sidebar-card">
                <h3>Table Of Contents</h3>

                <ul className="blog-toc">
                  {tableOfContents.map((item) => (
                    <li key={item.id}>
                      <a href={`#${item.id}`}>{item.label}</a>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="blog-sidebar-card">
              <h3>Post Info</h3>

              <div className="blog-info-list">
                {blog.categoryName && (
                  <div className="blog-info-item">
                    <span className="blog-info-label">Category</span>
                    <span className="blog-info-value">{blog.categoryName}</span>
                  </div>
                )}

                {blog.authorName && (
                  <div className="blog-info-item">
                    <span className="blog-info-label">Author</span>
                    <span className="blog-info-value">{blog.authorName}</span>
                  </div>
                )}

                {blog.readTime ? (
                  <div className="blog-info-item">
                    <span className="blog-info-label">Read Time</span>
                    <span className="blog-info-value">{blog.readTime} min</span>
                  </div>
                ) : null}

                {blog.viewCount ? (
                  <div className="blog-info-item">
                    <span className="blog-info-label">Views</span>
                    <span className="blog-info-value">{blog.viewCount}</span>
                  </div>
                ) : null}
              </div>
            </div>

            {blog.keywordList.length > 0 && (
              <div className="blog-sidebar-card">
                <h3>Keywords</h3>

                <div className="blog-tag-list">
                  {blog.keywordList.map((keyword) => (
                    <span key={keyword} className="blog-tag">
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {blog.tags.length > 0 && (
              <div className="blog-sidebar-card">
                <h3>Tags</h3>

                <div className="blog-tag-list">
                  {blog.tags.map((tag) => (
                    <span key={tag.id || tag.slug || tag.name} className="blog-tag">
                      {tag.name}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </aside>

          <div className="blog-main-content">
            <ContentSection
              id="content"
              title="Article Content"
              content={blog.content}
            />

            {blog.sections.map((section) => (
              <ContentSection
                key={section.id}
                id={`section-${section.id}`}
                title={section.title}
                content={section.content}
                image={section.image}
              />
            ))}

            {blog.gallery.length > 0 && (
              <section className="blog-gallery-section">
                <h2 className="blog-section-title">Gallery</h2>

                <div className="blog-gallery-grid">
                  {blog.gallery.map((item) => (
                    <GalleryItem key={item.id} item={item} />
                  ))}
                </div>
              </section>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}

export default BlogDetailsPage;