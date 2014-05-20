<?php
	if(!isset($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else {
		$check_item = $db->first("SELECT count(id) as count FROM store WHERE id=:store_id", [":store_id" => $_POST['store_id']]);
		if($check_item['count'] == 0)
			echo json_encode(["messageCode" => 10]);
		else
			echo json_encode(["messageCode" => 9]);
	}
?>