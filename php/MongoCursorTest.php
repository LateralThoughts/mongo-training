<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');


/**
 * Class MongoCursorTest
 * Utilisation des curseurs pour trier, sauter, limiter
 */
class MongoCursorTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $movies;

    /**
     * Initialisation des membres privés à compléter
     */
    public function setUp(){
      $this->mongoclient = new MongoClient();
      $this->db = $this->mongoclient->selectDB("mediatheque");
      $this->movies = $this->db->selectCollection("movies");
    }

    public function tearDown(){
        $this->mongoclient->close();
    }

    /**
     *  Ce test permet de vérifier le titre du 10eme film trié par note ascendante
     */
    public function testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne(){

        // TODO
        $cursor = null;

        foreach($cursor as $movie) {
            $this->assertEquals($movie['title'], 'Yûsei ôji');
        }
    }

}
?>