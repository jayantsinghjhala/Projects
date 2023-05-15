<?php
$insert=false;
if(isset($_POST['name'])){
     //Set Connection variables
     $server = "localhost";
     $username = "root";
     $password = "root";
     $database = "trip";

     //Create a connection
     $con = mysqli_connect($server, $username, $password, $database, 3306);

     //check if succesfully connected
     if(!$con){
          die("Connection to the database failed due to: " . mysqli_connect_error());
     }
     echo "Success Connecting to Database<br>";

     //collecting post variables
     $name = $_POST['name'];
     $age = $_POST['age'];
     $gender = $_POST['gender'];
     $email = $_POST['email'];
     $phone = $_POST['phone'];
     $desc = $_POST['desc'];

     $sql = "INSERT INTO `trip` (`name`, `age`, `gender`, `email`, `phone`, `other`, `dt`) 
     VALUES ('$name', '$age', '$gender', '$email', '$phone', '$desc', current_timestamp());";

     //echo $sql;
     //execute the query
     if($con->query($sql) == true){
          //echo "Successfully Inserted";
          //flag for succesful insertion
          $insert=true;
     }
     else{
          echo "ERROR: $sql <br> " . $con->error;
     }
     //closing the database connection
     $con->close();
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Welcome to Travel Form</title>
     <link rel="stylesheet" href="style.css">
</head>
<body>
     <img class="bg" src="bg.jpeg" alt="SPSU Udaipur"
     <div class="container">
          <h1 style="text-align: center ;">Welcome to Sir Padampat Singhania University Goa trip Form</h1>
          <p>Enter your details to confirm your
                participation in the Trip</p>
          <?php
          if($insert==true)
          {
               echo "<p class='submitmsg'>Thank you for submitting your form. We are happy to see you joining us for the goa Trip</p>";
          }
          ?>
          <form action="index.php" method="post">
               <input type="text" name="name" id="name" placeholder="Enter your name"><br>
               <input type="text" name="age" id="age" placeholder="Enter You Age"><br>
               <select name="gender" id="gender" placeholder="Gender">
                    <option value="null" Selected>Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
               </select><br>
               <input type="text" name="email" id="email" placeholder="Enter Your Email"><br>
               <input type="text" name="phone" id="phone" placeholder="Enter your Phone Number"><br>
               <textarea name="desc" id="desc" cols="30" rows="10" placeholder="Enter any other information here"></textarea><br>
               <button class="btn">Submit</button>

          </form>
     </div>
     <script src="index.js"></script>
     
</body>
</html>
