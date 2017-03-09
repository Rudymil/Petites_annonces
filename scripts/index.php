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
				float:left; /* horizontal */
				margin-right: 70px;
				width: 200px;
			}
			#mapid {
				height: 400px;
			    width: 700px;
			    float:left; /* horizontal */
			}
			#main {
				margin-left: 70px; 
				margin-right: 70px;
			}
			#description{
				margin-left: 70px;
				float:left; /* horizontal */
			}
			#apercue{
				margin-left: 270px;
				margin-right: 70px;
			    width: 700px;
			}
			.bouton {
				width: 200px;
			}
			#apercue {
			    border-collapse: collapse;
				margin-right: 70px;
			    margin-top: 450px;
			}
			td, th {
			    border: 1px solid black;
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
			foreach ( $cursor as $key => $val) {
				//echo "$id: ";
				//var_dump( $value );
				$tableau[$key] = $val;
			}
		?>
		<!-- HTML -->
		<center><h1>Petites annonces</h1></center>
		<div id="main">
			<div id="menu">
				<center><h2>Menu</h2></center>
				<!-- PHP -->
				<?php
					$services = array();
					foreach($tableau as $key => $val){ // pour chaque id de tableau
				        //echo $key;
				        //var_dump( $val );
				        foreach($val as $key => $val){ // pour chaque service d un id
					        if ($key == '_id'){ // si on a a faire avec le champs _id
					        }
					        elseif (array_key_exists($key, $services)){ // si services contient deja la clef
					        	//array_push($services[$key], $val); // on ajoute la valeur a la clef
					        }
					        else {
								$services[$key] = $val; // on ajoute la clef et la valeur
								echo "<center><input class='bouton' type='button' value='$key'></center>"; // on cree le bouton
					        }
					    }
					}
					/*foreach($services as $key => $val){ // verification !!!
						echo $key;
						var_dump( $val );
					}*/
				?>
				<!-- HTML -->
			</div>
			<div id="mapid"></div>
			<div id="description">
				<center><h3>Description</h3></center>
			</div>
		</div>
		<table id="apercue">
			<tr id="entete=">
				<th id="id">id</th>
				<th id="pseudo">pseudo</th>
				<th id="titre">titre</th>
				<th id="tarif">tarif</th>
				<th id="date">date</th>
				<th id="libelle">libelle</th>
			</tr>
		</table>
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