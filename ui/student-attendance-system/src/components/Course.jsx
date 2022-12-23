import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
// import { useHistory } from 'react-router-dom';

const Course = ({ uni }) => {
    const [courses, setCourses] = useState(null);

    // const history = useHistory();

    // const handleClick = (course) => {
    //     history.push(`/attendance/${uni}/${course.call_no}`);
    //     // history.push(`/attendance?uni=${uni}&call_no=${course.call_no}`);
    // };

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

    if (!courses) {
        return <div className="courses">Loading courses...</div>;
    }

    console.log(courses);

    return (
        <div>
            <h2 className="courses">Courses</h2>
            {courses.map((course) => (
                // <div className="courses" key={course.call_no} onClick={() => {
                //     // Navigate to the Attendance component and pass along the necessary parameters as query string parameters in the URL
                //     window.location.assign(`/attendance?uni=${uni}&call_no=${course.call_no}`);
                // }}>
                //     <p className="course">{course.call_no}</p>
                // </div>
                <div className="courses" key={course.call_no}>
                    {/* <Link onClick={() => handleClick(course)}>{course.call_no}</Link> */}
                    <Link to={`/attendance/${uni}/${course.call_no}`}>{course.call_no}</Link>
                </div>
            ))}
        </div>
    );
};

export default Course;




// import React, { useEffect, useState } from "react";
// import axios from "axios";

// const Course = ({ uni, call_no }) => {
//     return (
//         <div>
//             <h1>Course Name</h1>
//             <p>Course Description</p>
//             <button onClick={() => checkIn(uni, call_no)}>Check In</button>
//         </div>
//     );
// }

// const checkIn = (uni, call_no) => {
//     // Make POST request to /api/attendance endpoint
//     fetch('http://ec2-34-224-37-72.compute-1.amazonaws.com:5011/api/enrollments', {
//         method: 'POST',
//         body: JSON.stringify({ call_no, uni }),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//         .then(res => res.json())
//         .then(data => {
//             console.log(data);
//             // Handle success or failure of request
//         })
//         .catch(error => {
//             console.error(error);
//         });
// }

// const Courses = ({ uni }) => {
//     const [courses, setCourses] = useState([]);
//     // console.log("we're here")
//     useEffect(() => {
//         const fetchCourses = async () => {
//             try {
//                 const response = await axios.get(`http://ec2-34-224-37-72.compute-1.amazonaws.com:5011/enrollments/uni/${uni}`);
//                 setCourses(response.data);
//             } catch (error) {
//                 console.error(error);
//             }
//         };
//         fetchCourses();
//     }, [uni]);

//     return (
//         // console.log(courses);
//         <div className="courses">
//             {courses.map((course) => (
//                 <Course key={course.call_no} uni={course.uni} courseNumber={course.course_number} />
//             ))}
//         </div>
//     );
// };

// export default Courses;
