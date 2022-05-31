<!DOCTYPE html>
<html>

<head>
    <title>SEQ Weather Today | Brisbane</title>
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php
    exec('sudo python /var/www/html/scripts/brisbane.py');
    ?>
</head>

    <header><strong>SEQ Weather Today</strong></header>

<div class="topnav">
    <a href="index.html">Home</a>
    <a href="goldcoast.php">Gold Coast</a>
    <a class="active" href="brisbane.php">Brisbane</a>
    <a href="sunshinecoast.php">Sunshine Coast</a>
</div>
<body>
    <br>
    <p1>Today's Weather in Brisbane</p1>
    <p><strong>Air Temperature (°C)</strong></p>
    <img src="./img/brisbane/temp.png">
    <br>
    <p><strong>Wind Speed (km/h)</strong></p>
    <img src="./img/brisbane/wind.png">
    <br>
    <p><strong>Relative Humidity (%)</strong></p>
    <img src="./img/brisbane/humidity.png">
    <br>
    <br>
    <a href="./img/brisbane/response_bne.txt" download><button type="button">View raw data</button></a>
    <br>
    <br>
    <a href="http://www.bom.gov.au/qld/forecasts/brisbane.shtml" download><button type="button">View Brisbane Weather Forecast on BOM</button></a>
</body>
</html>