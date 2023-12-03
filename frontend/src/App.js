import logo from './logo.svg';
import './App.css';
import UserProfileComponent from './components/UserProfileComponent';

function App() {
  return (
        <div className="App">
            <header className="App-header">
                <h1>Welcome to HarmonyDash</h1>
            </header>
            <main>
                <UserProfileComponent />
            </main>
        </div>
    );
}

export default App;
