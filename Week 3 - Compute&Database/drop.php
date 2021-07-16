<?php

// A Tool for Drop Table

include "../inc/dbinfo.inc";

$connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD);
$database = mysqli_select_db($connection, DB_DATABASE);
$query = "DROP TABLE EMPLOYEES;";

if(mysqli_query($connection, $query)) echo("Drop Complete");

?>