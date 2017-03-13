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
			    width: 700px;
			    float: left; /* horizontal */
			    margin-bottom: 70px;
			}
			#main {
				margin-left: 70px; 
				margin-right: 70px;
			}
			#description{
				margin-left: 1020px;
				text-align: justify;
			}
			#tableau{
				margin-left: 340px;
			    border-collapse: collapse;
				margin-right: 70px;
			    margin-top: auto;
			}
			#apercue{
			    width: 700px;
			    text-align: center;
			}
			td, th {
			    border: 1px solid black;
			}
			.bouton {
				width: 200px;
			}
		</style>
	</head>
	<!-- BODY -->
	<body>
		<!-- PHP connexion -->
		<?php
			//$con = new MongoDB\Driver\Manager("mongodb://212.194.0.132:27117"); # raspi1
			$con = new MongoDB\Driver\Manager("mongodb://localhost:27017"); # localhost:27017
			$dbname_collection = 'services.annonces';
			$query = new \MongoDB\Driver\Query( // Create query object with all options:
				[] // query (empty: select all)
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
				<!-- PHP menu -->
				<?php
					$services = array();
					foreach ($tableau as $key => $val) { // pour chaque id de tableau
				        //echo $key;
				        //var_dump( $val );
						foreach ($val as $key => $val) { // pour chaque service d un id
					        if ($key == '_id'){ // si on a a faire avec le champs _id
					        	continue;
					        }
					        elseif (array_key_exists($key, $services)) { // si services contient deja la clef
					        	//array_push($services[$key], $val); // on ajoute la valeur a la clef
					        }
					        else {
								$services[$key] = $val; // on ajoute la clef et la valeur
								echo "<center><input class='bouton' type='button' value='$key' onclick='javascript:afficher_ligne(this.getAttribute(\"value\"));'></center>"; // on cree le bouton
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
			<center><h3>Description</h3></center>
			<div id="description">
			</div>
		</div>
		<div id="tableau">
			<table id="apercue">
				<!--tr id="entete">
					<th id="id">id</th>
					<th id="pseudo">pseudo</th>
					<th id="titre">titre</th>
					<th id="tarif">tarif</th>
					<th id="date">date</th>
					<th id="libelle">libelle</th>
				</tr-->
			</table>
		</div>
		<!-- JAVASCRIPT carte -->
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
		<!-- JAVASCRIPT fonctions -->
		<script type="text/javascript">
			var services = <?php echo json_encode($services); ?>; // tableau des services => annonces
			var service_actuel;
			var marker = new Array();
			//console.log(services); // verification !!!
			function afficher_ligne(service_choisi){
				//console.log("service choisie : "+service_choisi);
				//console.log(services[service_choisi]);
				service_actuel = service_choisi;
				mymap.setView([46.62, 2.39], 5);
				var occ = 0; // occurence du tableau des markers
				if (marker != null){ // si y a des markers
					for(occ = 0; occ < marker.length ; occ++) {
					    mymap.removeLayer(marker[occ]); // on enleve tous les markers
					}
					marker = []; // on vide les markers
					occ = 0;
				}
				document.getElementById("description").innerHTML = ""; // vidange
				document.getElementById("tableau").innerHTML = '<table id="apercue"><tr id="entete"><th id="id">id</th><th id="pseudo">pseudo</th><th id="titre">titre</th><th id="tarif">tarif</th><th id="date">date</th><th id="libelle">libelle</th></tr></table>'; // rajout de l entete
				for (var annonce in services[service_choisi]) {
					//console.log("annonce numero : "+annonce);
					//console.log(services[service_choisi][annonce][3]);
					document.getElementById("apercue").insertAdjacentHTML('beforeend', '<tr id='+services[service_choisi][annonce][0]+' class="ligne" onclick="javascript:afficher_descrition(this.getAttribute(\'value\'));"><td class="id">'+services[service_choisi][annonce][0]+'</td><td class="pseudo">'+services[service_choisi][annonce][1]+'</td><td class="titre">'+services[service_choisi][annonce][2]+'</td><td class="tarif">'+services[service_choisi][annonce][4]+'</td><td class="date">'+services[service_choisi][annonce][5]+'</td><td class="libelle">'+services[service_choisi][annonce][8]+'</td></tr>'); // insertion de la ligne
					//console.log(services[service_choisi][annonce][0]);
					document.getElementById(services[service_choisi][annonce][0]).setAttribute('value', services[service_choisi][annonce][3]); // attribution de la valeur en fonction de l identifiant
					marker.push(L.marker([services[service_choisi][annonce][6], services[service_choisi][annonce][7]]).bindTooltip(services[service_choisi][annonce][8], {permanent: false, className: "my-label", offset: [0, -10], direction: 'top', interactive:true})); // creation d un marker
					mymap.addLayer(marker[occ]); // ajout de la couche marker
					occ ++;
				}
			}
			function afficher_descrition(description){
				//console.log(description);
				document.getElementById("description").innerHTML = description; // ajout de la description
				var elements = document.getElementsByClassName("ligne");
				for (var i = 0; i < elements.length; i++) { // pour chaque ligne du tableau
					elements[i].style.backgroundColor= "#ffffff"; // surbrillance blanche
				}
				for (var annonce in services[service_actuel]) {
					if (services[service_actuel][annonce][3] == description){ // si la description correspond
						mymap.setView([services[service_actuel][annonce][6], services[service_actuel][annonce][7]], 12); // display
						document.getElementById(services[service_actuel][annonce][0]).style.backgroundColor = "#f6ff00"; // surbrillance jaune
					}
				}
			}
		</script>
	</body>
</html>