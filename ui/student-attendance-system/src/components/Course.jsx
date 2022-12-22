import React, { useEffect, useState } from "react";
import axios from "axios";

const Course = ({ uni, call_no }) => {
    return (
        <div>
            <h1>Course Name</h1>
            <p>Course Description</p>
            <button onClick={() => checkIn(uni, call_no)}>Check In</button>
        </div>
    );
}

const checkIn = (uni, call_no) => {
    // Make POST request to /api/attendance endpoint
    fetch('http://ec2-34-224-37-72.compute-1.amazonaws.com:5011/api/enrollments', {
        method: 'POST',
        body: JSON.stringify({ call_no, uni }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            // Handle success or failure of request
        })
        .catch(error => {
            console.error(error);
        });
}

const Courses = ({ uni }) => {
    const [courses, setCourses] = useState([]);
    // console.log("we're here")
    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.get(`http://ec2-34-224-37-72.compute-1.amazonaws.com:5011/enrollments/uni/${uni}`);
                setCourses(response.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchCourses();
    }, [uni]);

    return (
        // console.log(courses);
        <div className="courses">
            {courses.map((course) => (
                <Course key={course.course_number} courseName={course.course_name} courseNumber={course.course_number} />
            ))}
        </div>
    );
};

export default Courses;














// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import '../App.css';

// const baseUrl = "http://ec2-34-224-37-72.compute-1.amazonaws.com:5011";

// function Course(props) {
//     const { uni } = props;
//     const [courses, setCourses] = useState([]);

//     useEffect(() => {
//         const fetchData = async () => {
//             try {
//                 // Make a request to the student microservice to get the student's name
//                 const studentResponse = await axios(
//                     `http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/student/${uni}`
//                 );
//                 const studentName = studentResponse.data.name;

//                 // Use the student's name to get the courses they are taking
//                 const result = await axios(
//                     `${baseUrl}/section/name/${studentName}`
//                 );
//                 setCourses(result.data);
//             } catch (error) {
//                 console.error(error);
//             }
//         };
//         fetchData();
//     }, [uni]);

//     if (!courses) {
//         return <p>Loading courses data...</p>;
//     }

//     return (
//         <div className="courses">
//             {courses.map((course) => (
//                 <div className="course" key={course.call_no}>
//                     <h1 className="course h1">{course.course_name}</h1>
//                     <p className="course p">{course.enrollment_number}</p>
//                     <button className="course button" onClick={() => checkIn(course.call_no, course.enrollment_number)}>Check In</button>
//                 </div>
//             ))}
//         </div>
//     );
// }

// function checkIn(callNo, enrollmentNumber) {
//     axios.post(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/edit_enrollment_number`, {
//         call_no: callNo,
//         enrollment_number: enrollmentNumber + 1,
//     });
// }


// export default Course;
