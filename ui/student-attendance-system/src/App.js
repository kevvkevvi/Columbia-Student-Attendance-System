import { BrowserRouter, Routes, Route, Switch } from "react-router-dom";
import React, { useState, useEffect } from "react";
import './App.css';
import Home from "./pages/home/Home";

function App() {
  return (
    <div className="App">
      <h1>Student Management System</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
