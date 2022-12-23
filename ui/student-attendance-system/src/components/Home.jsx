// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import { Link } from "react-router-dom";
// import { useHistory } from "react-router-dom";
import Student from "./Student"
import Course from "./Course";

const Home = () => {
    console.log("Home");
    // const [student, setStudent] = useState(null);
    // const [showForm, setShowForm] = useState(false);
    // const [formValues, setFormValues] = useState({
    //     UNI: "",
    //     first_name: "",
    //     last_name: "",
    //     email: "",
    // });
    // const history = useHistory();

    // // useEffect(() => {
    // //     if (student) {
    // //         setFormValues({
    // //             UNI: student.UNI,
    // //             first_name: student.first_name,
    // //             last_name: student.last_name,
    // //             email: student.email,
    // //         });
    // //     }
    // // }, [student]);

    // const handleChange = (event) => {
    //     const { name, value } = event.target;
    //     setFormValues({ ...formValues, [name]: value });
    // };

    // const handleSubmit = async (event) => {
    //     event.preventDefault();
    //     try {
    //         setFormValues({
    //             UNI: event.target.UNI.value,
    //             first_name: event.target.first_name.value,
    //             last_name: event.target.last_name.value,
    //             email: event.target.email.value,
    //         });
    //         const response = await axios.post(`http://6156projstudentmicroservice-env.eba-ds6ar3x2.us-east-2.elasticbeanstalk.com/api/student`, formValues);
    //         // update student with the response data from the server
    //         setStudent(response.data);
    //         history.push(`/student/${response.data.UNI}`);
    //         // set showForm to false to hide the form
    //         setShowForm(false);
    //     } catch (error) {
    //         console.error(error);
    //     }
    // };

    // if (!student) {
    return (
        <div>
            <Student uni="hw2910" />
            <Course uni="hw2910" />
            {/* play around with the uni value to see the different results*/}
            {/* <Student uni="kjl2185" />
                <Course uni="kjl2185" /> */}
            {/* <Attendance /> */}
            {/* </Router> */}
        </div>
    );
    // };
};

export default Home;