import "./HeroSection.css";

function HeroSection({ hero, about }) {
  const safeHero = hero && hero.is_active ? hero : {};
  const safeAbout = about && about.is_active ? about : {};

  const greeting = safeHero.greeting || "👋 DESIGNING THINGS FOR HUMAN";
  const fullName = safeHero.full_name || "Talented Designer";
  const profession = safeHero.profession || "That Help You";
  const shortBio =
    safeHero.short_bio ||
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.";

  const profileImage = safeHero.profile_image || "";
  const primaryButtonText = safeHero.primary_button_text || "Get Started";
  const primaryButtonLink = safeHero.primary_button_link || "#contact";

  const stats = [
    {
      value: safeAbout.awards ?? 45,
      label: "Awards",
    },
    {
      value: safeAbout.completed_projects ?? 10,
      label: "Projects Finished",
    },
    {
      value: safeAbout.years_of_experience ?? 3,
      label: "Years Experience",
    },
    {
      value: safeAbout.happy_clients ?? 16,
      label: "Happy Clients",
    },
  ];

  return (
    <section className="hero-v2-section" id="hero">
      <div className="container">
        <div className="hero-v2-card">
          <div className="hero-v2-content">
            <p className="hero-v2-greeting">{greeting}</p>

            <h1 className="hero-v2-title">
              <span className="hero-v2-title-light">{fullName}</span>
              <span className="hero-v2-title-accent"> {profession}</span>
            </h1>

            <p className="hero-v2-description">{shortBio}</p>

            <div className="hero-v2-divider" />

            <div className="hero-v2-bottom">
              <div className="hero-v2-stats">
                {stats.map((item) => (
                  <div className="hero-v2-stat" key={item.label}>
                    <h3>{item.value}</h3>
                    <p>{item.label}</p>
                  </div>
                ))}
              </div>

              <a href={primaryButtonLink} className="hero-v2-circle-btn">
                <span>{primaryButtonText}</span>
              </a>
            </div>
          </div>

          <div className="hero-v2-image-wrap">
            {profileImage ? (
              <img
                src={profileImage}
                alt={fullName}
                className="hero-v2-image"
              />
            ) : (
              <div className="hero-v2-image-placeholder">No Image</div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

export default HeroSection;