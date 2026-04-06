import "./BrandLogosSection.css";

function BrandLogosSection({ brands }) {
  // handle both API shapes:
  // 1. full response → brands.results
  // 2. direct array → brands
  const brandList = Array.isArray(brands)
    ? brands
    : Array.isArray(brands?.results)
    ? brands.results
    : [];

  const filteredBrands = brandList
    .filter((brand) => brand.is_active)
    .sort((a, b) => a.order - b.order);

  return (
    <section className="brand-logos-section">
      <div className="container">
        <div className="brand-logos-grid">
          {filteredBrands.length > 0 ? (
            filteredBrands.map((brand) => (
              <div className="brand-logo-item" key={brand.id}>
                <img
                  src={brand.image}
                  alt={brand.name}
                  className="brand-logo-image"
                />
              </div>
            ))
          ) : (
            <p className="brand-logos-empty">No brands available</p>
          )}
        </div>
      </div>
    </section>
  );
}

export default BrandLogosSection;