import React, { useState } from "react";
import Chat from "./Chat";
import Form from "./Form";
import styles from "./styles";

function App() {
  const [editMeeting, setEditMeeting] = useState(null);
  const [refreshKey, setRefreshKey] = useState(0);

  const refresh = () => setRefreshKey(prev => prev + 1);

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🚀 AI CRM HCP Module</h1>
      <div style={styles.layout}>
        <div style={styles.leftPanel}>
          <Form
            editMeeting={editMeeting}
            clearEdit={() => setEditMeeting(null)}
            refresh={refresh}
          />
        </div>
        <div style={styles.rightPanel}>
          <Chat key={refreshKey} setEditMeeting={setEditMeeting} />
        </div>
      </div>
    </div>
  );
}

export default App;