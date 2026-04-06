import Header from "../components/common/Header";

function MainLayout({ children, socialLinks }) {
  return (
    <>
      <Header socialLinks={socialLinks} />
      {children}
    </>
  );
}

export default MainLayout;