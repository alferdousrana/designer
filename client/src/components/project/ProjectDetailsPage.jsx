import { useMemo } from "react";
import { Link, useParams } from "react-router-dom";
import useProjectDetails from "../../hooks/useProjectDetails";
import "./ProjectDetailsPage.css";
const BASE_URL = import.meta.env.VITE_API_BASE_URL;

function formatDate(dateString) {
  if (!dateString) return "June 18, 2021";

  const date = new Date(dateString);
  if (Number.isNaN(date.getTime())) return "June 18, 2021";

  return date.toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
  });
}

function fixImageUrls(htmlString) {
  if (!htmlString) return "";

  return htmlString.replace(
    /src="\/media\//g,
    `src="${BASE_URL}/media/`
  );
}

function getPlainText(htmlString) {
  if (!htmlString) return "";
  return htmlString.replace(/<[^>]*>/g, "").trim();
}

function getSafeHtml(content) {
  if (!content) return { __html: "" };

  const fixedContent = fixImageUrls(content);

  const hasHtmlTag = /<\/?[a-z][\s\S]*>/i.test(fixedContent);

  return {
    __html: hasHtmlTag ? fixedContent : `<p>${fixedContent}</p>`,
  };
}

function buildTableOfContents(project) {
  const items = [];

  if (project?.overview) items.push({ id: "overview", label: "Overview" });
  if (project?.challenge) items.push({ id: "challenge", label: "Challenge" });
  if (project?.goal) items.push({ id: "goal", label: "Goal" });
  if (project?.process) items.push({ id: "process", label: "Process" });
  if (project?.solution) items.push({ id: "solution", label: "Solution" });
  if (project?.outcome) items.push({ id: "outcome", label: "Outcome" });

  project?.sections?.forEach((section) => {
    items.push({
      id: `section-${section.id}`,
      label: section.title || "Section",
    });
  });

  return items;
}

function InfoItem({ label, value }) {
  if (!value) return null;

  return (
    <div className="project-info-item">
      <span className="project-info-label">{label}</span>
      <span className="project-info-value">{value}</span>
    </div>
  );
}

function MetricCard({ item }) {
  return (
    <div className="project-metric-card">
      <h3>{item.value}</h3>
      <p>{item.label}</p>
    </div>
  );
}

function GalleryItem({ item }) {
  return (
    <figure className="project-gallery-item">
      <img src={item.image} alt={item.altText} />
      {item.caption && <figcaption>{item.caption}</figcaption>}
    </figure>
  );
}

function ContentSection({ id, title, content, image }) {
  const plainText = getPlainText(content);

  if (!title && !plainText && !image) return null;

  return (
    <section id={id} className="project-content-block">
      {title && <h2 className="project-section-title">{title}</h2>}

      {plainText && (
        <div
          className="project-rich-text"
          dangerouslySetInnerHTML={getSafeHtml(content)}
        />
      )}

      {image && (
        <div className="project-inline-image">
          <img src={image} alt={title || "Project section"} />
        </div>
      )}
    </section>
  );
}

function ProjectDetailsPage() {
  const { slug } = useParams();
  const { project, loading, error } = useProjectDetails(slug);

  const tableOfContents = useMemo(() => buildTableOfContents(project), [project]);

  if (loading) {
    return (
      <main className="project-details-page">
        <div className="container page-state">
          <p>Loading project details...</p>
        </div>
      </main>
    );
  }

  if (error || !project) {
    return (
      <main className="project-details-page">
        <div className="container page-state">
          <p>{error || "Project not found."}</p>
        </div>
      </main>
    );
  }

  return (
    <main className="project-details-page">
      <section className="project-details-hero">
        <div className="container project-details-shell">
          <div className="project-details-header">
            <div className="project-details-breadcrumb">
              <Link to="/">Home</Link>
              <span>/</span>
              <Link to="/project">Projects</Link>
              <span>/</span>
              <span>{project.title}</span>
            </div>

            {project.categoryName && (
              <p className="project-details-category">{project.categoryName}</p>
            )}

            <h1 className="project-details-title">{project.title}</h1>

            <div className="project-details-meta">
              <span>{formatDate(project.publishedAt)}</span>
              {project.readTime ? (
                <>
                  <span>•</span>
                  <span>{project.readTime} min read</span>
                </>
              ) : null}
              {project.viewCount ? (
                <>
                  <span>•</span>
                  <span>{project.viewCount} views</span>
                </>
              ) : null}
            </div>

            {project.shortDesc && (
              <p className="project-details-summary">{project.shortDesc}</p>
            )}
          </div>

          {project.coverImage && (
            <div className="project-cover-wrap">
              <img
                src={project.coverImage}
                alt={project.title}
                className="project-cover-image"
              />
            </div>
          )}
        </div>
      </section>

      <section className="project-body-section">
        <div className="container project-details-shell">
          <aside className="project-sidebar">
            {tableOfContents.length > 0 && (
              <div className="project-sidebar-card">
                <h3>Table Of Contents</h3>

                <ul className="project-toc">
                  {tableOfContents.map((item) => (
                    <li key={item.id}>
                      <a href={`#${item.id}`}>{item.label}</a>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="project-sidebar-card">
              <h3>Project Info</h3>

              <div className="project-info-list">
                <InfoItem label="Category" value={project.categoryName} />
                <InfoItem label="Client" value={project.clientName} />
                <InfoItem label="Role" value={project.myRole} />
                <InfoItem label="Duration" value={project.duration} />
              </div>
            </div>

            {project.toolsList.length > 0 && (
              <div className="project-sidebar-card">
                <h3>Tools</h3>

                <div className="project-tag-list">
                  {project.toolsList.map((tool) => (
                    <span key={tool} className="project-tag">
                      {tool}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {project.keywordList.length > 0 && (
              <div className="project-sidebar-card">
                <h3>Keywords</h3>

                <div className="project-tag-list">
                  {project.keywordList.map((keyword) => (
                    <span key={keyword} className="project-tag">
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </aside>

          <div className="project-main-content">
            {project.metrics.length > 0 && (
              <section className="project-metrics-grid">
                {project.metrics.map((item) => (
                  <MetricCard key={item.id} item={item} />
                ))}
              </section>
            )}

            <ContentSection
              id="overview"
              title="Overview"
              content={project.overview}
            />

            <ContentSection
              id="challenge"
              title="Challenge"
              content={project.challenge}
            />

            <ContentSection id="goal" title="Goal" content={project.goal} />

            <ContentSection
              id="process"
              title="Process"
              content={project.process}
            />

            <ContentSection
              id="solution"
              title="Solution"
              content={project.solution}
            />

            <ContentSection
              id="outcome"
              title="Outcome"
              content={project.outcome}
            />

            {project.sections.map((section) => (
              <ContentSection
                key={section.id}
                id={`section-${section.id}`}
                title={section.title}
                content={section.content}
                image={section.image}
              />
            ))}

            {project.gallery.length > 0 && (
              <section className="project-gallery-section">
                <h2 className="project-section-title">Gallery</h2>

                <div className="project-gallery-grid">
                  {project.gallery.map((item) => (
                    <GalleryItem key={item.id} item={item} />
                  ))}
                </div>
              </section>
            )}

            <div className="project-action-row">
              {project.liveUrl && (
                <a
                  href={project.liveUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="project-action-btn"
                >
                  Live Preview
                </a>
              )}

              {project.behanceUrl && (
                <a
                  href={project.behanceUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="project-action-btn"
                >
                  Behance
                </a>
              )}

              {project.githubUrl && (
                <a
                  href={project.githubUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="project-action-btn"
                >
                  GitHub
                </a>
              )}

              {project.figmaUrl && (
                <a
                  href={project.figmaUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="project-action-btn"
                >
                  Figma File
                </a>
              )}
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}

export default ProjectDetailsPage;