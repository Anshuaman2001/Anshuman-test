import React, { useEffect, useState } from "react";
import axios from "axios";

const ProductList = ({ onSelect }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/products")
      .then((res) => setProducts(res.data))
      .catch((err) => console.error("Error fetching products:", err));
  }, []);

  return (
    <div>
      <h2>All Products</h2>
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
