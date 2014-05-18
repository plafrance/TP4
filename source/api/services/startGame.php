<?php
	if(!isset($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else if(empty($_POST['type_of_chracter'])) {
		echo json_encode(["messageCode" => 4]);
	} else {
		$game_id = $db->query("INSERT INTO games SET teams=:teams", [
			":teams" => json_encode([
				"team1" => [
						[$_SESSION["user_id"], $_POST["type_of_chracter"]]
					],
				"team2" => []
				])
			]);
		echo json_encode(["messageCode" => 13, "id" => $game_id]);
	}
?>