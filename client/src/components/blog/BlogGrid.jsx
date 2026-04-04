import BlogCard from "./BlogCard";

function BlogGrid({ blogs = [], pagination, currentPage, onPageChange }) {
  const safeBlogs = Array.isArray(blogs) ? blogs : [];

  return (
    <section className="blog-list-section">
      <div className="container">
        <p className="blog-list-label">LATEST POSTS</p>

        <div className="blog-grid">
          {safeBlogs.map((item) => (
            <BlogCard key={item.id || item.slug} item={item} />
          ))}
        </div>

        <div className="blog-pagination">
          <button
            type="button"
            onClick={() => onPageChange(currentPage - 1)}
            disabled={!pagination?.previous}
          >
            Previous
          </button>

          <span>Page {currentPage}</span>

          <button
            type="button"
            onClick={() => onPageChange(currentPage + 1)}
            disabled={!pagination?.next}
          >
            Next
          </button>
        </div>
      </div>
    </section>
  );
}

export default BlogGrid;