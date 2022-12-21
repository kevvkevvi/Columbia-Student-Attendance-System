import React, { useState, useEffect } from "react";
import axios from "axios";

const Attendance = () => {
    const [attendances, setAttendances] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await axios.get("http://ec2-44-204-239-194.compute-1.amazonaws.com:5011/api/class");
                setAttendances(result.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchData();
    }, []);

    return (
        <ul>
            {Array.isArray(attendances) ? attendances.map((attendance) => (
                <li key={attendance.call_no}>
                    {attendance.call_no}: {attendance.date} - {attendance.attendance}
                </li>
            )) : <p>No attendances found</p>}

            {/* {attendances.map((attendance) => (
                <li key={attendance.call_no}>
                    {attendance.call_no}: {attendance.date} - {attendance.attendance}
                </li>
            ))} */}
        </ul>
    );
};

export default Attendance;