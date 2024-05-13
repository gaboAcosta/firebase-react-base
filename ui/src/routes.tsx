import { RouteObject } from "react-router-dom";

import Layout from "./components/Layout";
import ErrorView from "./views/Error/ErrorView.tsx";
import NotFound from "./views/Error/NotFoundView.tsx";
import Login from "./views/Login/LoginView.tsx";
import Dashboard from "./views/Dashboard/DashboardView.tsx";

export const publicRoutes: RouteObject = {
  path: "/",
  element: <Layout />,
  errorElement: <ErrorView />,
  children: [
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/login",
      element: <Login />,
    },
    {
      path: "*",
      element: <NotFound />,
    },
  ],
};

export const appRoutes: RouteObject = {
  path: "/app/",
  element: <Layout />,
  errorElement: <ErrorView />,
  children: [
    {
      path: "/app/dashboard",
      element: <Dashboard />,
    },
  ],
};
