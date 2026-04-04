import { Link } from "react-router-dom";

function ProjectHero() {
  return (
    <section className="project-hero">
      <div className="container">
        <div className="project-hero-inner">
          <h1 className="project-hero-title">Projects</h1>

          <div className="project-breadcrumb">
            <Link to="/">Home</Link>
            <span>›</span>
            <span>Projects</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default ProjectHero;