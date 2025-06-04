<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>registration <form action=""></form></title>
</head>
<body>
    <div>
        <h1>enter the details<h1>
        <br>

    <?php

    if($_SERVER["REQUEST_METHOD"]=="POST"){



        $firstname=$_POST['firstname'];
        $age=$_POST['age'];
        $email=$_POST['email'];
        $phone=$_POST['phone'];
        $desc=$_POST['desc'];

        $conn= new mysqli('localhost','root','','registrations');

        if($conn->connect_error)
        {
            echo "failed".$conn->connect_error;
        }
        else
        {
            $stmt=$conn->prepare("INSERT INTO new(firstname,age,email,phone,description) value(?,?,?,?,?)");
            $stmt->bind_param("sisis",$firstname,$age,$email,$phone,$desc);
        
            if($stmt->execute())
            {
                echo "sucess";
            }
            else
            {
                echo "failed";
            }
            $stmt->close();
            $conn->close();
        } 

    }

   ?>
     




    <form action="form.php" method="post">
    <input type="text" name="firstname" placeholder="first name">
    <br>
    <input type="text" name="age" placeholder="age">
    <br>
    <input type="text" name="email" placeholder="email">
    <br>
    <input type="text" name="phone" placeholder="phone">
    <br>
    <input type="text" name="desc" placeholder="desc">
    <br>
    <button>submit</button>


    </form>

    </div>
</body>
</html>