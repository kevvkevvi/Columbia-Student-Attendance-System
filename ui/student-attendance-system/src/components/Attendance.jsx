import React, { useState, useEffect } from 'react';

const Attendance = ({ callNo, uni }) => {
    const [attendances, setAttendances] = useState([]);

    useEffect(() => {
        const fetchAttendances = async () => {
            const response = await fetch(`http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/sections/${callNo}/class/`);
            const data = await response.json();
            setAttendances(data);
        };
        fetchAttendances();
    }, [callNo]);

    return (
        <div className="attendance">
            {attendances.map((attendance) => (
                <div key={attendance.date} className="attendance-record">
                    <div>Date: {attendance.date}</div>
                    <div>Attendance: {attendance.attendance}</div>
                </div>
            ))}
        </div>
    );
};

export default Attendance;





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