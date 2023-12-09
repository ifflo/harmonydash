import React, { useState, useEffect } from 'react';

const SpendingByCategory = () => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/spending-by-category/');
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();
                setCategories(data);
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
            <h2>Spending by Category</h2>
            <ul>
                {categories.map(category => (
                    <li key={category.name}>{category.name}: ${category.amount}</li>
                ))}
            </ul>
        </div>
    );
};

export default SpendingByCategory;
