<?php
	$return = [];

	if(empty($_POST["username"]) || empty($_POST["password"]) || empty($_POST["firstname"]) || empty($_POST["lastname"])) {
		$return = ["messageCode" => 4];
	} else {
		$user = $db->query("INSERT INTO users SET firstname=:firstname, lastname=:lastname, username=:username, password=:password", [
			":firstname" => $_POST["firstname"],
			":lastname" => $_POST["lastname"],
			":username" => $_POST["username"],
			":password" => md5($_POST["password"])
		]);

		if($user) {
			$return = ["messageCode" => 6];
			$_SESSION["user_id"] = $user;
		} else
			$return = ["messageCode" => 7];
	}

	echo json_encode($return);

?>