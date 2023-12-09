// src/components/MonthlyOverview.js
import React, { useState, useEffect } from 'react';

const MonthlyOverview = () => {
    const [financialData, setFinancialData] = useState({ income: 0, expenses: 0 });

    useEffect(() => {
        // Fetch financial data from your API
        const fetchData = async () => {
            // Update with the correct API endpoint
            const response = await fetch('http://localhost:8000/api/financial-summary/');
            const data = await response.json();
            setFinancialData(data);
        };

        fetchData();
    }, []);

    return (
        <div>
            <h2>Monthly Overview</h2>
            <p>Total Income: ${financialData.income}</p>
            <p>Total Expenses: ${financialData.expenses}</p>
        </div>
    );
};

export default MonthlyOverview;