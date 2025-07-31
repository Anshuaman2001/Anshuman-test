import React, { useState } from "react";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";

function App() {
  const [selectedProductId, setSelectedProductId] = useState(null);

  return (
    <div style={{ display: "flex", gap: "2rem", padding: "2rem" }}>
      <ProductList onSelect={setSelectedProductId} />
      <ProductDetail productId={selectedProductId} />
    </div>
  );
}

export default App;
