// src/components/MonthlyOverview.js
import React, { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card';

const MonthlyOverview = ({ income, expenses }) => {
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
        <Card className="text-center">
            <Card.Header as="h5">Monthly Overview</Card.Header>
            <Card.Body>
                <Card.Title>Total Income: ${income}</Card.Title>
                <Card.Title>Total Expenses: ${expenses}</Card.Title>
            </Card.Body>
        </Card>
    );
};

export default MonthlyOverview;
