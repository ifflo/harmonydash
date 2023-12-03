// src/apiService.js
import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/';

export const getUserProfiles = () => {
    return axios.get(`${BASE_URL}userprofiles/`);
};

// Add more functions for different API endpoints
