import React, { useState, useEffect } from 'react';
import AddClass from './AddClass';
import UpdateClass from './UpdateClass';
import DeleteClass from './DeleteClass';
import './ClassesList.css'; // Import your styles

const ClassesList = () => {
  const [classes, setClasses] = useState([]);
  const [selectedClass, setSelectedClass] = useState(null);

  const fetchClasses = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/classes');
      const data = await response.json();
      setClasses(data);
    } catch (error) {
      console.error('Error fetching classes:', error);
    }
  };

  useEffect(() => {
    fetchClasses();
  }, []);

  const handleAddClass = async (newClass) => {
    try {
      const response = await fetch('http://localhost:5000/api/classes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newClass),
      });

      if (response.ok) {
        fetchClasses();
      } else {
        console.error('Failed to add class:', response.statusText);
      }
    } catch (error) {
      console.error('Error adding class:', error);
    }
  };

  const handleUpdateClass = (classInfo) => {
    setSelectedClass(classInfo);
  };

  const handleDeleteClass = async (classInfo) => {
    try {
      const response = await fetch(`http://localhost:5000/api/classes/classes${classInfo.class_id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        fetchClasses();
      } else {
        console.error('Failed to delete class:', response.statusText);
      }
    } catch (error) {
      console.error('Error deleting class:', error);
    }
  };

  return (
    <div className="classes-list">
      <h2>Classes List</h2>
      <AddClass onAddClass={handleAddClass} />
      <ul>
        {classes.map((classInfo) => (
          <li key={classInfo.class_id} className="class-item">
            {/* ... (unchanged code) */}
            <div className="class-actions">
              <button onClick={() => handleUpdateClass(classInfo)}>Update</button>
              <button onClick={() => handleDeleteClass(classInfo)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
      {selectedClass && (
        <UpdateClass
          classInfo={selectedClass}
          onUpdateClass={() => {
            fetchClasses();
            setSelectedClass(null);
          }}
          onCancel={() => setSelectedClass(null)}
        />
      )}
    </div>
  );
};

export default ClassesList;