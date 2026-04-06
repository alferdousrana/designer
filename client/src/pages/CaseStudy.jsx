import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import useHomeData from "../hooks/useHomeData";
import useCaseStudies from "../hooks/useCaseStudies";
import CaseStudyHero from "../components/caseStudy/CaseStudyHero";
import CaseStudyGrid from "../components/caseStudy/CaseStudyGrid";
import "../components/caseStudy/CaseStudyPage.css";

function CaseStudy() {
  const [page, setPage] = useState(1);
  const { caseStudies, pagination, loading, error } = useCaseStudies(page);
  const { homeData } = useHomeData();

  function handlePageChange(nextPage) {
    if (nextPage < 1) return;
    setPage(nextPage);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <CaseStudyHero />

      {loading && (
        <main className="container page-state">
          <p>Loading case studies...</p>
        </main>
      )}

      {!loading && (
        <>
          {error && (
            <div className="container page-state">
              <p>{error}</p>
            </div>
          )}

          <CaseStudyGrid
            caseStudies={caseStudies}
            pagination={pagination}
            currentPage={page}
            onPageChange={handlePageChange}
          />
        </>
      )}
    </MainLayout>
  );
}

export default CaseStudy;