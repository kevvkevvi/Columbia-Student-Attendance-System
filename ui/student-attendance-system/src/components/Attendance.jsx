import { useParams } from "react-router-dom";
import React, { useState, useEffect } from "react";
import axios from "axios";
import qs from "qs";
// import date from "date-and-time";
// import { useLocation } from "react-router-dom";


const Attendance = () => {
    const { uni, call_no } = useParams();
    // console.log(uni + " " + call_no);
    const [attendance, setAttendance] = useState([]);
    const date = '2022-02-13';
    // const location = useLocation();
    // const uni = location.search.split('uni=')[1];
    // const call_no = location.search.split('call_no=')[1];

    const updateAttendance = async (call_no, date) => {
        try {
            await axios.put(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/${call_no}/class/${date}`, {
                attendance: 1  // increment attendance by 1
            });
        } catch (error) {
            console.error(error);
        }
    }



    useEffect(() => {
        const fetchAttendance = async () => {
            // Retrieve the uni and call_no query string parameters from the URL
            // const params = new URLSearchParams(window.location.search);
            // const uni = params.get("uni");
            // const call_no = params.get("call_no");

            // try {
            //     // await axios.post('http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/class', qs.stringify({
            //     //     'call_no': call_no,
            //     //     'date': date,
            //     //     'attendance': 0
            //     // }));
            //     // await axios.post('http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/students', qs.stringify({
            //     //     'call_no': call_no,
            //     //     'uni': uni,
            //     //     'date': date
            //     // }));
            //     const response = await axios.get(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/${call_no}/students/${uni}`);
            //     // console.log(response.data)
            //     setAttendance(response.data);
            // } catch (error) {
            //     console.error(error);
            // }
            try {
                const response = await axios.get(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/${call_no}/class/${date}`);
                setAttendance(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchAttendance();
    }, [uni, call_no]);

    // const currentDate = new Date();
    const currentAttendance = attendance.filter(record => record.date === date);
    console.log(attendance);
    console.log(currentAttendance);

    return (
        <div className="attendances">
            {currentAttendance.map(record => (
                <div className="attendance" key={record.date}>
                    <p>Date: {record.date}</p>
                    <p>Attendance: {record.attendance}</p>
                    <button onClick={() => updateAttendance(record.call_no, record.date)}>Check In</button>
                </div>
            ))}
        </div>
    );
};

export default Attendance;








// import React, { useState, useEffect } from 'react';

// const Attendance = ({ callNo, uni }) => {
//     const [attendances, setAttendances] = useState([]);

//     useEffect(() => {
//         const fetchAttendances = async () => {
//             const response = await fetch(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/${callNo}/class/`);
//             const data = await response.json();
//             setAttendances(data);
//         };
//         fetchAttendances();
//     }, [callNo]);

//     return (
//         <div className="attendance">
//             {attendances.map((attendance) => (
//                 <div key={attendance.date} className="attendance-record">
//                     <div>Date: {attendance.date}</div>
//                     <div>Attendance: {attendance.attendance}</div>
//                 </div>
//             ))}
//         </div>
//     );
// };

// export default Attendance;





// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import '../App.css';

// const Attendance = () => {
//     const [attendances, setAttendances] = useState([]);

//     useEffect(() => {
//         const fetchData = async () => {
//             try {
//                 const result = await axios.get("http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/class");
//                 setAttendances(result.data);
//             } catch (error) {
//                 console.error(error);
//             }
//         };
//         fetchData();
//     }, []);

//     return (
//         <ul className="attendances">
//             {Array.isArray(attendances) ? attendances.map((attendance) => (
//                 <li className="attendance" key={attendance.call_no}>
//                     {attendance.call_no}: {attendance.date} - {attendance.attendance}
//                 </li>
//             )) : <p className="student-info">No attendances found</p>}

//             {/* {attendances.map((attendance) => (
//                 <li key={attendance.call_no}>
//                     {attendance.call_no}: {attendance.date} - {attendance.attendance}
//                 </li>
//             ))} */}
//         </ul>
//     );
// };

// export default Attendance;