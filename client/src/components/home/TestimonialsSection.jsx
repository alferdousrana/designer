import { useEffect, useMemo, useState } from "react";
import "./TestimonialsSection.css";
import { fallbackTestimonials } from "../../data/fallbackTestimonials";

function normalizeTestimonialsData(testimonials) {
  if (!Array.isArray(testimonials) || testimonials.length === 0) {
    return fallbackTestimonials;
  }

  const mapped = testimonials
    .filter((item) => item?.is_active !== false)
    .map((item, index) => ({
      id: item.id ?? index + 1,
      client_name: item.client_name || "Anonymous Client",
      client_role: item.client_role || "Client",
      client_company: item.client_company || "",
      client_photo: item.client_photo || "",
      review:
        item.review ||
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.",
      rating: item.rating ?? 5,
      is_featured: item.is_featured ?? false,
      order: item.order ?? index + 1,
      is_active: item.is_active ?? true,
    }))
    .sort((a, b) => a.order - b.order);

  return mapped.length ? mapped : fallbackTestimonials;
}

function renderStars(rating = 5) {
  const fullStars = Math.round(rating);
  return "★".repeat(fullStars);
}

function TestimonialsSection({ testimonials }) {
  const safeTestimonials = useMemo(
    () => normalizeTestimonialsData(testimonials),
    [testimonials]
  );

  const [startIndex, setStartIndex] = useState(0);

  useEffect(() => {
    if (safeTestimonials.length <= 2) return;

    const interval = setInterval(() => {
      setStartIndex((prev) => (prev + 1) % safeTestimonials.length);
    }, 3000);

    return () => clearInterval(interval);
  }, [safeTestimonials]);

  const visibleTestimonials = useMemo(() => {
    if (safeTestimonials.length <= 2) return safeTestimonials;

    return [
      safeTestimonials[startIndex],
      safeTestimonials[(startIndex + 1) % safeTestimonials.length],
    ];
  }, [safeTestimonials, startIndex]);

  return (
    <section className="testimonials-section" id="testimonials">
      <div className="container">
        <div className="testimonials-heading">
          <h2 className="testimonials-title">
            <span className="testimonials-title-light">Clients</span>
            <span className="testimonials-title-accent"> Talking</span>
          </h2>
        </div>

        <div className="testimonials-layout">
          <div className="testimonials-left">
            <div className="testimonials-cards">
              {visibleTestimonials.map((item) => (
                <article className="testimonial-card" key={item.id}>
                  <p className="testimonial-review">{item.review}</p>

                  <div className="testimonial-client">
                    {item.client_photo ? (
                      <img
                        src={item.client_photo}
                        alt={item.client_name}
                        className="testimonial-avatar"
                      />
                    ) : (
                      <div className="testimonial-avatar placeholder-avatar">
                        {item.client_name?.charAt(0)}
                      </div>
                    )}

                    <div>
                      <h3 className="testimonial-name">{item.client_name}</h3>
                      <p className="testimonial-role">
                        {item.client_role}
                        {item.client_company ? `, ${item.client_company}` : ""}
                      </p>
                    </div>
                  </div>
                </article>
              ))}
            </div>

            <div className="testimonial-dots">
              {safeTestimonials.slice(0, 3).map((_, index) => (
                <span
                  key={index}
                  className={`testimonial-dot ${
                    index === (startIndex % 3) ? "active-dot" : ""
                  }`}
                />
              ))}
            </div>
          </div>

          <div className="testimonials-right">
            <div className="testimonial-metric">
              <h3>100%</h3>
              <p>Satisfaction Rate</p>
            </div>

            <div className="testimonial-metric-divider" />

            <div className="testimonial-metric">
              <h3>97%</h3>
              <p>Repeat Order</p>
            </div>

            <div className="testimonial-metric-divider" />

            <div className="testimonial-metric">
              <h3>
                4.8 <span className="testimonial-stars">{renderStars(5)}</span>
              </h3>
              <p>Google Review</p>
            </div>

            <div className="testimonial-metric-divider" />

            <a href="#contact" className="testimonial-hire-btn">
              Hire Me
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}

export default TestimonialsSection;