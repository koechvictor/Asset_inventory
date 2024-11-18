import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom"; // Import Navigate for redirecting
import HomePage from "./pages/HomePage";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import AdminDashboard from "./pages/AdminDashboard";
import UserDashboard from "./pages/UserDashboard";
import ManagerDashboard from "./pages/ManagerDashboard";
import AboutPage from "./pages/AboutPage";
import { checkAuth } from "./services/api"; // Import checkAuth function

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Effect to check if user is authenticated
  useEffect(() => {
    const fetchUser = async () => {
      const authenticatedUser = await checkAuth(); // Call the API to check user authentication
      setUser(authenticatedUser);
      setLoading(false); // Stop loading once user state is set
    };

    fetchUser();
  }, []);

  // If still loading, show loading message
  if (loading) return <div>Loading...</div>;

  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<HomePage />} />
        <Route
          path="/signup"
          element={user ? <Navigate to="/admin-dashboard" /> : <SignUp />}
        />
        <Route
          path="/login"
          element={user ? <Navigate to="/admin-dashboard" /> : <Login />}
        />
        <Route path="/about" element={<AboutPage />} />

        {/* Private Routes (Require Authentication) */}
        <Route
          path="/admin-dashboard"
          element={user ? <AdminDashboard /> : <Navigate to="/login" />}
        />
        <Route
          path="/user-dashboard"
          element={user ? <UserDashboard /> : <Navigate to="/login" />}
        />
        <Route
          path="/manager-dashboard"
          element={user ? <ManagerDashboard /> : <Navigate to="/login" />}
        />

        {/* Catch-all Route for 404 */}
        <Route path="*" element={<div>404 Not Found</div>} />
      </Routes>
    </Router>
  );
}

export default App;
