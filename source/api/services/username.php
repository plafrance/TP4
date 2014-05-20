<?php
	if(empty($_GET['username']))
		echo json_encode(["messageCode" => 4]);
	else {
		$check = $db->first("SELECT count(id) as count FROM users WHERE username=:username", [":username" => $_GET['username']]);
		if($check['count'] == 0)
			echo json_encode(["messageCode" => 8]);
		else
			echo json_encode(["messageCode" => 9]);
	}
?>