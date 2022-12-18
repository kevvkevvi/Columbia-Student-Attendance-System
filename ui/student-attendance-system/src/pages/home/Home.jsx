import React from 'react'
import axios from 'axios'
import Student from '../../components/student/Student'

const Home = () => {
    const student = { UNI: '12345', first_name: 'John', last_name: 'Doe', email: 'john.doe@example.com' };
    return (
        <div>
            <Student student={student} />
        </div>
    );
}

export default Home