import { Link } from "react-router-dom";
import "./Header.css";

function Header({ socialLinks }) {
  const links = Array.isArray(socialLinks)
    ? socialLinks
    : Array.isArray(socialLinks?.results)
    ? socialLinks.results
    : [];

  const filteredLinks = links
    .filter((item) => item?.is_active !== false)
    .sort((a, b) => a.order - b.order);

  return (
    <header className="site-header dark-header">
      <div className="container header-wrapper">
        <div className="logo logo-dark">RiJU</div>

        <nav className="nav-menu nav-menu-dark">
          <Link to="/">Home</Link>
          <Link to="/project">Projects</Link>
          <Link to="/case-study">Case Study</Link>
          <Link to="/blog">Blog</Link>
        </nav>

        <div className="header-social header-social-dark">
          {filteredLinks.length > 0 ? (
            filteredLinks.map((item) => (
              <a
                key={item.id}
                href={item.url}
                target="_blank"
                rel="noreferrer"
              >
                {item.platform_display || item.platform}
              </a>
            ))
          ) : (
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
    </header>
  );
}

export default Header;