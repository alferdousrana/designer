import { Link } from "react-router-dom";

function ProjectCard({ item }) {
  return (
    <article className="project-card">
      <Link to={`/project/${item.slug}`} className="project-card-image-link">
        <img
          src={item.thumbnail || item.coverImage}
          alt={item.title}
          className="project-card-image"
        />
      </Link>

      <div className="project-card-content">
        {item.categoryName && (
          <p className="project-card-category">{item.categoryName}</p>
        )}

        <h2 className="project-card-title">
          <Link to={`/project/${item.slug}`}>{item.title}</Link>
        </h2>

        {item.shortDesc && (
          <p className="project-card-desc">{item.shortDesc}</p>
        )}

        <div className="project-card-meta">
          {item.clientName && <span>{item.clientName}</span>}
          {item.rating && <span>★ {item.rating}</span>}
        </div>
      </div>
    </article>
  );
}

export default ProjectCard;