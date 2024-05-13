import { useRouteError } from "react-router-dom";
import MainLayout from "../../components/Layout/MainLayout.js";
import LayoutContent from "../../components/Layout/LayoutContent.js";

interface Error {
  message: string;
  stack: string;
}

const ErrorView = () => {
  const error = useRouteError() as Error;
  return (
    <>
      <MainLayout>
        <LayoutContent title="Error">
          <div>Error: {error.message}</div>
          <div>
            Stacktrace:
            <pre>{error.stack}</pre>
          </div>
        </LayoutContent>
      </MainLayout>
    </>
  );
};

export default ErrorView;
