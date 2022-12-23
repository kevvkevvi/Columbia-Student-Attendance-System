import React from "react";
// import { Routes, Route, Router } from 'react-router-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
// import { createBrowserHistory } from 'history';
// import Student from "./components/Student"
// import Course from "./components/Course";
import Home from "./components/Home";
import Attendance from "./components/Attendance";
import './App.css';


// const history = createBrowserHistory();

const App = () => {
  return (
    <div>
      <BrowserRouter basename="/">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/attendance/:uni/:call_no" component={Attendance} />
        </Switch>
      </BrowserRouter>
      {/* <Route path="/attendance/:uni/:call_no" element={<Attendance />} /> */}
    </div>
  );
};

export default App;