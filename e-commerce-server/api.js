const token =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MjQ0MDhkMS05NDY1LTQ5OWYtYjBmNi0zYzgzYmYxMGZkMmQiLCJleHAiOjE3NzY5Mzk5MzAsInR5cGUiOiJhY2Nlc3NfdG9rZW4ifQ.IWd3cPVat21XO318q2W0gt4LGfP2Lo5-2a89Yr8Uu3o";

fetch("http://localhost:8000/vehicle", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  },
  body: JSON.stringify({
    brand: "string",
    model: "string",
    year: "string",
    price: 1,
    mileage: 1,
    description: "string",
    location: "string",
    user_id: "fb063d32-2827-4bf5-af24-9e068a408c85",
  }),
})
  .then((resp) => resp.json())
  .then((data) => console.log(data))
  .catch((err) => console.log(err));
