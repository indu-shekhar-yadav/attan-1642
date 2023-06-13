// Fetch the attendance data from the JSON file
fetch("fingerprint_data.json")
  .then(response => response.json())
  .then(data => {
    // Get the table body element
    const tableBody = document.querySelector("#attendanceTable tbody");

    // Iterate over the attendance data and create table rows
    data.forEach(fingerprint => {
      // Create a new row
      const row = document.createElement("tr");

      // Create cells for ID and Timestamp
      const idCell = document.createElement("td");
      const timestampCell = document.createElement("td");

      // Set the text content of the cells
      idCell.textContent = fingerprint.id;
      timestampCell.textContent = fingerprint.timestamp;

      // Append cells to the row
      row.appendChild(idCell);
      row.appendChild(timestampCell);

      // Append the row to the table body
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error(error));
