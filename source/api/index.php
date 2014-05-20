<?php
	session_start();
	// IP check
	if($_SESSION['ip_check'] != $_SERVER['REMOTE_ADDR']){
	   session_regenerate_id();
	   session_destroy();
	   session_start();
	}
	$_SESSION['ip_check'] = $_SERVER['REMOTE_ADDR'];
	require_once "lib/config.php";
	require_once "lib/utils.php";
	require_once "lib/db.class.php";
	require_once "lib/messages.php";

	$security = ["GET" => ["home", "pipes","getMessage", "sessions", "SID", "user", "username", "getStore", "canStart", "playerInGame", "isValidGame"], "POST" => ["login", "register", "startGame", "joinGame","addPipe"]];

	$method = $_SERVER["REQUEST_METHOD"];
	$service = (key($_GET) == "") ? "home" : key($_GET);

	$r = [];

	if(!in_array($service, $security[$method])) {
		$r = ["messageCode" => 1, "message" => $messages[1]];
		echo json_encode($r);
		exit();
	}

	ob_start();
	require_once("services/".$service.".php");
	$service_file = ob_get_contents();
	ob_end_clean();
	
	$r = json_decode($service_file, true);

	if(isset($_GET["withMessage"])){
		$r['message'] = $messages[$r['messageCode']];
	}

	$encode = json_encode($r);
	if($encode != "null") {
		echo $encode;
	} else {
		echo $service_file;
	}
?>