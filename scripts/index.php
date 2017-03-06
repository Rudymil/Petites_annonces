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
			#title { text-align: center; }
			#mapid { margin-left: 70px; margin-right: 70px; height: 300px; }
		</style>
	</head>
	<!-- BODY -->
	<body>
		<h1 id="title">Petites annonces</h1>
		
		<div id="mapid"></div>
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
	</body>
</html>
