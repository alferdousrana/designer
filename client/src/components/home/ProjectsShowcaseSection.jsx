import "./ProjectsShowcaseSection.css";
import { fallbackProjects } from "../../data/fallbackProjects";

function getProjectImage(project) {
  return (
    project?.cover_image ||
    project?.thumbnail ||
    project?.gallery?.find((item) => item?.is_active !== false)?.image ||
    ""
  );
}

function getProjectClient(project) {
  return (
    project?.client_name ||
    project?.client ||
    project?.client_company ||
    project?.sections?.find((item) =>
      item?.title?.toLowerCase().includes("client")
    )?.content ||
    "Client Name"
  );
}

function getProjectRating(project) {
  return (
    project?.rating ||
    project?.metrics?.find((item) =>
      item?.label?.toLowerCase().includes("rating")
    )?.value ||
    "4.8"
  );
}

function normalizeProjectsData(projects) {
  if (!Array.isArray(projects) || projects.length === 0) {
    return fallbackProjects;
  }

  const mapped = projects
    .filter((item) => item?.is_active !== false && item?.is_featured !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      title: item.title || "Untitled Project",
      slug: item.slug || `project-${index + 1}`,
      category: {
        name: item?.category?.name || "Project Category",
      },
      short_desc:
        item.short_desc ||
        item.overview ||
        "Fusce mollis sem eu ligula ornare, ut molestie eros volutpat. Praesent condimentum, libero id tincidunt tincidunt, neque ex ultrices purus, interdum gravida enim sapien ac urna.",
      image: getProjectImage(item),
      client_name: getProjectClient(item),
      rating: getProjectRating(item),
      live_url: item.live_url || item.behance_url || item.figma_url || "#",
      order: item.order ?? index + 1,
      is_active: item.is_active ?? true,
      is_featured: item.is_featured ?? true,
    }))
    .sort((a, b) => a.order - b.order);

  return mapped.length ? mapped : fallbackProjects;
}

function renderStars() {
  return "★★★★★";
}

function ProjectsShowcaseSection({ projects }) {
  const safeProjects = normalizeProjectsData(projects);

  return (
    <section className="projects-showcase-section" id="projects">
      <div className="container">
        <div className="projects-showcase-heading">
          <p className="projects-showcase-eyebrow">👌 SHOW CASE</p>
          <h2 className="projects-showcase-title">
            <span className="projects-showcase-title-light">Discover</span>
            <span className="projects-showcase-title-accent"> How I Work</span>
          </h2>
        </div>

        <div className="projects-showcase-list">
          {safeProjects.map((project, index) => {
            const isReverse = index % 2 === 1;

            return (
              <article
                className={`project-showcase-item ${
                  isReverse ? "project-showcase-reverse" : ""
                }`}
                key={project.id}
              >
                <div className="project-showcase-image-wrap">
                  <img
                    src={project.image}
                    alt={project.title}
                    className="project-showcase-image"
                  />
                </div>

                <div className="project-showcase-content">
                  <div className="project-showcase-meta">
                    <p className="project-showcase-label">PROJECT CATEGORY</p>
                    <h3 className="project-showcase-name">{project.title}</h3>
                  </div>

                  <div className="project-showcase-meta">
                    <p className="project-showcase-label">SHORT DESCRIPTION</p>
                    <p className="project-showcase-description">
                      {project.short_desc}
                    </p>
                  </div>

                  <div className="project-showcase-meta">
                    <p className="project-showcase-label">CLIENT</p>
                    <h4 className="project-showcase-client">
                      {project.client_name}
                    </h4>
                  </div>

                  <div className="project-showcase-divider" />

                  <div className="project-showcase-footer">
                    <div className="project-showcase-rating">
                      <span>({project.rating})</span>
                      <span className="project-showcase-stars">
                        {renderStars()}
                      </span>
                    </div>

                    <a
                      href={project.live_url}
                      className="project-showcase-link"
                      target="_blank"
                      rel="noreferrer"
                    >
                      Showcase
                    </a>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default ProjectsShowcaseSection;