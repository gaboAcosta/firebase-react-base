// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, User } from "firebase/auth";
import { signInWithEmailAndPassword } from "firebase/auth";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCH5MU4I5zImohm2PuIzwjDOZJ5KKN0cLg",
  authDomain: "fir-intro-b775d.firebaseapp.com",
  projectId: "fir-intro-b775d",
  storageBucket: "fir-intro-b775d.appspot.com",
  messagingSenderId: "563843062375",
  appId: "1:563843062375:web:8033fdd54f46e44c1812c2",
  measurementId: "G-KY89T6HP4H",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default app;

export const auth = getAuth(app);
export const login = async (email: string, password: string) => {
  await signInWithEmailAndPassword(auth, email, password);
  return auth.currentUser;
};

export const getUser = async (): Promise<User | null> => {
  const user = getAuth(app);
  return user.currentUser;
};
