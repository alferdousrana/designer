import "./ExperienceSection.css";
import { fallbackExperience } from "../../data/fallbackExperience";

function normalizeExperienceData(experienceItems) {
  const items = Array.isArray(experienceItems)
    ? experienceItems
    : Array.isArray(experienceItems?.results)
    ? experienceItems.results
    : [];

  if (items.length === 0) {
    return fallbackExperience;
  }

  const mapped = items
    .filter((item) => item?.is_active !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      year: item.year || item.date || item.label || "0000",
      title: item.title || item.role || item.name || "Untitled Role",
      description:
        item.description ||
        item.short_description ||
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      order: item.order ?? index + 1,
      is_active: item.is_active ?? true,
    }))
    .sort((a, b) => a.order - b.order);

  return mapped.length ? mapped : fallbackExperience;
}

function ExperienceSection({ sectionData, experience }) {
  const safeExperience = normalizeExperienceData(experience);

  const eyebrow = sectionData?.eyebrow || "MY JOURNEY & TRACK RECORD";
  const titleLight = sectionData?.title_light || "Tons Of";
  const titleAccent = sectionData?.title_accent || "Experiences";
  const experienceImage = sectionData?.experience_image || "";

  return (
    <section className="experience-section" id="experience">
      <div className="container experience-grid">
        <div className="experience-image-col">
          {experienceImage ? (
            <img
              src={experienceImage}
              alt={titleAccent || "Experience"}
              className="experience-person-image"
            />
          ) : (
            <div className="experience-image-placeholder">No Image</div>
          )}
        </div>

        <div className="experience-content-col">
          <p className="experience-eyebrow">{eyebrow}</p>

          <h2 className="experience-title">
            <span className="experience-title-light">{titleLight}</span>
            <span className="experience-title-accent"> {titleAccent}</span>
          </h2>

          <div className="experience-items-grid">
            {safeExperience.map((item) => (
              <article className="experience-item" key={item.id}>
                <div className="experience-year-wrap">
                  <span className="experience-year">{item.year}</span>
                </div>

                <div className="experience-line" />

                <h3 className="experience-item-title">{item.title}</h3>
                <p className="experience-item-description">{item.description}</p>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

export default ExperienceSection;