// App.js
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar, Row, Col } from 'react-bootstrap';
import YNABDataFetcher from './components/YNABDataFetcher';

function App() {
    return (
        <div className="App">
            <Navbar bg="dark" variant="dark">
                <Container>
                    <Navbar.Brand href="#home">Harmony Dashboard</Navbar.Brand>
                </Container>
            </Navbar>
            <Container>
                <Row className="justify-content-md-center">
                    <Col md="auto">
                        <YNABDataFetcher />
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default App;
