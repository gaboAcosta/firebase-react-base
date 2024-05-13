import { ReactNode } from "react";
import { Typography } from "antd";

const { Title } = Typography;

interface LayoutParams {
  children: ReactNode;
  title?: string;
  outerTittle?: string;
}

const LayoutContent = (params: LayoutParams) => {
  const { children, title = null, outerTittle = null } = params;

  return (
    <div className="main-container">
      {outerTittle?.length && (
        <Title className="section-title">{outerTittle}</Title>
      )}
      <div className="white-box">
        <div className="white-box-content">
          {title && <Title>{title}</Title>}
          {children}
        </div>
      </div>
    </div>
  );
};

export default LayoutContent;
