import { Layout } from "antd";
import Header from "./LayoutHeader.tsx";
import LayoutFooter from "./LayoutFooter.tsx";
import PropTypes from "prop-types";

const { Content } = Layout;
type MainLayoutParams = {
  children: React.ReactNode;
};
const MainLayout = ({ children }: MainLayoutParams) => {
  return (
    <Layout>
      <Header />
      <Content className="main-content">{children}</Content>
      <LayoutFooter />
    </Layout>
  );
};

MainLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default MainLayout;
