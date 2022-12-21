import React, { useState, useEffect } from "react";
import axios from "axios";

const baseUrl = "http://ec2-34-224-37-72.compute-1.amazonaws.com:5011";

function Course(props) {
    const { uni } = props;
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Make a request to the student microservice to get the student's name
                const studentResponse = await axios(
                    `http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/student/${uni}`
                );
                const studentName = studentResponse.data.name;

                // Use the student's name to get the courses they are taking
                const result = await axios(
                    `${baseUrl}/section/name/${studentName}`
                );
                setCourses(result.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchData();
    }, [uni]);

    if (!courses) {
        return <p>Loading courses data...</p>;
    }

    return (
        <div>
            {courses.map((course) => (
                <div key={course.call_no}>
                    <h1>{course.course_name}</h1>
                    <p>{course.enrollment_number}</p>
                    <button onClick={() => checkIn(course.call_no, course.enrollment_number)}>Check In</button>
                </div>
            ))}
        </div>
    );
}

function checkIn(callNo, enrollmentNumber) {
    axios.post(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/edit_enrollment_number`, {
        call_no: callNo,
        enrollment_number: enrollmentNumber + 1,
    });
}


export default Course;



// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const Course = () => {
//     const [sections, setSections] = useState([]);
//     const [callNo, setCallNo] = useState('');
//     const [courseName, setCourseName] = useState('');
//     const [enrollmentNumber, setEnrollmentNumber] = useState('');

//     const getSections = () => {
//         console.log('Sending GET request to /api/sections');
//         // fetch
//         return axios.get(`/api/sections`)
//             .then((response) => {
//                 console.log('Received response from /api/sections');
//                 return response.data;
//             })
//             .catch((error) => {
//                 console.error('Error getting sections:', error);
//                 throw error;
//             });
//     };

//     const addSection = (callNo, courseName, enrollmentNumber) => {
//         console.log('Sending POST request to /api/sections');
//         return axios.post(`/api/sections`, {
//             call_no: callNo,
//             course_name: courseName,
//             enrollment_number: enrollmentNumber,
//         })
//             .then((response) => {
//                 console.log('Received response from /api/sections');
//                 return response.data;
//             })
//             .catch((error) => {
//                 console.error('Error adding section:', error);
//                 throw error;
//             });
//     };


//     useEffect(() => {
//         getSections()
//             .then((data) => {
//                 setSections(data);
//             })
//             .catch((error) => {
//                 console.error(error);
//             });
//     }, []);

//     const handleSubmit = async (event) => {
//         event.preventDefault();
//         try {
//             const data = await addSection(callNo, courseName, enrollmentNumber);
//             console.log(data);
//             setCallNo('');
//             setCourseName('');
//             setEnrollmentNumber('');
//         } catch (error) {
//             console.error(error);
//         }
//     };

//     return (
//         <div>
//             <h2>Course List</h2>
//             <ul>
//                 {sections.map((section) => (
//                     <li key={section.call_no}>
//                         {section.course_name} ({section.call_no})
//                     </li>
//                 ))}
//             </ul>
//             <form onSubmit={handleSubmit}>
//                 <label htmlFor="callNo">
//                     Call No:
//                     <input
//                         type="text"
//                         value={callNo}
//                         onChange={(event) => setCallNo(event.target.value)}
//                     />
//                 </label>
//                 <br />
//                 <label htmlFor="courseName">
//                     Course Name:
//                     <input
//                         type="text"
//                         value={courseName}
//                         onChange={(event) => setCourseName(event.target.value)}
//                     />
//                 </label>
//                 <br />
//                 <label htmlFor="enrollmentNumber">
//                     Enrollment Number:
//                     <input
//                         type="number"
//                         value={enrollmentNumber}
//                         onChange={(event) => setEnrollmentNumber(event.target.value)}
//                     />
//                 </label>
//                 <br />
//                 <button type="submit">Add Section</button>
//             </form>
//         </div>
//     );
// };

// export default Course;

