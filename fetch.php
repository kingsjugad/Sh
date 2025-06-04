<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Travel Plan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
        <?php
$conn = new mysqli('localhost', 'root', '', 'trip1');

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Fetch and display rows
$sql = "SELECT * FROM new ORDER BY id DESC";
$result = $conn->query($sql);
 
if ($result->num_rows > 0) {
    echo "<h2>Registered Participants</h2>";
    echo "<table border='1' cellpadding='5' cellspacing='0'>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Gender</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Description</th>
            </tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>".htmlspecialchars($row["id"])."</td>
                <td>".htmlspecialchars($row["firstname"])."</td>
                <td>".htmlspecialchars($row["age"])."</td>
                <td>".htmlspecialchars($row["gender"])."</td>
                <td>".htmlspecialchars($row["email"])."</td>
                <td>".htmlspecialchars($row["phone"])."</td>
                <td>".htmlspecialchars($row["description"])."</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "<p>No registrations yet.</p>";
}

$conn->close();
?>
</body>
</html>