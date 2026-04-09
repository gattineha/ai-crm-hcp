# main.py
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ----------------------------
# DATABASE CONFIG (SQLite)
# ----------------------------
DB_FILE = "crm_db.db"

def get_db():
    return sqlite3.connect(DB_FILE)

# Create table automatically
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor TEXT,
            date TEXT,
            time TEXT,
            attendees TEXT,
            objective TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------------------------
# FASTAPI SETUP
# ----------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# MODEL
# ----------------------------
class Meeting(BaseModel):
    doctor: str
    date: str
    time: str
    attendees: str
    objective: str

# ----------------------------
# ROUTES
# ----------------------------

@app.get("/")
def home():
    return {"message": "Server is running"}

# ✅ ADD MEETING
@app.post("/meetings")
def add_meeting(meeting: Meeting):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interactions (doctor, date, time, attendees, objective)
        VALUES (?, ?, ?, ?, ?)
    """, (
        meeting.doctor,
        meeting.date,
        meeting.time,
        meeting.attendees,
        meeting.objective
    ))

    conn.commit()
    conn.close()

    return {"message": "Meeting stored successfully"}

# ✅ GET MEETINGS
@app.get("/meetings")
def get_meetings():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interactions ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": r[0],
            "doctor": r[1],
            "date": r[2],
            "time": r[3],
            "attendees": r[4],
            "objective": r[5]
        }
        for r in rows
    ]

# ✅ UPDATE MEETING
@app.put("/meetings/{meeting_id}")
def update_meeting(meeting_id: int, meeting: Meeting):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE interactions
        SET doctor=?, date=?, time=?, attendees=?, objective=?
        WHERE id=?
    """, (
        meeting.doctor,
        meeting.date,
        meeting.time,
        meeting.attendees,
        meeting.objective,
        meeting_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Meeting updated successfully"}

# ✅ AI SUMMARY
@app.post("/chat")
def chat(meeting_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT doctor, objective FROM interactions WHERE id=?", (meeting_id,))
    row = cursor.fetchone()

    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Meeting not found")

    doctor, objective = row

    return {
        "response": f"""
AI Response:
1. Meeting conducted with {doctor}
2. Objective: {objective}
3. Key discussion points covered
4. Action items assigned
5. Follow-up meeting planned
"""
    }