import axios from "axios";

// Base URL for your backend API
const API_URL = "http://localhost:5000"; // Change this if your backend is hosted elsewhere

// Create an Axios instance with the base URL and default headers
export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json", // JSON content type
  },
  withCredentials: true, // Send cookies with requests (important for session-based authentication)
});

// Generic function to handle API requests
const handleApiCall = async (method, url, data = null) => {
  try {
    const response = await api[method](url, data); // Perform the API request (GET, POST, etc.)
    return response.data; // Return the response data
  } catch (error) {
    console.error("API error:", error);

    return error.response
      ? error.response.data // Return the error response if available
      : { message: "An error occurred. Please try again later." }; // Generic error message
  }
};

// API calls to interact with the backend

// Register a new user
export const registerUser = (userData) =>
  handleApiCall("post", "/register", userData);

// Login a user
export const loginUser = (credentials) =>
  handleApiCall("post", "/login", credentials);

// Logout the user
export const logoutUser = () => handleApiCall("get", "/logout");

// Check authentication status (returns user data if authenticated)
export const checkAuth = async () => {
  try {
    const response = await api.get("/my_profile");
    return response.data.user; // Return user data if authenticated
  } catch (error) {
    console.error("Authentication error:", error);
    return null; // Return null if not authenticated
  }
};

// Fetch assets (protected route, requires authentication)
export const fetchAssets = () => handleApiCall("get", "/assets");

// Fetch departments (protected route, requires authentication)
export const fetchDepartments = () => handleApiCall("get", "/departments");

// Fetch categories (protected route, requires authentication)
export const fetchCategories = () => handleApiCall("get", "/categories");

export default api;
