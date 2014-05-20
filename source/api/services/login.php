<?php
	$return = [];

	if(empty($_POST["username"]) || empty($_POST["password"])) {
		$return = ["messageCode" => 4];
	} else {
		$user = $db->first("SELECT id FROM users WHERE username=:username AND password=:password", [
			":username" => $_POST["username"],
			":password" => md5($_POST["password"])
		]);

		if($user) {
			$return = ["messageCode" => 2];
			$_SESSION["user_id"] = $user['id'];
		} else
			$return = ["messageCode" => 3];
	}

	echo json_encode($return);

?>