import MainLayout from "../layouts/MainLayout";
import CaseStudyDetailsPage from "../components/caseStudy/CaseStudyDetailsPage";
import useHomeData from "../hooks/useHomeData";

function CaseStudyDetails() {
  const { homeData } = useHomeData();

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <CaseStudyDetailsPage />
    </MainLayout>
  );
}

export default CaseStudyDetails;