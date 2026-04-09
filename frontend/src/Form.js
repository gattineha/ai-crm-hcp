import React, { useState, useEffect } from "react";
import axios from "axios";
import styles from "./styles";

function Form({ editMeeting, clearEdit, refresh }) {
  const [doctor, setDoctor] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [attendees, setAttendees] = useState("");
  const [objective, setObjective] = useState("");

  useEffect(() => {
    if (editMeeting) {
      setDoctor(editMeeting.doctor);
      setDate(editMeeting.date);
      setTime(editMeeting.time);
      setAttendees(editMeeting.attendees);
      setObjective(editMeeting.objective);
    }
  }, [editMeeting]);

  const handleSubmit = async () => {
  const payload = { doctor, date, time, attendees, objective };

  try {
    if (editMeeting) {
      await axios.put(
        `http://localhost:8000/meetings/${editMeeting.id}`,
        payload
      );
      alert("Meeting updated successfully!");
      clearEdit();
    } else {
      await axios.post("http://localhost:8000/meetings", payload);
      alert("Meeting added successfully!");
    }

    setDoctor(""); setDate(""); setTime(""); setAttendees(""); setObjective("");
    refresh();

  } catch (err) {
    alert("Error saving meeting!");
    console.error(err);
  }
};

  return (
    <div>
      <h3 style={styles.heading}>{editMeeting ? "Edit Meeting" : "Add Meeting"}</h3>
      <input
        style={styles.input}
        placeholder="Doctor"
        value={doctor}
        onChange={(e) => setDoctor(e.target.value)}
      />
      <input
        style={styles.input}
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <input
        style={styles.input}
        type="time"
        value={time}
        onChange={(e) => setTime(e.target.value)}
      />
      <input
        style={styles.input}
        placeholder="Attendees"
        value={attendees}
        onChange={(e) => setAttendees(e.target.value)}
      />
      <textarea
        style={styles.textarea}
        placeholder="Objective"
        value={objective}
        onChange={(e) => setObjective(e.target.value)}
      />
      <button style={styles.button} onClick={handleSubmit}>
        {editMeeting ? "Update Meeting" : "Add Meeting"}
      </button>
    </div>
  );
}

export default Form;