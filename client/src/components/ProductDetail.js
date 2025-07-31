import React, { useEffect, useState } from "react";
import axios from "axios";

const ProductDetail = ({ productId }) => {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    if (productId) {
      axios.get(`http://localhost:5000/api/products/${productId}`)
        .then((res) => setProduct(res.data))
        .catch((err) => console.error("Error fetching product detail:", err));
    }
  }, [productId]);

  if (!productId) return <div>Select a product to view details.</div>;
  if (!product) return <div>Loading...</div>;

  return (
    <div>
      <h3>{product.name}</h3>
      <p><strong>Price:</strong> ₹{product.price}</p>
      <p><strong>Description:</strong> {product.description}</p>
    </div>
  );
};

export default ProductDetail;
