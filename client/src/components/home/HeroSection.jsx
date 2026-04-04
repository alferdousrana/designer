import "./HeroSection.css";

function HeroSection({ hero, about }) {
  const safeHero = hero || {};
  const safeAbout = about || {};

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
      value: 45,
      label: "Awards",
    },
    {
      value: safeAbout.completed_projects ?? 345,
      label: "Project Finished",
    },
    {
      value: safeAbout.years_of_experience ?? 12,
      label: "Years Experience",
    },
    {
      value: safeAbout.happy_clients ?? 175,
      label: "Global Clients",
    },
  ];

  return (
    <section className="hero-v2-section" id="hero">
      <div className="container">
        {/* <div className="hero-top-rated">
          <span>Top Rated At</span>
          <div className="hero-badges">
            <span className="hero-badge hero-badge-green">fi</span>
            <span className="hero-badge hero-badge-white">up</span>
          </div>
        </div> */}

        <div className="hero-v2-card">
          <div className="hero-v2-content">
            <p className="hero-v2-greeting">{greeting}</p>

            <h1 className="hero-v2-title">
              <span className="hero-v2-title-light">{fullName}</span>
              <span className="hero-v2-title-accent">{profession}</span>
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