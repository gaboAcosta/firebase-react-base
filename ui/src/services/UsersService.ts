import { axiosInstance } from "../utils/axiosHelper.ts";

export type User = {
  id: string;
  email: string;
};

export const getUsers = async (): Promise<User[]> => {
  const response = await axiosInstance.get("/v1/users/");
  return response.data;
};
