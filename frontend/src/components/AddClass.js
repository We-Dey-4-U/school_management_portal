import React, { useState } from 'react';

const AddClass = ({ onAddClass }) => {
  const [teacherId, setTeacherId] = useState('');
  const [subjectId, setSubjectId] = useState('');
  const [gradeLevel, setGradeLevel] = useState('');
  const [roomNumber, setRoomNumber] = useState('');
  const [scheduleDay, setScheduleDay] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');

  const handleAddClass = () => {
    // Validation and API call to add a new class
    const newClass = {
      teacher_id: parseInt(teacherId),
      subject_id: parseInt(subjectId),
      grade_level: parseInt(gradeLevel),
      room_number: roomNumber,
      schedule_day: scheduleDay,
      class_start_time: startTime,
      class_end_time: endTime,
    };

    // Assuming you have a function to add a class in your Flask API
    onAddClass(newClass);

    // Reset form fields after adding a new class
    setTeacherId('');
    setSubjectId('');
    setGradeLevel('');
    setRoomNumber('');
    setScheduleDay('');
    setStartTime('');
    setEndTime('');
  };

  return (
    <div>
      <h2>Add New Class</h2>
      {/* Form for adding a new class */}
      <label>
        Teacher ID:
        <input type="text" value={teacherId} onChange={(e) => setTeacherId(e.target.value)} />
      </label>
      <br />
      <label>
        Subject ID:
        <input type="text" value={subjectId} onChange={(e) => setSubjectId(e.target.value)} />
      </label>
      <br />
      <label>
        Grade Level:
        <input type="text" value={gradeLevel} onChange={(e) => setGradeLevel(e.target.value)} />
      </label>
      <br />
      <label>
        Room Number:
        <input type="text" value={roomNumber} onChange={(e) => setRoomNumber(e.target.value)} />
      </label>
      <br />
      <label>
        Schedule Day:
        <input type="text" value={scheduleDay} onChange={(e) => setScheduleDay(e.target.value)} />
      </label>
      <br />
      <label>
        Class Start Time:
        <input type="text" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
      </label>
      <br />
      <label>
        Class End Time:
        <input type="text" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
      </label>
      <br />
      <button onClick={handleAddClass}>Add Class</button>
    </div>
  );
};

export default AddClass;