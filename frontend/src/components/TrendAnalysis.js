import React, { useState, useEffect } from 'react';

const TrendAnalysis = () => {
    const [trends, setTrends] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/trend-analysis/');
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();
                setTrends(data);
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
            <h2>Trend Analysis</h2>
            {trends.map((trend, index) => (
                <p key={index}>{trend.month}: ${trend.amount}</p>
            ))}
        </div>
    );
};

export default TrendAnalysis;
