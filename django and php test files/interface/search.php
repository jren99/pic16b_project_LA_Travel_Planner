<?php
    include 'header.php';
?>

<h1>Search Page</h1>

<div class="places-container">
 <?php
    if(isset($_POST['submit-search'])){
        $search = mysqli_real_escape_string($conn, $_POST['search']);
        $sql = "SELECT * FROM top150_touristsite WHERE `Tourist Site Name` LIKE '%$search%'";
        $result = mysqli_query($conn, $sql);
        $queryResult = mysqli_num_rows($result);

        echo "There are ".$queryResult." results.";

        if($queryResult > 0){
            while($row = mysqli_fetch_assoc($result)){
                echo "<div class = 'place-box'>
                    <h3><a href=".$row['Site Link'].">".$row['Tourist Site Name']."</a></h3>
                    <p> Rank: ".$row['Rank']."</p>
                </div>";
            }

        }else{
            echo "There are no results maching your search!";
        }

    }
 ?>
</div>