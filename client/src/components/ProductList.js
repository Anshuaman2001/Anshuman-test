import React, { useEffect, useState } from "react";
import axios from "axios";

const ProductList = ({ onSelect }) => {
  const [products, setProducts] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [selectedDept, setSelectedDept] = useState("");

  // Fetch departments on first load
  useEffect(() => {
    axios.get("http://localhost:5000/api/departments")
      .then((res) => setDepartments(res.data))
      .catch((err) => console.error("Error fetching departments:", err));
  }, []);

  // Fetch products whenever selected department changes
  useEffect(() => {
    const endpoint = selectedDept
      ? `http://localhost:5000/api/departments/${selectedDept}/products`
      : "http://localhost:5000/api/products";

    axios.get(endpoint)
      .then((res) => setProducts(res.data))
      .catch((err) => console.error("Error fetching products:", err));
  }, [selectedDept]);

  return (
    <div>
      <h2>All Products</h2>

      <label>Filter by Department: </label>
      <select onChange={(e) => setSelectedDept(e.target.value)} value={selectedDept}>
        <option value="">All</option>
        {departments.map((d, idx) => (
          <option key={idx} value={d.department}>
            {d.department}
          </option>
        ))}
      </select>

      <ul>
        {products.map((p) => (
          <li key={p.id} onClick={() => onSelect(p.id)} style={{ cursor: "pointer" }}>
            {p.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
