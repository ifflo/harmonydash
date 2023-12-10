import logo from './logo.svg';
import './App.css';
import UserProfileComponent from './components/UserProfileComponent';
import MonthlyOverview from './components/MonthlyOverview';
import SpendingByCategory from './components/SpendingByCategory';
import TrendAnalysis from './components/TrendAnalysis';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


function App() {
  return (
    <Container>
            <Row>
                <Col><MonthlyOverview income={1000} expenses={500} /></Col>
            </Row>
            <Row>
                <Col><SpendingByCategory categories={[/* categories data */]} /></Col>
            </Row>
            <Row>
                <Col><TrendAnalysis trends={[/* trends data */]} /></Col>
            </Row>
        </Container>
  );
}

export default App;
