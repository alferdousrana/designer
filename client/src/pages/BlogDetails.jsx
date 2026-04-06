import MainLayout from "../layouts/MainLayout";
import BlogDetailsPage from "../components/blog/BlogDetailsPage";
import useHomeData from "../hooks/useHomeData";

function BlogDetails() {
  const { homeData } = useHomeData();

  return (
    <MainLayout socialLinks={homeData?.social_links}>
      <BlogDetailsPage />
    </MainLayout>
  );
}

export default BlogDetails;