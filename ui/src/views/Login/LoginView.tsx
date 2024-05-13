import "./styles.css";
import { User } from "firebase/auth";
import AuthenticationService from "../../services/AuthenticationService";
import { BaseSyntheticEvent, useState } from "react";
import { Link } from "react-router-dom";
import { auth, getUser } from "../../utils/firebase";
import LayoutContent from "../../components/Layout/LayoutContent.tsx";
import { Form, Typography, Input, Divider, Button } from "antd";
import {
  checkEmail,
  required,
  minLength,
  whiteSpace,
} from "../../utils/antdFormValidations.ts";
import { signInWithEmailAndPassword } from "firebase/auth";
import { setUser } from "../../utils/session";
const { Item: FormItem } = Form;
const { Text } = Typography;

const Login = () => {
  const [email, setEmail] = useState("");
  const [psw, setPsw] = useState("");

  const handleEmailChange = (e: BaseSyntheticEvent) => {
    setEmail(e.target.value.toLowerCase());
  };

  const onEmailSubmit = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, psw);
      const user: User | null = await getUser();
      if (user === null) {
        return console.error({ message: "Internal error" });
      }
      const token = await user.getIdToken();
      const userData = await AuthenticationService.login(token);
      setUser(userData);

      // using window location to cause a page refresh
      window.location.replace("/app/dashboard");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <LayoutContent title={"Enter registered Email"}>
      <Text>Enter your credentials to login</Text>
      <Form
        name="basic"
        onFinish={onEmailSubmit}
        autoComplete="off"
        layout="vertical"
      >
        <FormItem name="email" rules={[required(), checkEmail()]}>
          <Input
            data-test-id="login-input-email"
            size="large"
            placeholder="Email"
            value={email}
            onChange={handleEmailChange}
          />
        </FormItem>
        <FormItem
          name="password"
          rules={[
            required(),
            minLength(8),
            whiteSpace(),
            () => ({
              pattern: /[!@#$%^&*()\-_=+{};:,<.>]/,
              message: "Password must contain at least one special character.",
            }),
          ]}
        >
          <Input.Password
            data-test-id="login-input-password"
            size="large"
            placeholder="Password"
            value={psw}
            onChange={(e) => setPsw(e.target.value)}
          />
        </FormItem>
        <FormItem>
          <Link
            className="btn-reset-psw"
            to="/forgot-password"
            data-test-id="login-link-forgot"
          >
            Forgot Password
          </Link>
        </FormItem>
        <Button type="primary" htmlType="submit">
          Login
        </Button>
      </Form>

      <Divider />
    </LayoutContent>
  );
};

export default Login;
