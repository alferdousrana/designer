import { useEffect, useMemo, useState } from "react";
import "./TestimonialsSection.css";
import { fallbackTestimonials } from "../../data/fallbackTestimonials";

function normalizeTestimonialsData(testimonials) {
  const items = Array.isArray(testimonials)
    ? testimonials
    : Array.isArray(testimonials?.results)
      ? testimonials.results
      : [];

  if (items.length === 0) {
    return fallbackTestimonials;
  }



  const mapped = items
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
  const fullStars = Math.floor(rating);
  const emptyStars = 5 - fullStars;

  return "★".repeat(fullStars) + "☆".repeat(emptyStars);
}

function TestimonialsSection({ sectionData, testimonials }) {
  const safeTestimonials = useMemo(
    () => normalizeTestimonialsData(testimonials),
    [testimonials],
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

  const titleLight = sectionData?.title_light || "Clients";
  const titleAccent = sectionData?.title_accent || "Talking";

  const satisfactionRate = sectionData?.satisfaction_rate || "100%";
  const satisfactionRateLabel =
    sectionData?.satisfaction_rate_label || "Satisfaction Rate";

  const repeatOrderRate = sectionData?.repeat_order_rate || "97%";
  const repeatOrderLabel = sectionData?.repeat_order_label || "Repeat Order";

  const googleReviewRating = sectionData?.google_review_rating || "4.8";
  const googleReviewLabel = sectionData?.google_review_label || "Google Review";

  const hireButtonText = sectionData?.hire_button_text || "Hire Me";
  const hireButtonLink = sectionData?.hire_button_link || "#contact";

  return (
    <section className="testimonials-section" id="testimonials">
      <div className="container">
        <div className="testimonials-heading">
          <h2 className="testimonials-title">
            <span className="testimonials-title-light">{titleLight}</span>
            <span className="testimonials-title-accent"> {titleAccent}</span>
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

                    <div className="testimonial-client-info">
                      <div className="testimonial-name-row">
                        <h3 className="testimonial-name">{item.client_name}</h3>

                        <span className="testimonial-rating">
                          {renderStars(item.rating)}
                        </span>
                      </div>

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
              {safeTestimonials.map((_, index) => (
                <span
                  key={index}
                  className={`testimonial-dot ${
                    index === startIndex ? "active-dot" : ""
                  }`}
                />
              ))}
            </div>
          </div>

          <div className="testimonials-right">
            <div className="testimonial-metric">
              <h3>{satisfactionRate}</h3>
              <p>{satisfactionRateLabel}</p>
            </div>

            <div className="testimonial-metric-divider" />

            <div className="testimonial-metric">
              <h3>{repeatOrderRate}</h3>
              <p>{repeatOrderLabel}</p>
            </div>

            <div className="testimonial-metric-divider" />

            <div className="testimonial-metric">
              <h3>
                {googleReviewRating}{" "}
                <span className="testimonial-stars">
                  {renderStars(googleReviewRating)}
                </span>
              </h3>
              <p>{googleReviewLabel}</p>
            </div>

            <div className="testimonial-metric-divider" />

            <a href={hireButtonLink} className="testimonial-hire-btn">
              {hireButtonText}
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}

export default TestimonialsSection;
