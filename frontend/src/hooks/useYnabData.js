// src/hooks/useYnabData.js
import { useState, useEffect } from 'react';
import { getYnabBudgets } from '../services/YnabService';

const useYnabData = () => {
    const [budgets, setBudgets] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        getYnabBudgets()
            .then(response => {
                const { data: { budgets: ynabBudgets = [] } = {} } = response.data;
                setBudgets(ynabBudgets);
                setIsLoading(false);
            })
            .catch(error => {
                console.error("Error fetching YNAB budgets:", error);
                setIsLoading(false);
            });
    }, []);

    return { budgets, isLoading };
};

export default useYnabData;
