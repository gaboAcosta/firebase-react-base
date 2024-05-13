import { Typography } from "antd";
import { ReactNode } from "react";

const { Title } = Typography;

interface LayoutParams {
  children: ReactNode;
  outerTittle?: string;
}

const LayoutContentTransparent = (params: LayoutParams) => {
  const { children, outerTittle = null } = params;

  return (
    <div className="main-container">
      {outerTittle?.length && (
        <Title className="section-title">{outerTittle}</Title>
      )}
      <div className="transparent-box">{children}</div>
    </div>
  );
};

export default LayoutContentTransparent;
