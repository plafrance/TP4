<?php
	echo json_encode(['PHPSESSID' => explode('=',SID)[1]]);
?>