import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";

function DepartmentPage() {
  const { departmentName } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get(`/api/departments/${departmentName}/products`)
      .then(res => setProducts(res.data))
      .catch(err => console.error(err));
  }, [departmentName]);

  return (
    <div>
      <h2>{departmentName.toUpperCase()} Department</h2>
      <p>{products.length} product(s) found</p>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name} - ₹{product.price}</li>
        ))}
      </ul>
      <Link to="/">⬅ Back to All Products</Link>
    </div>
  );
}

export default DepartmentPage;
