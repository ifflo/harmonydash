// src/components/MonthlyOverview.js
import React, { useState, useEffect } from 'react';

const MonthlyOverview = () => {
    const [financialData, setFinancialData] = useState({ income: 0, expenses: 0 });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/monthly-overview/');
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();
                setFinancialData(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h2>Monthly Overview</h2>
            <p>Total Income: ${financialData.income}</p>
            <p>Total Expenses: ${financialData.expenses}</p>
        </div>
    );
};

export default MonthlyOverview;
