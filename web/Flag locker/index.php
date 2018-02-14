<?php

$flag ="xiomara{s0metim3s_fl@g_c@n_b3_d3cl@red_@s_v@riable}";

$fun="why";
if ( isset($_GET["locker"]) ){
    $fun = $_GET["locker"];
}
include($fun."_locker.php");
?>

<html>
<head><title>Xiomara flag locker</title></head>

<body>

<h1 align ="center">Xiomara flag locker</h1>

<p align = "center"><img src ="indiaflag.gif" align = "center"></p>

<center><h3>
    <?php echo $lang['lang']; ?> : 
    <a href="?locker=why" style="text-decoration:<?php ($fun=="why")?print "underline":print "none"; ?>">Why us?</a>
    &nbsp;|&nbsp;
    <a href="?locker=privacy" style="text-decoration:<?php ($fun=="privacy")?print "underline":print "none"; ?>">Privacy policy</a>
</h3></p>

<p><?php echo $lang["welcome"]; ?></p></center

</body>
</html>

