import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';

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
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Month</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {trends.map((trend, index) => (
                        <tr key={index}>
                            <td>{trend.month}</td>
                            <td>${trend.amount}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    );
};

export default TrendAnalysis;
