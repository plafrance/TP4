<?php
	if(!isset($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else {
		$user_data = $db->first("SELECT * FROM users WHERE id=:id", [':id' => $_SESSION['user_id']]);
		echo json_encode($user_data);
	}
?>