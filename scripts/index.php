<!DOCTYPE html>
<html lang="fr">
	<!-- HEAD -->
	<head>
		<meta charset="UTF-8" />
		<title>Petites annonces</title>
		<script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
		<link href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css" rel="stylesheet">
		<!-- CSS -->
		<style>
			#menu{
				float: left; /* horizontal */
				margin-right: 70px;
				width: 200px;
			}
			#mapid {
				height: 400px;
			}
			#main {
				margin-left: 70px; 
				margin-right: 70px;
			}
			#description{
				margin-left: 70px;
				float: right; /* horizontal */
			}
			#apercue{
				margin-left: 270px;
				margin-right: 70px;
			}
			.bouton {
				width: 200px;
			}
		</style>
	</head>
	<!-- BODY -->
	<body>
		<!-- PHP -->
		<?php
			//$con = new MongoDB\Driver\Manager("mongodb://212.194.0.132:27117"); # raspi1
			$con = new MongoDB\Driver\Manager("mongodb://localhost:27017"); # localhost:27017
			$dbname_collection = 'services.annonces';
			$query = new \MongoDB\Driver\Query( // Create query object with all options:
			        [], // query (empty: select all)
			        [ 'sort' => [ 'name' => 1 ], 'limit' => 40 ] // options
			);
			$cursor = $con->executeQuery( $dbname_collection, $query ); // Execute query and obtain cursor:
			$tableau = array();
			$services = array();
			$occ = 0;
			foreach ( $cursor as $id => $value ) {
				//echo "$id: ";
				//var_dump( $value );
				$tableau[$occ] = $value;
				$occ ++;
			}
		?>
		<!-- HTML -->
		<center><h1>Petites annonces</h1></center>
		<div id="main">
		<div id="menu">
		<center><h2>Menu</h2></center>
		<!-- PHP -->
		<?php
			$occ = 0;
			foreach($tableau as $key => $val){
		        //echo $key;
		        //var_dump( $val );
		        foreach($val as $key => $val){
			        if ($key == '_id' || in_array($key, $services)) {
			        	continue;
			        }
			        $services[$occ] = $key;
			        $occ ++;
			        echo "<center><input class='bouton' type='button' value='$key'></center>";
			    }
			}
			/*foreach($tableau as $row){
			    foreach($row as $key => $val){
			        echo $key;
			        var_dump( $val );
					echo '<br>';
			    }
			}*/
		?>
		<!-- HTML -->
		</div>
		<div id="mapid"></div>
		<div id="description">blablabla</div>
		</div>
		<table id="apercue"><tr id="entete="><td id="id">id</td><td id="pseudo">pseudo</td><td id="titre">titre</td><td id="tarif">tarif</td><td id="date">date</td><td id="libelle"></td>libelle</tr></table>
		<!-- JAVASCRIPT -->
		<script type="text/javascript">
			var mymap = L.map('mapid').setView([46.62, 2.39], 5);
			L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
				maxZoom: 18,
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
					'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
					'Imagery © <a href="http://mapbox.com">Mapbox</a>',
				id: 'mapbox.streets'
			}).addTo(mymap);
		</script>
	</body>
</html>