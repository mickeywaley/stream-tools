import React, { Component } from 'react';
import TasksPage from './components/TasksPage';
import logo from "./logo.svg";
import "./App.css";


// import { createStore } from "redux";
// function counterReducer(state = 0, action) {
//   if (action.type === "INCREMENT") {
//     return state + 1;
//   }
//   return state;
// }
// const store = createStore(counterReducer);
// console.log(store.getState());
// store.subscribe(() => {
//   console.log("current state: ", store.getState());
// });
// store.dispatch({ type: "INCREMENT" });


class App extends Component {
  render() {
    return (
      <div className="main-content">
        {" "}
        <TasksPage tasks={mockTasks} />{" "}
      </div>
    );
  }
}
export default App;


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header" >
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//
// export default App;
