import React from 'react';
import axios from 'axios';

const Student = ({ student }) => {
    const getStudentByKey = (uni) => {
        return axios.get(`/student/${uni}`)
            .then(response => response.data)
            .catch(error => {
                throw error;
            });
    };

    // Use the getStudentByKey function to make the API request and handle the response
    getStudentByKey('12345')
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });

    const addStudent = (uni, firstName, lastName, email) => {
        return axios.post('/api/student', {
            UNI: uni,
            first_name: firstName,
            last_name: lastName,
            email: email,
        })
            .then(response => response.data)
            .catch(error => {
                throw error;
            });
    };

    // Use the addStudent function to make the API request and handle the response
    addStudent('12345', 'John', 'Doe', 'john.doe@example.com')
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });

    return (
        <div className="student-card">
            <h2>{student.first_name} {student.last_name}</h2>
            <p>UNI: {student.UNI}</p>
            <p>Email: {student.email}</p>
        </div>
    );
};

export default Student;




