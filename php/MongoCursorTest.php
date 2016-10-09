<?php
require 'vendor/autoload.php';

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
      $this->mongoclient = new MongoDB\Client();
      $this->db = $this->mongoclient->selectDatabase("mediatheque");
      $this->movies = $this->db->selectCollection("movies");
    }

    public function tearDown(){
        
    }

    /**
     *  Ce test permet de vérifier le titre du 10eme film de Sci-Fi trié par note ascendante
     */
    public function testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne(){

        // TODO
        $movie = $this->movies->find()->toArray()[0];
        $this->assertEquals($movie['title'], 'Space Mutiny');

    }

}
?>