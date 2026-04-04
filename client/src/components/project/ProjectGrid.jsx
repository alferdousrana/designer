import ProjectCard from "./ProjectCard";

function ProjectGrid({ projects, pagination, currentPage, onPageChange }) {
  return (
    <section className="project-list-section">
      <div className="container">
        <p className="project-list-label">LATEST PROJECT</p>

        <div className="project-grid">
          {projects.map((item) => (
            <ProjectCard key={item.id} item={item} />
          ))}
        </div>

        <div className="project-pagination">
          <button
            type="button"
            onClick={() => onPageChange(currentPage - 1)}
            disabled={!pagination.previous}
          >
            Previous
          </button>

          <span>Page {currentPage}</span>

          <button
            type="button"
            onClick={() => onPageChange(currentPage + 1)}
            disabled={!pagination.next}
          >
            Next
          </button>
        </div>
      </div>
    </section>
  );
}

export default ProjectGrid;