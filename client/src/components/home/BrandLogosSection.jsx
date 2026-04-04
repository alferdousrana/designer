import "./BrandLogosSection.css";
import { brandLogos } from "../../data/brandLogos";

function BrandLogosSection() {
  return (
    <section className="brand-logos-section">
      <div className="container">
        <div className="brand-logos-grid">
          {brandLogos.map((brand) => (
            <div className="brand-logo-item" key={brand.id}>
              <img src={brand.image} alt={brand.name} className="brand-logo-image" />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default BrandLogosSection;