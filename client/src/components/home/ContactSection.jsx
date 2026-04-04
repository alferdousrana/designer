import { useMemo, useState } from "react";
import "./ContactSection.css";

function normalizeContactInfo(contactInfo) {
  if (!contactInfo || contactInfo?.is_active === false) {
    return {
      email: "hello@yoursite.com",
      phone: "+671 873-359-73",
      whatsapp: "",
      location: "",
      availability_text:
        "I help people and teams worldwide. I can help you build your next digital product so feel free to contact me. Sooner you write is better for both of us.",
    };
  }

  return {
    email: contactInfo.email || "hello@yoursite.com",
    phone: contactInfo.phone || "+671 873-359-73",
    whatsapp: contactInfo.whatsapp || "",
    location: contactInfo.location || "",
    availability_text:
      contactInfo.availability_text ||
      "I help people and teams worldwide. I can help you build your next digital product so feel free to contact me. Sooner you write is better for both of us.",
  };
}

function ContactSection({ contactInfo, socialLinks = [], onSubmitContact }) {
  const safeContact = useMemo(
    () => normalizeContactInfo(contactInfo),
    [contactInfo]
  );

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone: "",
    project_type: "",
    message: "",
  });

  const [status, setStatus] = useState({
    loading: false,
    success: "",
    error: "",
  });

  const projectOptions = [
    "UI Design",
    "UI Animation",
    "UX Design",
    "UX Research",
    "Wireframing",
    "Micro Interaction",
    "Design System",
    "All In One",
  ];

  function handleChange(event) {
    const { name, value } = event.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();

    setStatus({
      loading: true,
      success: "",
      error: "",
    });

    const payload = {
      full_name: formData.full_name,
      email: formData.email,
      subject: `New contact from ${formData.full_name || "Website Visitor"}`,
      message: formData.message,
      phone: formData.phone,
      company_name: "",
      budget: "",
      project_type: formData.project_type,
    };

    try {
      if (onSubmitContact) {
        await onSubmitContact(payload);
      }

      setStatus({
        loading: false,
        success: "Message sent successfully.",
        error: "",
      });

      setFormData({
        full_name: "",
        email: "",
        phone: "",
        project_type: "",
        message: "",
      });
    } catch (error) {
      setStatus({
        loading: false,
        success: "",
        error: "Failed to send message. Please try again.",
      });
    }
  }

  return (
    <section className="contact-section" id="contact">
      <div className="container">
        <div className="contact-grid">
          <div className="contact-left">
            <p className="contact-eyebrow">😎 INTERESTED?</p>

            <h2 className="contact-title">
              <span className="contact-title-light">Let&apos;s</span>
              <span className="contact-title-accent"> Connect!</span>
            </h2>

            <p className="contact-description">{safeContact.availability_text}</p>

            <div className="contact-info-list">
              <p>
                <span className="contact-info-icon">✉</span> {safeContact.email}
              </p>
              <p>
                <span className="contact-info-icon">✆</span> {safeContact.phone}
              </p>
            </div>
          </div>

          <div className="contact-right">
            <form className="contact-form" onSubmit={handleSubmit}>
              <div className="contact-form-grid">
                <div className="contact-field">
                  <label htmlFor="full_name">Name</label>
                  <input
                    id="full_name"
                    name="full_name"
                    type="text"
                    placeholder="e.g. John Doe"
                    value={formData.full_name}
                    onChange={handleChange}
                  />
                </div>

                <div className="contact-field">
                  <label htmlFor="email">
                    Email <span>*</span>
                  </label>
                  <input
                    id="email"
                    name="email"
                    type="email"
                    placeholder="e.g. hello@yoursite.com"
                    value={formData.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="contact-field">
                  <label htmlFor="phone">
                    Phone <span>*</span>
                  </label>
                  <input
                    id="phone"
                    name="phone"
                    type="text"
                    placeholder="e.g. +1 373 3783"
                    value={formData.phone}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="contact-field">
                  <label htmlFor="project_type">
                    I&apos;m Interested In <span>*</span>
                  </label>
                  <select
                    id="project_type"
                    name="project_type"
                    value={formData.project_type}
                    onChange={handleChange}
                    required
                  >
                    <option value="">Select</option>
                    {projectOptions.map((option) => (
                      <option key={option} value={option}>
                        {option}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="contact-field contact-field-full">
                  <label htmlFor="message">
                    Tell Me More About Your Goals <span>*</span>
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    rows="5"
                    placeholder="Tell me more about your goals"
                    value={formData.message}
                    onChange={handleChange}
                    required
                  />
                </div>
              </div>

              <button
                className="contact-submit-btn"
                type="submit"
                disabled={status.loading}
              >
                {status.loading ? "Sending..." : "Send"}
              </button>

              {status.success ? (
                <p className="contact-status success-status">{status.success}</p>
              ) : null}

              {status.error ? (
                <p className="contact-status error-status">{status.error}</p>
              ) : null}
            </form>
          </div>
        </div>

        <div className="footer-bar">
          <div className="footer-left">
            <div className="footer-logo">RiJU</div>
            <p className="footer-copy">© 2026 Riju</p>
            <p className="footer-credit">by Afroza Riju</p>
          </div>

          <div className="footer-right">
            {(socialLinks?.length ? socialLinks : []).map((item) => (
              <a key={item.id || item.platform} href={item.url} target="_blank" rel="noreferrer">
                {item.platform_display || item.platform}
              </a>
            ))}

            {!socialLinks?.length && (
              <>
                <a href="/">Dribbble</a>
                <a href="/">Fb</a>
                <a href="/">Ig</a>
                <a href="/">Be</a>
                <a href="/">In</a>
                <a href="/">Ytb</a>
              </>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

export default ContactSection;