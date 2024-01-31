import React from 'react';

const DeleteClass = ({ classInfo, onDeleteClass, onCancel }) => {
  const handleDelete = async () => {
    // API call to delete the class
    try {
      const response = await fetch(`http://localhost:5000/api/classes/${classInfo.class_id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        onDeleteClass();
      } else {
        console.error('Failed to delete class:', response.statusText);
      }
    } catch (error) {
      console.error('Error deleting class:', error);
    }
  };

  return (
    <div>
      <h3>Delete Class</h3>
      <p>Are you sure you want to delete this class?</p>
      <button onClick={handleDelete}>Yes</button>
      <button onClick={onCancel}>No</button>
    </div>
  );
};

export default DeleteClass;