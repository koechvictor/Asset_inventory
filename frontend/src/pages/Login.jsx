import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../services/api";
import styles from "./Login.module.css";
import { Link } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate(); // Use react-router's navigate hook

  const handleSubmit = async (e) => {
    e.preventDefault();
    const credentials = { email, password };
    const data = await loginUser(credentials);

    if (data.message) {
      setMessage(data.message);
    } else {
      setMessage("Login successful!");
      onLogin(data.user_id);

      // Redirect to the user dashboard
      navigate("/user-dashboard");
    }
  };

  return (
    <div className={styles["login-container"]}>
      <div className={styles.wrapper}>
        <div className={`${styles["form-wrapper"]} ${styles["sign-in"]}`}>
          <form onSubmit={handleSubmit}>
            <h1 className={styles["main-title"]}>Asset Maze</h1>
            <h2>Login</h2>
            <div className={styles["input-group"]}>
              <input
                type="text"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <label>Email</label>
            </div>
            <div className={styles["input-group"]}>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <label>Password</label>
            </div>
            <div className={styles.rememder}>
              <label>
                <input type="checkbox" /> Remember me
              </label>
            </div>
            <button type="submit" className={styles["login-button"]}>
              Login
            </button>
            {message && <div>{message}</div>}
            <div className={styles["signup-link"]}>
              <p>
                Don't have an account?{" "}
                <Link to="/signup" className={styles["signupbtn-link"]}>
                  Sign up
                </Link>
              </p>
            </div>
            <Link to="/" className={styles["home-button"]}>
              Back to Home
            </Link>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
