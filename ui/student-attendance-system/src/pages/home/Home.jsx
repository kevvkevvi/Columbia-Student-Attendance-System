import React from 'react'
// import axios from 'axios'
import Student from '../../components/Student'
import Course from '../../components/Course'

const Home = () => {
    const student = { UNI: '12345', first_name: 'John', last_name: 'Doe', email: 'john.doe@example.com' };
    return (
        <div>
            <Student student={student} />
            <Course />
        </div>
    );
}

export default Home