import React, { useState, useEffect } from "react";
import axios from "axios";
import styles from "./styles";

function Chat({ setEditMeeting }) {
  const [meetings, setMeetings] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [summary, setSummary] = useState("");

  const fetchMeetings = async () => {
    const res = await axios.get("http://localhost:8000/meetings");
    setMeetings(res.data);
  };

  useEffect(() => {
    fetchMeetings();
  }, []);

  const handleEdit = (meeting) => {
    setEditMeeting(meeting);
  };

  const handleSummarize = async (id) => {
    try {
      const res = await axios.post(
        `http://localhost:8000/chat?meeting_id=${id}`
      );
      setSummary(res.data.response);
      setSelectedId(id);
    } catch (err) {
      console.error(err);
      alert("Error generating summary");
    }
  };

  return (
    <div>
      <h3 style={styles.heading}>🤖 AI Assistant</h3>
      {meetings.map((m) => (
        <div key={m.id} style={styles.card}>
          <div style={styles.cardHeader}>
            {m.doctor} | {m.date} {m.time}
          </div>
          <div>Attendees: {m.attendees}</div>
          <div>Objective: {m.objective}</div>
          <div style={styles.cardButtons}>
            <button style={styles.button} onClick={() => handleEdit(m)}>
              Edit
            </button>
            <button style={styles.button} onClick={() => handleSummarize(m.id)}>
              Summarize
            </button>
          </div>
        </div>
      ))}
      {summary && <div style={styles.summaryBox}>{summary}</div>}
    </div>
  );
}

export default Chat;