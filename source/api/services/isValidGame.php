<?php
	if(empty($_GET['isValidGame'])) {
		echo json_encode(["messageCode" => 4]);
	} else {
		$game = $db->first("SELECT teams FROM games WHERE id=:id", [":id" => $_GET['isValidGame']]);
		if($game) {
			$total_player = 0;
			$teams = json_decode($game["teams"],true);
			foreach($teams as $team_name=>$team_player) {
				$total_player += count($team_player);
			}
			if($total_player == 4) {
				echo json_encode(["messageCode" => 14]);
			} else {
				echo json_encode(["messageCode" => 17]);
			}
		} else {
			echo json_encode(["messageCode" => 18]);
		}
	}