import { Link } from "react-router-dom";

function BlogHero() {
  return (
    <section className="blog-hero">
      <div className="container">
        <div className="blog-hero-inner">
          <h1 className="blog-hero-title">Blog</h1>

          <div className="blog-breadcrumb">
            <Link to="/">Home</Link>
            <span>›</span>
            <span>Blog</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default BlogHero;