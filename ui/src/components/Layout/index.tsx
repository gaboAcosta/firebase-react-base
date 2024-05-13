import { useEffect } from "react";
import { Outlet } from "react-router-dom";
import MainLayout from "./MainLayout.tsx";
import "./styles.css";
import { ConfigProvider } from "antd";

function PublicLayout() {
  useEffect(() => {
    // set favicon and title for page
    document.title = "Endless Health Admin Portal";
  }, []);
  return (
    <ConfigProvider>
      <MainLayout>
        <Outlet />
      </MainLayout>
    </ConfigProvider>
  );
}

export default PublicLayout;
