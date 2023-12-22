// src/services/YnabService.js
import apiClient from './apiService';

export const getYnabBudgets = () => {
    return apiClient.get('api/ynab/budgets/');
};