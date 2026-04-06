import "./ProjectsShowcaseSection.css";
import { fallbackProjects } from "../../data/fallbackProjects";
import { Link } from "react-router-dom";

function getProjectImage(project) {
  return project?.thumbnail || project?.cover_image || "";
}

function normalizeProjectsData(projects) {
  const items = Array.isArray(projects)
    ? projects
    : Array.isArray(projects?.results)
    ? projects.results
    : [];

  if (items.length === 0) {
    return fallbackProjects;
  }

  const mapped = items
    .filter((item) => item?.is_active !== false && item?.is_featured !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      title: item.title || "Untitled Project",
      slug: item.slug || `project-${index + 1}`,
      category: item?.category?.name || "Project",
      short_desc:
        item.short_desc ||
        "No description available for this project.",
      image: getProjectImage(item),
      client_name: item?.client_name || "Client",
      rating: item?.rating ?? "4.8",
      live_url: item.live_url || item.behance_url || item.figma_url || "#",
      order: item.order ?? index + 1,
    }))
    .sort((a, b) => a.order - b.order);

  return mapped.length ? mapped : fallbackProjects;
}

function renderStars(rating = 5) {
  const fullStars = Math.floor(rating);
  const emptyStars = 5 - fullStars;

  return "★".repeat(fullStars) + "☆".repeat(emptyStars);
}

function ProjectsShowcaseSection({ sectionData, projects }) {
  const safeProjects = normalizeProjectsData(projects);

  // section API data
  const eyebrow = sectionData?.eyebrow || "SHOW CASE";
  const titleLight = sectionData?.title_light || "Discover";
  const titleAccent = sectionData?.title_accent || "How I Work";
  const maxItems = sectionData?.max_items || safeProjects.length;

  const visibleProjects = safeProjects.slice(0, maxItems);

  return (
    <section className="projects-showcase-section" id="projects">
      <div className="container">
        <div className="projects-showcase-heading">
          <p className="projects-showcase-eyebrow">{eyebrow}</p>

          <h2 className="projects-showcase-title">
            <span className="projects-showcase-title-light">{titleLight}</span>
            <span className="projects-showcase-title-accent">
              {" "}
              {titleAccent}
            </span>
          </h2>
        </div>

        <div className="projects-showcase-list">
          {visibleProjects.map((project, index) => {
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
                    <h3 className="project-showcase-name">
                      {project.title}
                    </h3>
                  </div>

                  <div className="project-showcase-meta">
                    <p className="project-showcase-label">
                      SHORT DESCRIPTION
                    </p>
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
                        {renderStars(project.rating)}
                      </span>
                    </div>

                    <Link
                      to={`/project/${project.slug}`}
                      className="project-showcase-link"
                    >
                      Showcase
                    </Link>
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