<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');


class MongoMoviesAggregationTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $movies;

    public function setUp(){
      $this->mongoclient = new MongoClient();
      $this->db = $this->mongoclient->selectDB("mediatheque");
      $this->movies = $this->db->selectCollection("movies");
    }

    public function tearDown(){
        $this->mongoclient->close();
    }

    /**
     * Trouver l'actor avec le plus grand nombre de films à son actif
     */
    public function testFindActorWithLargestPorfolio(){
        // TODO définir le pipeline

        $result = $this->zips->aggregate();

        $this->assertEquals('Robert De Niro', $result['result'][0]['_id']);
        $this->assertEquals(9, $result['result'][0]['number_of_movies']);
    }

    /**
     * Trouver l'actor avec le plus grand nombre de films à son actif
     * avec un map reduce
     */
    public function testFindActorWithLargestPorfolioWithMapReduce(){
        $map = null;
        $reduce = null;

        $this->db->command(array(
            "mapreduce" => "movies",
            "map" => $map,
            "reduce" => $reduce,
            "out" => "movies_per_actor"));

        $movies_per_actor = $this->db->selectCollection("movies_per_actor");
        $query = array();
        $this->assertTrue($movies_per_actor->count($query)>0);
        $actors = $movies_per_actor->find()->sort(array('value.count'=>-1))->limit(1);
        foreach($actors as $actor) {
            $this->assertEquals('Robert De Niro', $actor['_id']);
            $this->assertEquals(9, $actor['value']['count']);
        }
    }
}
?>