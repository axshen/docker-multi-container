import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import OtherPage from './OtherPage';
import Fib from './Fib';

function App() {
  return (
    <Router>
      <div className="App" styles={{ backgroundImage:'https://source.unsplash.com/random' }}>
        <h2>Welcome</h2>
        <div>
          <Route exact path="/" component={Fib} />
          <Route path="/otherpage" component={OtherPage} />
        </div>
        <img src={'https://source.unsplash.com/random'} alt='random'/>
      </div>
    </Router>
  );
}

export default App;
