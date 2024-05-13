import { Router } from "@remix-run/router";
import { Container } from "react-bootstrap";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
import { publicRoutes, appRoutes } from "./routes.tsx";
import { getUser } from "./utils/session.ts";

function App() {
  const user = getUser();
  const routes = user ? [publicRoutes, appRoutes] : [publicRoutes];
  const router: Router = createBrowserRouter(routes);

  return (
    <Container>
      <RouterProvider router={router} />
    </Container>
  );
}

export default App;
