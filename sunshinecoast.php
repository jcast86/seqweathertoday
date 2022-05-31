<!DOCTYPE html>
<html>

<head>
    <title>SEQ Weather Today | Sunshine Coast</title>
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php
    exec('sudo python /var/www/html/scripts/suncoast.py');
    ?>
</head>

    <header><strong>SEQ Weather Today</strong></header>

<div class="topnav">
    <a href="index.html">Home</a>
    <a href="goldcoast.php">Gold Coast</a>
    <a href="brisbane.php">Brisbane</a>
    <a class="active" href="sunshinecoast.php">Sunshine Coast</a>
</div>
<body>
    <br>
    <p1>Today's Weather on the Sunshine Coast</p1>
    <p><strong>Air Temperature (°C)</strong></p>
    <img src="./img/suncoast/temp.png">
    <br>
    <p><strong>Wind Speed (km/h)</strong></p>
    <img src="./img/suncoast/wind.png">
    <br>
    <p><strong>Relative Humidity (%)</strong></p>
    <img src="./img/suncoast/humidity.png">
    <br>
    <br>
    <a href="./img/suncoast/response_suncoast.txt" download><button type="button">View raw data</button></a>
    <br>
    <br>
    <a href="http://www.bom.gov.au/qld/forecasts/maroochydore.shtml" download><button type="button">View Sunshine Coast Weather Forecast on BOM</button></a>
</body>
</html>