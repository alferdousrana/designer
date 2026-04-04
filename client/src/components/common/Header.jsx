import { Link } from "react-router-dom";
import "./Header.css";

function Header() {
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
          <a href="/">Dribbble</a>
          <a href="/">Fb</a>
          <a href="/">Ig</a>
          <a href="/">Be</a>
          <a href="/">In</a>
          <a href="/">Ytb</a>
        </div>
      </div>
    </header>
  );
}

export default Header;