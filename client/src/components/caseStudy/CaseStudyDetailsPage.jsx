import { useMemo } from "react";
import { Link, useParams } from "react-router-dom";
import useCaseStudyDetails from "../../hooks/useCaseStudyDetails";
import "./CaseStudyDetailsPage.css";
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

function getPlainText(htmlString) {
  if (!htmlString) return "";
  return htmlString.replace(/<[^>]*>/g, "").trim();
}

function renderHtml(content) {
  return { __html: content || "" };
}

function fixImageUrls(htmlString) {
  if (!htmlString) return "";

  return htmlString.replace(
    /src="\/media\//g,
    `src="${BASE_URL}/media/`
  );
}

function buildTableOfContents(caseStudy) {
  const items = [];

  if (caseStudy?.overview) {
    items.push({ id: "overview", label: "Overview" });
  }

  if (caseStudy?.challenge) {
    items.push({ id: "challenge", label: "Challenge" });
  }

  if (caseStudy?.goal) {
    items.push({ id: "goal", label: "Goal" });
  }

  if (caseStudy?.process) {
    items.push({ id: "process", label: "Process" });
  }

  if (caseStudy?.solution) {
    items.push({ id: "solution", label: "Solution" });
  }

  if (caseStudy?.outcome) {
    items.push({ id: "outcome", label: "Outcome" });
  }

  caseStudy?.sections?.forEach((section) => {
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
    <div className="case-study-info-item">
      <span className="case-study-info-label">{label}</span>
      <span className="case-study-info-value">{value}</span>
    </div>
  );
}

function MetricCard({ item }) {
  return (
    <div className="case-study-metric-card">
      <h3>{item.value}</h3>
      <p>{item.label}</p>
    </div>
  );
}

function GalleryItem({ item }) {
  return (
    <figure className="case-study-gallery-item">
      <img src={item.image} alt={item.altText} />
      {item.caption && <figcaption>{item.caption}</figcaption>}
    </figure>
  );
}

function ContentSection({ id, title, content, image }) {
  const fixedContent = fixImageUrls(content);
  const plainText = getPlainText(fixedContent);

  if (!title && !plainText && !image) return null;

  return (
    <section id={id} className="case-study-content-block">
      {title && <h2 className="case-study-section-title">{title}</h2>}

      {plainText && (
        <div
          className="case-study-rich-text"
          dangerouslySetInnerHTML={renderHtml(fixedContent)}
        />
      )}

      {image && (
        <div className="case-study-inline-image">
          <img
            src={image.startsWith("http") ? image : `${BASE_URL}${image}`}
            alt={title || "Case study section"}
          />
        </div>
      )}
    </section>
  );
}
function CaseStudyDetailsPage() {
  const { slug } = useParams();
  const { caseStudy, loading, error } = useCaseStudyDetails(slug);

  const tableOfContents = useMemo(
    () => buildTableOfContents(caseStudy),
    [caseStudy]
  );

  if (loading) {
    return (
      <main className="case-study-details-page">
        <div className="container page-state">
          <p>Loading case study details...</p>
        </div>
      </main>
    );
  }

  if (error || !caseStudy) {
    return (
      <main className="case-study-details-page">
        <div className="container page-state">
          <p>{error || "Case study not found."}</p>
        </div>
      </main>
    );
  }

  return (
    <main className="case-study-details-page">
      <section className="case-study-details-hero">
        <div className="container case-study-details-shell">
          <div className="case-study-details-header">
            <div className="case-study-details-breadcrumb">
              <Link to="/">Home</Link>
              <span>/</span>
              <Link to="/case-study">Case Study</Link>
              <span>/</span>
              <span>{caseStudy.title}</span>
            </div>

            <h1 className="case-study-details-title">{caseStudy.title}</h1>

            <div className="case-study-details-meta">
              <span>By Admin</span>
              <span>•</span>
              <span>{formatDate(caseStudy.publishedAt)}</span>
              {caseStudy.readTime ? (
                <>
                  <span>•</span>
                  <span>{caseStudy.readTime} min read</span>
                </>
              ) : null}
            </div>

            {caseStudy.shortDesc && (
              <p className="case-study-details-summary">{caseStudy.shortDesc}</p>
            )}
          </div>

          {caseStudy.coverImage && (
            <div className="case-study-cover-wrap">
              <img
                src={caseStudy.coverImage}
                alt={caseStudy.title}
                className="case-study-cover-image"
              />
            </div>
          )}
        </div>
      </section>

      <section className="case-study-body-section">
        <div className="container case-study-details-shell">
          <aside className="case-study-sidebar">
            {tableOfContents.length > 0 && (
              <div className="case-study-sidebar-card">
                <h3>Table Of Contents</h3>

                <ul className="case-study-toc">
                  {tableOfContents.map((item) => (
                    <li key={item.id}>
                      <a href={`#${item.id}`}>{item.label}</a>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="case-study-sidebar-card">
              <h3>Project Info</h3>

              <div className="case-study-info-list">
                <InfoItem label="Project" value={caseStudy.projectName} />
                <InfoItem label="Client" value={caseStudy.clientName} />
                <InfoItem label="Industry" value={caseStudy.industry} />
                <InfoItem label="Role" value={caseStudy.myRole} />
                <InfoItem label="Team" value={caseStudy.team} />
                <InfoItem label="Timeline" value={caseStudy.timeline} />
              </div>
            </div>

            {caseStudy.toolsList.length > 0 && (
              <div className="case-study-sidebar-card">
                <h3>Tools</h3>

                <div className="case-study-tag-list">
                  {caseStudy.toolsList.map((tool) => (
                    <span key={tool} className="case-study-tag">
                      {tool}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {caseStudy.keywordList.length > 0 && (
              <div className="case-study-sidebar-card">
                <h3>Keywords</h3>

                <div className="case-study-tag-list">
                  {caseStudy.keywordList.map((keyword) => (
                    <span key={keyword} className="case-study-tag">
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </aside>

          <div className="case-study-main-content">
            {caseStudy.metrics.length > 0 && (
              <section className="case-study-metrics-grid">
                {caseStudy.metrics.map((item) => (
                  <MetricCard key={item.id} item={item} />
                ))}
              </section>
            )}

            <ContentSection
              id="overview"
              title="Overview"
              content={caseStudy.overview}
            />

            <ContentSection
              id="challenge"
              title="Challenge"
              content={caseStudy.challenge}
            />

            <ContentSection id="goal" title="Goal" content={caseStudy.goal} />

            <ContentSection
              id="process"
              title="Process"
              content={caseStudy.process}
            />

            <ContentSection
              id="solution"
              title="Solution"
              content={caseStudy.solution}
            />

            <ContentSection
              id="outcome"
              title="Outcome"
              content={caseStudy.outcome}
            />

            {caseStudy.sections.map((section) => (
              <ContentSection
                key={section.id}
                id={`section-${section.id}`}
                title={section.title}
                content={section.content}
                image={section.image}
              />
            ))}

            {caseStudy.gallery.length > 0 && (
              <section className="case-study-gallery-section">
                <h2 className="case-study-section-title">Gallery</h2>

                <div className="case-study-gallery-grid">
                  {caseStudy.gallery.map((item) => (
                    <GalleryItem key={item.id} item={item} />
                  ))}
                </div>
              </section>
            )}

            <div className="case-study-action-row">
              {caseStudy.liveUrl && (
                <a
                  href={caseStudy.liveUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="case-study-action-btn"
                >
                  Live Preview
                </a>
              )}

              {caseStudy.prototypeUrl && (
                <a
                  href={caseStudy.prototypeUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="case-study-action-btn"
                >
                  Prototype
                </a>
              )}

              {caseStudy.figmaUrl && (
                <a
                  href={caseStudy.figmaUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="case-study-action-btn"
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

export default CaseStudyDetailsPage;