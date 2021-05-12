<?php
    include 'header.php';
?>

<!-- Navbar items -->
<div id="navlist">
    <a href="#">Home</a>
    <a href="#">About Us</a>
    <a href="#">Contact Us</a>
<!-- Heaadings -->
<h1>Travellers at LA</h1>
    
<b>
    Plan your trip to LA with just a few clicks
</b>
         
         
<p>
    How many times were you frustrated while
    planning the route for your roadtrip? We 
    are to provide a much simpler solution.
</p>
<!-- Search box -->
<!-- Load icon library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<!-- The form -->
<form class="searchbox" action="search.php" method="POST">
    <input type="text" placeholder="Enter museum to see popular museums in LA" name="search">
    <button type="submit" name="submit-search"><i class="fa fa-search"></i></button>
</form>

<div class="places-container">
    <?php 
        $sql = "SELECT * FROM top150_touristsite";
        $result = mysqli_query($conn, $sql);
        $queryResults = mysqli_num_rows($result);

        if($queryResults >0){
            while($row = mysqli_fetch_assoc($result)){
                echo "<div class = 'place-box'>
                    <h3><a href=".$row['Site Link'].">".$row['Tourist Site Name']."</a></h3>
                    <p> Rank: ".$row['Rank']."</p>
                </div>";
            }
        }
    ?>
    
</div>
</body>

</html>
