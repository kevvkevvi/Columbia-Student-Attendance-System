import React from "react";
import Student from "./Student"
import Course from "./Course";

const Home = () => {
    console.log("Home");
    return (
        <div>
            <h1>Student Attendance System</h1>
            <Student uni="hw2910" />
            <Course uni="hw2910" />
            {/* play around with the uni value to see the different results*/}
            {/* <Student uni="kjl2185" />
        <Course uni="kjl2185" /> */}
            {/* <Attendance /> */}
            {/* </Router> */}
        </div>
    );
};

export default Home;