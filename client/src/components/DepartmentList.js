import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function DepartmentList() {
  const [departments, setDepartments] = useState([]);

  useEffect(() => {
    axios.get("/api/departments")
      .then(res => setDepartments(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Departments</h2>
      <ul>
        {departments.map((dept, index) => (
          <li key={index}>
            <Link to={`/departments/${dept.department.toLowerCase()}`}>
              {dept.department}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DepartmentList;
