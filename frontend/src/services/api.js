// src/services/api.js

const apiUrl = 'http://localhost:5000'; // Replace with your actual Flask API URL

const api = {
  getClassList: async () => {
    const response = await fetch(`${apiUrl}/api/classes`);
    const data = await response.json();
    return data;
  },

  getSubjectList: async () => {
    const response = await fetch(`${apiUrl}/api/subjects`);
    const data = await response.json();
    return data;
  },

  getTeacherList: async () => {
    const response = await fetch(`${apiUrl}/api/teachers`);
    const data = await response.json();
    return data;
  },

  // Add more functions for other API calls
};

export default api;