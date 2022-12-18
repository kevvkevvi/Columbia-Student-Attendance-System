import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Course = () => {
    const [sections, setSections] = useState([]);
    const [callNo, setCallNo] = useState('');
    const [courseName, setCourseName] = useState('');
    const [enrollmentNumber, setEnrollmentNumber] = useState('');

    const getSections = () => {
        return axios.get('/api/sections')
            .then((response) => response.data)
            .catch((error) => {
                throw error;
            });
    };

    const addSection = (callNo, courseName, enrollmentNumber) => {
        return axios.post('/api/sections', {
            call_no: callNo,
            course_name: courseName,
            enrollment_number: enrollmentNumber,
        })
            .then((response) => response.data)
            .catch((error) => {
                throw error;
            });
    };

    useEffect(() => {
        getSections()
            .then((data) => {
                setSections(data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const data = await addSection(callNo, courseName, enrollmentNumber);
            console.log(data);
            setCallNo('');
            setCourseName('');
            setEnrollmentNumber('');
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h2>Course List</h2>
            <ul>
                {sections.map((section) => (
                    <li key={section.call_no}>
                        {section.course_name} ({section.call_no})
                    </li>
                ))}
            </ul>
            <form onSubmit={handleSubmit}>
                <label htmlFor="callNo">
                    Call No:
                    <input
                        type="text"
                        value={callNo}
                        onChange={(event) => setCallNo(event.target.value)}
                    />
                </label>
                <br />
                <label htmlFor="courseName">
                    Course Name:
                    <input
                        type="text"
                        value={courseName}
                        onChange={(event) => setCourseName(event.target.value)}
                    />
                </label>
                <br />
                <label htmlFor="enrollmentNumber">
                    Enrollment Number:
                    <input
                        type="number"
                        value={enrollmentNumber}
                        onChange={(event) => setEnrollmentNumber(event.target.value)}
                    />
                </label>
                <br />
                <button type="submit">Add Section</button>
            </form>
        </div>
    );
};

export default Course;

