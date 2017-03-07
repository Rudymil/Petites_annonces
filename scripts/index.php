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
				width: 150px;
			}
			#mapid { 
				height: 300px;
			}
			#main {
				margin-left: 70px; 
				margin-right: 70px;
			}
		</style>
	</head>
	<!-- BODY -->
	<body>
		<center><h1>Petites annonces</h1></center>
		<div id="main">
		<div id="menu"><center><h2>Menu</h2></center></div>
		<div id="mapid"></div>
		</div>
		<!-- JAVASCRIPT -->
		<script type="text/javascript">
			var mymap = L.map('mapid').setView([46.62, 2.39], 4);
			L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
				maxZoom: 18,
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
					'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
					'Imagery © <a href="http://mapbox.com">Mapbox</a>',
				id: 'mapbox.streets'
			}).addTo(mymap);
		</script>
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
			foreach ( $cursor as $id => $value )
			{
				echo "$id: ";
				var_dump( $value );
			}
		?>
	</body>
</html>