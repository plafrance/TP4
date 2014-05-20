<?php
	if(empty($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else if(empty($_GET["joinGame"])) {
		echo json_encode(["messageCode" => 4]);
	} else {
		$game = $db->first("SELECT teams FROM games WHERE id=:id", [":id" => $_GET['joinGame']]);
		$teams = json_decode($game["teams"],true);

		foreach($teams as $team_name=>$team_player) {
			$team[] = [count($team_player), $team_name];
		}

		if($team[0][0] > $team[1][0]) {
			$teams[$team[1][1]][] = [$_SESSION["user_id"], $_POST["type_of_chracter"]];
		} else {
			$teams[$team[0][1]][] = [$_SESSION["user_id"], $_POST["type_of_chracter"]];
		}

		$game = $db->query("UPDATE games SET teams=:teams WHERE id=:id", [":id" => $_GET['joinGame'], ':teams' => json_encode($teams)]);

		echo json_encode(["messageCode" => 16]);
	}