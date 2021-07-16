
<?php 
#include "../inc/dbinfo.inc"; 
?>
<!DOCTYPE html>

<html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Employee Information | Sample App</title>
      <!-- Latest compiled and minified CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  </head>
  <body>
    <div class="container">
    <div class="jumbotron"><h1>🧑‍💻 Employee Information | Sample App</h1></div>
<?php
  

  /* Connect to MySQL and select the database. */
  // $connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD);

  // if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();

  // $database = mysqli_select_db($connection, DB_DATABASE);

  /* Ensure that the EMPLOYEES table exists. */
  // VerifyEmployeesTable($connection, DB_DATABASE);

  /* If input fields are populated, add a row to the EMPLOYEES table. */
  // $employee_name = htmlentities($_POST['NAME']);
  // $employee_address = htmlentities($_POST['ADDRESS']);

  // if (strlen($employee_name) || strlen($employee_address)) {
  //   AddEmployee($connection, $employee_name, $employee_address);
  // }
  
?>

    <!-- Input form -->
    <form action="<?PHP echo $_SERVER['SCRIPT_NAME'] ?>" method="POST">
      <div class="form-group row" style="width:100%;margin:0;">
        <div class="col">
        <label for="NAME">Name:</label>
        <input class="form-control" type="text" name="NAME"/>
        </div>

        <div class="col">
        <label for="ADDRESS">Salary:</label>
        <input class="form-control" type="text" name="SALARY"/>
        </div>

        <div class="col">
        <label for="JOB">Job:</label>
        <select class="form-control" name="JOB">
          <option>Officer</option>
          <option>Developer</option>
          <option>Secretary</option>
          <option>Project Manager</option>
        </select>

        </div>
        <input style="height: 60%; margin-top: auto;" class="btn btn-primary" type="submit" value="Add Data" />
      </div>
    </form>

    <!-- Display table data. -->
    <div style="padding: 10px;">
      <table class="table table-hover" >
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>SALARY</th>
            <th>JOB</th>
          </tr>
        <thead>
        <tbody>
          <?php

          // $result = mysqli_query($connection, "SELECT * FROM EMPLOYEES");
          
          // while($query_data = mysqli_fetch_row($result)) {
          //   echo "<tr>";
          //   echo "<td>",$query_data[0], "</td>",
          //        "<td>",$query_data[1], "</td>",
          //        "<td>",$query_data[2], "</td>";
          //        "<td>",$query_data[3], "</td>";
          //   echo "</tr>";
          // }
          ?>
        </tbody>
      </div>
    </table>

<!-- Clean up. -->
<?php

  // mysqli_free_result($result);
  // mysqli_close($connection);

?>

  </div>
  </body>
</html>


<?php

/* Add an employee to the table. */
function AddEmployee($connection, $name, $address) {
   $n = mysqli_real_escape_string($connection, $name);
   $a = mysqli_real_escape_string($connection, $address);

   $query = "INSERT INTO EMPLOYEES (NAME, ADDRESS) VALUES ('$n', '$a');";

   if(!mysqli_query($connection, $query)) echo("<p>Error adding employee data.</p>");
}

/* Check whether the table exists and, if not, create it. */
function VerifyEmployeesTable($connection, $dbName) {
  if(!TableExists("EMPLOYEES", $connection, $dbName))
  {
     $query = "CREATE TABLE EMPLOYEES (
         ID int(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         NAME VARCHAR(45),
         ADDRESS VARCHAR(90)
       )";

     if(!mysqli_query($connection, $query)) echo("<p>Error creating table.</p>");
  }
}

/* Check for the existence of a table. */
function TableExists($tableName, $connection, $dbName) {
  $t = mysqli_real_escape_string($connection, $tableName);
  $d = mysqli_real_escape_string($connection, $dbName);

  $checktable = mysqli_query($connection,
      "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = '$t' AND TABLE_SCHEMA = '$d'");

  if(mysqli_num_rows($checktable) > 0) return true;

  return false;
}
?>                        
                