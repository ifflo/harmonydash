// src/components/YnabBudgetComponent.js
import React from 'react';
import useYnabData from '../hooks/useYnabData';
import { ListGroup } from 'react-bootstrap';


const YnabBudgetComponent = () => {
    const { budgets, isLoading } = useYnabData();

    if (isLoading) {
        return <p>Loading budgets...</p>;
    }

    return (
        <ListGroup>
            {budgets.map(budget => (
                <ListGroup.Item key={budget.id}>{budget.name}</ListGroup.Item>
            ))}
        </ListGroup>
    );
};

export default YnabBudgetComponent;
