import MainLayout from "../layouts/MainLayout";
import ProjectDetailsPage from "../components/project/ProjectDetailsPage";
import useHomeData from "../hooks/useHomeData";

function ProjectDetails() {
  const { homeData } = useHomeData();

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <ProjectDetailsPage />
    </MainLayout>
  );
}

export default ProjectDetails;