import React, { useState, useEffect } from "react";
import axios from "axios";

const Student = ({ uni }) => {
    const [student, setStudent] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const [formValues, setFormValues] = useState({
        UNI: "",
        first_name: "",
        last_name: "",
        email: "",
    });

    useEffect(() => {
        const fetchStudent = async () => {
            try {
                const response = await axios.get(`http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/student/${uni}`);
                setStudent(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchStudent();
    }, [uni]);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(`http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/api/student`, formValues);
            setStudent(response.data);
            setShowForm(false);
        } catch (error) {
            console.error(error);
        }
    };

    if (!student) {
        return (
            <div className="student-info">
                {!showForm ? (
                    <button onClick={() => setShowForm(true)}>Add Student</button>
                ) : (
                    <form onSubmit={handleSubmit}>
                        <label htmlFor="UNI">UNI:</label>
                        <input type="text" id="UNI" name="UNI" value={formValues.UNI} onChange={handleChange} />
                        <br />
                        <label htmlFor="first_name">First Name:</label>
                        <input type="text" id="first_name" name="first_name" value={formValues.first_name} onChange={handleChange} />
                        <br />
                        <label htmlFor="last_name">Last Name:</label>
                        <input type="text" id="last_name" name="last_name" value={formValues.last_name} onChange={handleChange} />
                        <br />
                        <label htmlFor="email">Email:</label>
                        <input type="text" id="email" name="email" value={formValues.email} onChange={handleChange} />
                        <br />
                        <button type="submit">Submit</button>
                    </form>
                )}
            </div>
        );
    }

    return (
        <div>
            <h2 className="student-info">Student Information</h2>
            <p className="student-info p">UNI: {student.UNI}</p>
            <p className="student-info p">First Name: {student.first_name}</p>
            <p className="student-info p">Last Name: {student.last_name}</p>
            <p className="student-info p">Email: {student.email}</p>
        </div>
    );

};

export default Student;











// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import '../App.css';
// // import { Link, Router } from 'react-router-dom';

// const Student = ({ uni }) => {
//     const [student, setStudent] = useState(null);

//     useEffect(() => {
//         const fetchStudent = async () => {
//             try {
//                 const response = await axios.get(`http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/student/${uni}`);
//                 setStudent(response.data);
//             } catch (error) {
//                 console.error(error);
//             }
//         };

//         fetchStudent();
//     }, [uni]);

//     if (!student) {
//         return <p>Loading student data...</p>;
//     }

//     return (
//         // <Router>
//         <div className='body'>
//             <h2 className='student-info'>Student Information</h2>
//             <p className='student-info'>UNI: {student.UNI}</p>
//             <p className='student-info'>First Name: {student.first_name}</p>
//             <p className='student-info'>Last Name: {student.last_name}</p>
//             <p className='student-info'>Email: {student.email}</p>
//             {/* <Link to="/">Back to Home</Link> */}
//         </div>
//         // </Router>
//     );
// };

// export default Student;