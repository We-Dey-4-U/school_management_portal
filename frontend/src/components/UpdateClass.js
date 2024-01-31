import React, { useState } from 'react';

const UpdateClass = ({ classInfo, onUpdateClass, onCancel }) => {
  const [updatedClass, setUpdatedClass] = useState({
    teacher_id: classInfo.teacher_id,
    subject_id: classInfo.subject_id,
    grade_level: classInfo.grade_level,
    room_number: classInfo.room_number,
    schedule_day: classInfo.schedule_day,
    class_start_time: classInfo.class_start_time,
    class_end_time: classInfo.class_end_time,
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUpdatedClass((prevClass) => ({
      ...prevClass,
      [name]: value,
    }));
  };

  const handleUpdate = async () => {
    // API call to update the class
    try {
      const response = await fetch(`http://localhost:5000/api/classes/${classInfo.class_id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedClass),
      });

      if (response.ok) {
        onUpdateClass();
      } else {
        console.error('Failed to update class:', response.statusText);
      }
    } catch (error) {
      console.error('Error updating class:', error);
    }
  };

  return (
    <div>
      <h3>Update Class</h3>
      <label>
        Grade Level:
        <input type="text" name="grade_level" value={updatedClass.grade_level} onChange={handleInputChange} />
      </label>
      <label>
        Room Number:
        <input type="text" name="room_number" value={updatedClass.room_number} onChange={handleInputChange} />
      </label>
      <label>
        Schedule Day:
        <input type="text" name="schedule_day" value={updatedClass.schedule_day} onChange={handleInputChange} />
      </label>
      <label>
        Start Time:
        <input type="text" name="class_start_time" value={updatedClass.class_start_time} onChange={handleInputChange} />
      </label>
      <label>
        End Time:
        <input type="text" name="class_end_time" value={updatedClass.class_end_time} onChange={handleInputChange} />
      </label>
      <button onClick={handleUpdate}>Update</button>
      <button onClick={onCancel}>Cancel</button>
    </div>
  );
};

export default UpdateClass;