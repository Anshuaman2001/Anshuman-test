import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";
import UpdateProduct from "./components/updateProduct";
import DepartmentList from "./components/DepartmentList";
import DepartmentPage from "./components/DepartmentPage";

function App() {
  return (
    <Router>
      <div style={{ display: "flex", gap: "2rem", padding: "2rem" }}>
        {/* Sidebar or top navigation for departments */}
        <div style={{ minWidth: "200px" }}>
          <DepartmentList />
        </div>

        {/* Main content area */}
        <div style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<ProductList />} />
            <Route path="/product/:id" element={<ProductDetail />} />
            <Route path="/update/:id" element={<UpdateProduct />} />
            <Route path="/departments/:departmentName" element={<DepartmentPage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
