<?php 

$email = $_POST["email"];

if(isset($_POST["email"]) && !empty($_POST["email"])){

        $response = shell_exec("echo Thankyou for subscribing! Your email id is ".$email);
echo $response;
}
       
?>
