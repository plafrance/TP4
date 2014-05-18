<?php
	if(empty($_SESSION["user_id"])) {
		echo json_encode(["messageCode" => 5]);
	} else if(empty($_GET['playerInGame'])) {
		echo json_encode(["messageCode" => 4]);
	} else {
		$game = $db->first("SELECT teams FROM games WHERE id=:id", [":id" => $_GET['playerInGame']]);
		$teams = json_decode($game["teams"]);
		$total_player = 0;
		foreach($teams as $team_name=>$team_player) {
			$total_player += count($team_player);
		}

		if($total_player == 4) {
			echo json_encode(["messageCode" => 14, "count_players" => $total_player]);
		} else {
			echo json_encode(["messageCode" => 15, "count_players" => $total_player]);
		}
	}