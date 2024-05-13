import { Link } from "react-router-dom";
import { Layout, Grid, Button } from "antd";
import AuthenticationService from "../../services/AuthenticationService";

const { Header: AntHeader } = Layout;
const { useBreakpoint } = Grid;

const Header = () => {
  const screens = useBreakpoint();

  const logout = async () => {
    await AuthenticationService.logout();
  };

  return (
    <>
      <AntHeader
        className={`app-header ${screens?.lg && "app-header-big-screen"}`}
      >
        <div className={"app-header-container"}>
          <div className="logo">
            <Link to="/"></Link>
          </div>
          <div>
            <Button onClick={logout}>Log out</Button>
          </div>
        </div>
      </AntHeader>
    </>
  );
};

export default Header;
