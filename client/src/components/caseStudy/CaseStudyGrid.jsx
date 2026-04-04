import CaseStudyCard from "./CaseStudyCard";

function CaseStudyGrid({ caseStudies, pagination, currentPage, onPageChange }) {
  return (
    <section className="case-study-list-section">
      <div className="container">
        <p className="case-study-list-label">LATEST POST</p>

        <div className="case-study-grid">
          {caseStudies.map((item) => (
            <CaseStudyCard key={item.id} item={item} />
          ))}
        </div>

        <div className="case-study-pagination">
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

export default CaseStudyGrid;