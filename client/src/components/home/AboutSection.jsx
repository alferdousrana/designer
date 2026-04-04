import "./AboutSection.css";

function AboutSection({ about }) {
  const hasRealAboutData =
    about &&
    about.is_active &&
    (about.title || about.subtitle || about.bio || about.profile_image);

  const safeAbout = hasRealAboutData
    ? about
    : {
        title: "😎 I WANT TO INTRODUCE MYSELF",
        subtitle: "Professional Experienced",
        bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.",
        profile_image:
          "https://elementor.deverust.com/crevidy/wp-content/uploads/sites/21/2022/05/man-in-eyewear-sitting-at-desk-and-working-on-lapt-MDJ825B.jpg",
      };

  const { title, subtitle, bio, profile_image } = safeAbout;

  const titleParts = subtitle.split(" ");
  const firstLine = titleParts[0] || "Professional";
  const secondLine = titleParts.slice(1).join(" ") || "Experienced";

  return (
    <section className="about-v2-section" id="about">
      <div className="container">
        <div className="about-v2-top">
          <div className="about-v2-heading-wrap">
            <p className="about-v2-eyebrow">{title}</p>

            <h2 className="about-v2-title">
              <span className="about-v2-title-light">{firstLine}</span>
              <span className="about-v2-title-accent">{secondLine}</span>
            </h2>
          </div>

          <div className="about-v2-content">
            <p className="about-v2-bio">{bio}</p>

            <div className="about-v2-actions">
              <a href="#contact" className="about-v2-btn about-v2-btn-primary">
                Hire Me
              </a>

              <a href="#hero" className="about-v2-btn about-v2-btn-link">
                Download CV
              </a>
            </div>
          </div>
        </div>

        <div className="about-v2-media">
          <img
            src={profile_image}
            alt={subtitle || "About"}
            className="about-v2-image"
          />

          <button className="about-v2-play-btn" type="button" aria-label="Play">
            ▶
          </button>
        </div>
      </div>
    </section>
  );
}

export default AboutSection;