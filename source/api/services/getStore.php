<?php
	if(!isset($_SESSION['user_id'])) {
		echo json_encode(["messageCode" => 5]);
	} else {
		$r = [];
		$store = $db->query("SELECT 
			store.*,
			weapons.name as name_w, 
			weapons.min, 
			weapons.max,
			shields.name as name_s,
			shields.strength
		 FROM `store` 
		 LEFT JOIN weapons ON
		 	store.item_id = weapons.id AND store.item_type = 0
		 LEFT JOIN shields ON
		 	store.item_id = shields.id AND store.item_type = 1"); 



	 	foreach($store as $item) {
	 		if($item["item_type"] == 0) {
	 			$r["weapons"][] = [
	 				"code"  => $item["id"],
	 				"name"  => $item["name_w"],
	 				"min"   => $item["min"],
	 				"max"   => $item["max"],
	 				"price" => $item["price"]
	 			];
	 		}
	 		if($item["item_type"] == 1) {
	 			$r["shields"][] = [
	 				"code"  => $item["id"],
	 				"name" => $item["name_s"],
	 				"strength" => $item["strength"],
	 				"price" => $item["price"]
	 			];
	 		}
	 	}

 		echo json_encode($r);
 	}

?>