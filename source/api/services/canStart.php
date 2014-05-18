<?php
	if(empty($_GET['canStart'])) {
		echo json_encode(["messageCode" => 4]);
	} else {
		$game = $db->first("SELECT teams FROM games WHERE id=:id", [":id" => $_GET['canStart']]);
		$teams = json_decode($game["teams"]);
		$total_player = 0;
		foreach($teams as $team_name=>$team_player) {
			$total_player += count($team_player);
		}

		if($total_player == 4) {
			echo json_encode(["messageCode" => 14]);
		} else {
			echo json_encode(["messageCode" => 15]);
		}
	}