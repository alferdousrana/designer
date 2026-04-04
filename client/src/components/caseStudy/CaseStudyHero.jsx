import { Link } from "react-router-dom";

function CaseStudyHero() {
  return (
    <section className="case-study-hero">
      <div className="container">
        <div className="case-study-hero-inner">
          <h1 className="case-study-hero-title">Case Study</h1>

          <div className="case-study-breadcrumb">
            <Link to="/">Home</Link>
            <span>›</span>
            <span>Case Study</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default CaseStudyHero;