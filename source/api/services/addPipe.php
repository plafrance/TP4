<?php
	if(empty($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else {
		$pipes = $db->query("INSERT INTO pipes SET user_id=:user_id, type=:type, command=:command, game_id=:game_id", [
			":user_id" => $_SESSION['user_id'],
			":type" => $_POST["type"],
			":command" => $_POST["command"],
			":game_id" => $_GET["addPipe"]
		]);

		echo json_encode(["messageCode" =>19]);
	}