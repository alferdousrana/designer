import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import useHomeData from "../hooks/useHomeData";
import useProjects from "../hooks/useProjects";
import ProjectHero from "../components/project/ProjectHero";
import ProjectGrid from "../components/project/ProjectGrid";
import "../components/project/ProjectPage.css";

function Projects() {
  const [page, setPage] = useState(1);
  const { projects, pagination, loading, error } = useProjects(page);
  const { homeData } = useHomeData();

  function handlePageChange(nextPage) {
    if (nextPage < 1) return;
    setPage(nextPage);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <ProjectHero />

      {loading && (
        <main className="container page-state">
          <p>Loading projects...</p>
        </main>
      )}

      {!loading && (
        <>
          {error && (
            <div className="container page-state">
              <p>{error}</p>
            </div>
          )}

          <ProjectGrid
            projects={projects}
            pagination={pagination}
            currentPage={page}
            onPageChange={handlePageChange}
          />
        </>
      )}
    </MainLayout>
  );
}

export default Projects;