<?php
require 'vendor/autoload.php';


/**
 * Class MongoDBTest
 * Cette classe est utilisée pour faire nos premiers pas avec Mongodb et le driver PHP
 */
class MongoDBTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $movies;

    /**
     *  Ce test permet de vérifier la connexion à une collection
     */
    public function testThatWeCanConnectToACollection(){
        $this->mongoclient = new MongoDB\Client();
        $this->db = $this->mongoclient->selectDatabase("mediatheque");
        $this->movies = $this->db->selectCollection("movies");
        $this->assertEquals("movies", $this->movies->getCollectionName());
    }

}
?>