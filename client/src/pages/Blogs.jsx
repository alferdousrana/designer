import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import useBlogs from "../hooks/useBlogs";
import useHomeData from "../hooks/useHomeData";
import BlogHero from "../components/blog/BlogHero";
import BlogGrid from "../components/blog/BlogGrid";
import "../components/blog/BlogPage.css";

function Blogs() {
  const [page, setPage] = useState(1);
  const { blogs, pagination, loading, error } = useBlogs(page);
  const { homeData } = useHomeData();

  function handlePageChange(nextPage) {
    if (nextPage < 1) return;
    setPage(nextPage);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <BlogHero />

      {loading && (
        <main className="container page-state">
          <p>Loading blog posts...</p>
        </main>
      )}

      {!loading && (
        <>
          {error && (
            <div className="container page-state">
              <p>{error}</p>
            </div>
          )}

          <BlogGrid
            blogs={blogs}
            pagination={pagination}
            currentPage={page}
            onPageChange={handlePageChange}
          />
        </>
      )}
    </MainLayout>
  );
}

export default Blogs;