fetch(`/api/products/${product.id}`, {
  method: "PUT",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: updatedName,
    description: updatedDescription,
    price: updatedPrice,
    image: updatedImage
  }),
})
.then(res => res.json())
.then(data => alert(data.message));
