import MainLayout from "../layouts/MainLayout";
import useHomeData from "../hooks/useHomeData";
import { submitContactForm } from "../services/api/homeApi";
import HeroSection from "../components/home/HeroSection";
import BrandLogosSection from "../components/home/BrandLogosSection";
import AboutSection from "../components/home/AboutSection";
import SkillsSection from "../components/home/SkillsSection";
import ExperienceSection from "../components/home/ExperienceSection";
import TestimonialsSection from "../components/home/TestimonialsSection";
import ProjectsShowcaseSection from "../components/home/ProjectsShowcaseSection";
import BlogSection from "../components/home/BlogSection";
import ContactSection from "../components/home/ContactSection";

function Home() {
  const { homeData, featuredProjects, featuredBlogs, loading, error } =
    useHomeData();

  async function handleContactSubmit(payload) {
    return submitContactForm(payload);
  }

  return (
    <MainLayout>
      {loading && (
        <main className="container page-state">
          <p>Loading homepage data...</p>
        </main>
      )}

      {!loading && (
        <>
          {error && (
            <div className="container page-state">
              <p>{error}</p>
            </div>
          )}

          <HeroSection hero={homeData?.hero} about={homeData?.about} />
          <BrandLogosSection />
          <AboutSection about={homeData?.about} />
          <SkillsSection skills={homeData?.skills} />
          <ExperienceSection
            experience={homeData?.experience}
            experienceImage={homeData?.experience_image}
          />
          <TestimonialsSection testimonials={homeData?.testimonials} />
          <ProjectsShowcaseSection projects={featuredProjects} />
          <BlogSection blogs={featuredBlogs} />
          <ContactSection
            contactInfo={homeData?.contact_info}
            socialLinks={homeData?.social_links}
            onSubmitContact={handleContactSubmit}
          />
        </>
      )}
    </MainLayout>
  );
}

export default Home;