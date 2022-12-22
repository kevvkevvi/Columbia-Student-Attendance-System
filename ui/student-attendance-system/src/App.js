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
      {/* <Router> */}
      {/* <Routes> */}
      <BrowserRouter>
        <Switch>
          <Route exact path="/" element={<Home />} />
          <Route path="/attendance" element={<Attendance />} />
        </Switch>
      </BrowserRouter>
      {/* <Route path="/attendance/:uni/:call_no" element={<Attendance />} /> */}
      {/* </Routes> */}
      {/* </Router> */}

      {/* <h1>Student Attendance System</h1>
      <Student uni="hw2910" />
      <Course uni="hw2910" /> */}
      {/* play around with the uni value to see the different results*/}
      {/* <Student uni="kjl2185" />
      <Course uni="kjl2185" /> */}
      {/* <Attendance /> */}
      {/* </Router> */}
    </div>
  );
};

export default App;