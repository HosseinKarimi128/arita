// Sample data
const data = {
  facts: [
    "The Earth orbits the Sun.",
    "Water is composed of hydrogen and oxygen.",
    // Add more fact strings as needed
  ],
  metadatas: [
    { tools: "ToolA", type: "Type1", kw: "Keyword1" },
    { tools: "ToolB", type: "Type2", kw: "Keyword2" },
    // Add more metadata objects as needed
  ],
};

// Make the POST request using fetch
fetch('http://127.0.0.1:8324/insert-texts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json', // Specify the content type
  },
  body: JSON.stringify(data), // Convert the data to JSON
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`Server error: ${response.statusText}`);
    }
    return response.json(); // Assuming the server returns JSON
  })
  .then(responseData => {
    console.log('Success:', responseData);
  })
  .catch(error => {
    console.error('Error:', error);
  });

