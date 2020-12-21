import React, { Component } from 'react'
import axios from 'axios';

const baseUrl = process.env.REACT_APP_API_URL;
console.log(baseUrl)

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      argument: null,
      value: null,
      duration: null,
      cache: {},
    };
  }

  componentDidMount() {
    this.getRequest('api/cache');
  }

  updateArgument = (event) => {
    this.setState({
      argument: event.target.value
    });
  }

  getRequest(endpoint) {
    var url = baseUrl + endpoint;
    axios.get(url)
    .then(res => {
      this.setState({
        cache: res.data
      });
    })
  }

  postRequest(endpoint) {
    var url = baseUrl + endpoint;
    axios.post(url, {
      'input': this.state.argument
    })
    .then(res => {
      this.setState({
        value: res.data.value,
        duration: res.data.duration
      });
      this.getRequest('api/cache');
    })
    .catch(err => {
      console.log(err);
    })
  }

  onSubmitHandler = (event, endpoint) => {
    event.preventDefault();
    this.postRequest(endpoint);
  }

  render() {
    let cache = this.state.cache;
    return (
      <>
        <div className='App'>
          <h1>Fibonacci</h1>
          <p>Enter the index you find: </p>
          <form method='post'>
            <input type='text' onChange={this.updateArgument} required></input>
            <button onClick={(event) => this.onSubmitHandler(event, "api/fib")}>Calculate</button>
            <button onClick={(event) => this.onSubmitHandler(event, "api/cached_fib")}>Calculate with cache</button>
          </form>

          <div>
            {(this.state.value !== null) && (this.state.duration !== null) &&
              <p>The fibonacci sequence value is {this.state.value} computed in {this.state.duration} ms</p>              
            }
          </div>
          <h1>Cache</h1>
          <p>We store some of the values you have previously calculated in cache. Let's see how much it speeds things up!</p>
          <p>Content (index | value):</p>
          <ul>
            {Object.keys(cache).map((key, index) => (
              <li key={index}>| {key} | {cache[key]} |</li>
            ))}
          </ul>
        </div>
      </>
    );
  }
}

export default App;
