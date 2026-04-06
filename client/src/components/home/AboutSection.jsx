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
        hire_me_button_text: "Hire Me",
        hire_me_button_link: "#contact",
        download_cv_text: "Download CV",
        download_cv_link: "#",
        cv_file: null,
        show_play_button: false,
        video_url: null,
      };

  const {
    title,
    subtitle,
    bio,
    profile_image,
    hire_me_button_text,
    hire_me_button_link,
    download_cv_text,
    download_cv_link,
    cv_file,
    show_play_button,
    video_url,
  } = safeAbout;

  const titleParts = (subtitle || "").split(" ");
  const firstLine = titleParts[0] || "Professional";
  const secondLine = titleParts.slice(1).join(" ") || "Experienced";

  const cvLink = cv_file || download_cv_link || "#";
  const playTarget = video_url || "#";

  return (
    <section className="about-v2-section" id="about">
      <div className="container">
        <div className="about-v2-top">
          <div className="about-v2-heading-wrap">
            <p className="about-v2-eyebrow">{title}</p>

            <h2 className="about-v2-title">
              <span className="about-v2-title-light">{firstLine}</span>
              <span className="about-v2-title-accent">
                {secondLine ? ` ${secondLine}` : ""}
              </span>
            </h2>
          </div>

          <div className="about-v2-content">
            <p className="about-v2-bio" style={{ whiteSpace: "pre-line" }}>
              {bio}
            </p>

            <div className="about-v2-actions">
              <a
                href={hire_me_button_link || "#contact"}
                className="about-v2-btn about-v2-btn-primary"
              >
                {hire_me_button_text || "Hire Me"}
              </a>

              <a
                href={cvLink}
                className="about-v2-btn about-v2-btn-link"
                target={cvLink.startsWith("http") ? "_blank" : "_self"}
                rel={cvLink.startsWith("http") ? "noopener noreferrer" : ""}
              >
                {download_cv_text || "Download CV"}
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

          {show_play_button && (
            <a
              href={playTarget}
              className="about-v2-play-btn"
              aria-label="Play video"
              target={video_url ? "_blank" : "_self"}
              rel={video_url ? "noopener noreferrer" : ""}
            >
              ▶
            </a>
          )}
        </div>
      </div>
    </section>
  );
}

export default AboutSection;