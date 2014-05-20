<?php

class db {

	private $pdo;

	public function __construct($options = array()) {

		if(!isset($options['dbname'])) {
			msg("Vous devez spécifier le nom de la base de données !");
		} else {
			try {
				$this->pdo = new PDO("mysql:host=".$options['host'].";dbname=".$options['dbname'], $options['username'], $options['password'],array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
				$this->pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
				$this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			} catch(Exception $e) {
				msg("Vos informations de connexion sont erronées");
			}
		}
	}
	
	private function pdo_sql_debug($sql,$placeholders){
		foreach($placeholders as $k => $v){
			$sql = preg_replace('/'.$k.'/',"'".$v."'",$sql);
		}
		return $sql;
	}

	public function query($req, $args = array()) {
		try {
			$pre = $this->pdo->prepare($req);
			$pre->execute($args);
			if(preg_match("#SELECT#i", $req))
				return $pre->fetchAll();
			if(preg_match("#UPDATE#i", $req))
				return $pre->rowCount();
			if(preg_match("#INSERT#i", $req))
				return $this->pdo->lastInsertId();
		} catch (PDOException $e) { 
			msg($e->getMessage(). "<br> QUERY: <u>".$this->pdo_sql_debug($req, $args)."</u>");
		}
	}
	
	public function first($req, $args = array()) {
		return current($this->query($req,$args));
	}

}

$db = new db(["host" => "localhost", "username" => "c0_tp4", "password" => "Sorry but I'm not a stupid guy", "dbname" => "c0_tp4"]);

?>
