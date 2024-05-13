import { ReactNode } from "react";
import "./styles.css";

interface LayoutParams {
  children: ReactNode;
  title: string;
}

const LayoutContentTransparentTitle = (params: LayoutParams) => {
  const { title, children } = params;

  return (
    <div className="lctt-header">
      <h3 className="lctt-title">{title}</h3>
      <p className="lctt-description">{children}</p>
    </div>
  );
};

export default LayoutContentTransparentTitle;
