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

function getCardImage(item) {
  return item?.thumbnail || item?.cover_image || "";
}

function CaseStudyCard({ item }) {
  return (
    <article className="case-study-card">
      <a href={`/case-study/${item.slug}`} className="case-study-card-image-link">
        <img
          src={getCardImage(item)}
          alt={item.title}
          className="case-study-card-image"
        />
      </a>

      <div className="case-study-card-content">
        <h2 className="case-study-card-title">
          <a href={`/case-study/${item.slug}`}>{item.title}</a>
        </h2>

        <p className="case-study-card-meta">
          {formatDate(item.published_at)} / No Comments
        </p>
      </div>
    </article>
  );
}

export default CaseStudyCard;