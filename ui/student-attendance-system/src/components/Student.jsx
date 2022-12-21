import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import { Link, Router } from 'react-router-dom';

const Student = ({ uni }) => {
    const [student, setStudent] = useState(null);

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

    if (!student) {
        return <p>Loading student data...</p>;
    }

    return (
        // <Router>
        <div>
            <h2>Student Information</h2>
            <p>UNI: {student.UNI}</p>
            <p>First Name: {student.first_name}</p>
            <p>Last Name: {student.last_name}</p>
            <p>Email: {student.email}</p>
            {/* <Link to="/">Back to Home</Link> */}
        </div>
        // </Router>
    );
};

export default Student;