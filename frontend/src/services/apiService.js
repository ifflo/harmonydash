// src/services/apiService.js
import axios from 'axios';

const BASE_URL = 'http://localhost:8000/';

const apiClient = axios.create({
    baseURL: BASE_URL,
    // Additional default settings can go here
});

export default apiClient;
