import { axiosInstance } from "../utils/axiosHelper";
import { endpoints } from "../config";

export interface SignupPayload {
  email: string;
}

class AuthenticationService {
  static async login(accessToken: string) {
    const headers = {
      authorization: `Bearer ${accessToken}`,
    };
    const response = await axiosInstance.post(
      endpoints.session,
      {},
      {
        headers,
      },
    );
    return response.data;
  }
  static signup(payload: SignupPayload) {
    return axiosInstance.post(endpoints.registerUser, payload);
  }
  static logout() {
    return axiosInstance.delete(endpoints.session);
  }

  static getCurrentSession() {
    return axiosInstance
      .get(endpoints.session)
      .then((response) => response.data);
  }
}

export default AuthenticationService;
