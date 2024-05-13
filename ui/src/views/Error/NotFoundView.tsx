import { Navigate } from "react-router-dom";
const NotFoundView = () => {
  return (
    <>
      <Navigate to="/login" />
    </>
  );
};

export default NotFoundView;
