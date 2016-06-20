<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');


/**
 * Class MongoDBTest
 * Cette classe est utilisée pour faire nos premiers pas avec Mongodb et le driver PHP
 */
class MongoDBTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $movies;

    /**
     *  Ce test permet de vérifier que nous pouvons nous connecter et lister les bases présentes
     */
    public function testThatListDbWorks(){
        $this->mongoclient = null; // TODO
        $databases = null; // TODO
        $this->assertTrue($databases['ok'] == 1);
    }

    /**
     *  Ce test permet de vérifier la connexion à une collection
     */
    public function testThatWeCanConnectToACollection(){
        $this->mongoclient = null; // TODO
        $this->db = null; //TODO
        $this->movies = null; //TODO
        $this->assertEquals("movies", $this->movies->getName());
    }

}
?>