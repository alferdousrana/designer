import "./SkillsSection.css";
import { fallbackSkills } from "../../data/fallbackSkills";

function normalizeSkillsData(skills) {
  if (!Array.isArray(skills) || skills.length === 0) {
    return fallbackSkills;
  }

  const mappedSkills = skills
    .filter((item) => item?.is_active !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,

      // future backend ready
      number:
        item.number ||
        `${String(item.order ?? index + 1).padStart(2, "0")}.`,

      // future title field, fallback to old name field
      title: item.title || item.name || "Untitled Skill",

      // future description field, fallback to generated text
      description:
        item.description ||
        item.short_description ||
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.",

      // future project link support
      project_link: item.project_link || "#",
      project_link_text: item.project_link_text || "See Past Work",

      order: item.order ?? index + 1,
      is_active: item.is_active ?? true,
    }))
    .sort((a, b) => a.order - b.order);

  return mappedSkills.length ? mappedSkills : fallbackSkills;
}

function SkillsSection({ skills }) {
  const safeSkills = normalizeSkillsData(skills);

  return (
    <section className="skills-section" id="skills">
      <div className="container">
        <div className="skills-heading">
          <p className="skills-eyebrow">🗓️ WHAT I DO</p>
          <h2 className="skills-title">
            <span className="skills-title-light">My</span>
            <span className="skills-title-accent"> Skillset</span>
          </h2>
        </div>

        <div className="skills-grid">
          {safeSkills.map((skill) => (
            <article className="skill-card" key={skill.id}>
              <div className="skill-card-top">
                <span className="skill-number">{skill.number}</span>
                <h3 className="skill-name">{skill.title}</h3>
              </div>

              <div className="skill-divider" />

              <p className="skill-description">{skill.description}</p>

              <a href={skill.project_link} className="skill-link">
                {skill.project_link_text}
              </a>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default SkillsSection;