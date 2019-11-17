<?php
    require_once('flag.php');
    if (!isset($_COOKIE['user'])) {
        setcookie('user', 'user');
        $status = 'Access Denied';
    } else {
        if ($_COOKIE['user'] === 'admin') {
            $status = "Access Granted. The flag is $flag";
        } else {
            setcookie('user', 'user');
            $status = 'Access Denied';
        }
    }
?>
<!doctype html>
<html>
<head>
    <title>Security system</title>
</head>
<body>
    <h1>
    <?php echo $status ?>
    </h1>
</body>
</html>
