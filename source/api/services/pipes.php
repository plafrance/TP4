<?php
	if(empty($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else {
		$pipes = $db->query("SELECT id, command, type, user_id FROM `pipes` WHERE `id` > :id AND `game_id` = :game_id", [
			":id" => $_GET["last_id"],
			":game_id" => $_GET["pipes"]
		]);

		$r = ["commands"=>[]];
		foreach($pipes as $command) {
			$r["commands"][] = ["command"=>$command["command"], "user_id"=>$command["user_id"], "type"=>$command["type"]];
		}
		if(empty($pipes))
			$r["last_id"] = $_GET["last_id"];
		else
			$r["last_id"] = end($pipes)["id"];

		echo json_encode($r);
	}