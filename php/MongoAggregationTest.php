<?php

require 'vendor/autoload.php';

/**
 * Class MongoAggregationTest
 * Prise en main du framework d'aggrégation
 */
class MongoAggregationTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $zips;

    /**
     * Initialisation des membres privés à compléter
     */
    public function setUp(){
      $this->mongoclient = new MongoDB\Client();
      $this->db = $this->mongoclient->selectDatabase('zips');
      $this->zips = $this->db->selectCollection('zips');
    }

    public function tearDown(){
    }

    /**
     *  Ce test d'exemple permet de vérifier que nous avons bien 29467 zipcode en base de données
     */
    public function testThatDatabaseHasZipcodes(){
        $this->assertEquals($this->zips->count(), 29467);
    }

    /**
     *  Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population (utiliser uniquement skip limit et sort)
     */
    public function testFindLargestZipCodeAmongstCity(){

        // TODO définir le pipeline
        $pipeline = [];

        $result = $this->zips->aggregate($pipeline);
        $this->assertEquals('CHICAGO', $result->toArray()[0]['city']);
    }

    /**
     *  Même question que précedemment mais en normalisant le nom de la ville dans l'id
     * par exemple : chicago IL - zipcode
     */
    public function testFindLargestCityWithNormalizedName(){

        // TODO définir le pipeline
        $pipeline = [];

        $result = $this->zips->aggregate($pipeline);
        $this->assertEquals('chicago IL - 60623', $result->toArray()[0]['_id']);
    }

    /**
     *  Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population uniquement dans l'état de New York (NY)
     */
    public function testFindLargestZipCodeAmongstCityOfNewYork(){

        // TODO définir le pipeline
        $pipeline = [];
        $result = $this->zips->aggregate($pipeline);
        $this->assertEquals('BROOKLYN', $result->toArray()[0]['city']);
    }

    /**
     *  Trouver l'état avec le plus de quartier
     */
    public function testStateWithTheLargestNumberOfZipCodes(){
        // TODO définir le pipeline
        $pipeline = [];

        $result = $this->zips->aggregate($pipeline)->toArray();

        $this->assertEquals('TX', $result[0]['_id']);
        $this->assertEquals('1676', $result[0]['number_of_zipcode']);
    }

    /**
     *  Trouver le second état avec le plus de quartier
     */
    public function testSecondStateWithTheLargestNumberOfZipCodes(){
        // TODO définir le pipeline
        $pipeline = [];
        $result = $this->zips->aggregate($pipeline)->toArray();
        $this->assertEquals('NY', $result[0]['_id']);
        $this->assertEquals('1596', $result[0]['number_of_zipcode']);
    }

    /**
     *  Trouver l'état avec la plus grande population
     */
    public function testStateWithLargestPopulation(){
        // TODO définir le pipeline
        $pipeline = [];
        $result = $this->zips->aggregate($pipeline)->toArray();
        $this->assertEquals('CA', $result[0]['_id']);
        $this->assertEquals('29760021', $result[0]['total_pop']);
    }

    /**
     *  Quelle est la plus grande ville de l'état de New York (sans utiliser skip et limit mais avec first ou last)
     */
    public function testLargestCityInNewYork(){

        // TODO définir le pipeline
        $match = [];
        $groupByCity = [];
        $sort = [];;
        $findLargest = [];

        $pipeline = [$match, $groupByCity, $sort, $findLargest];
        $result = $this->zips->aggregate($pipeline)->toArray();
        
        $this->assertEquals('BROOKLYN', $result[0]['largest_city']);
        $this->assertEquals(2300504, $result[0]['largest_pop']);
    }


    /**
     *  Quelle est la moyenne de population d'une ville dans l'état de New York (NY)
     */
    public function testAvgPopulationByCityInNewYork(){

        // TODO définir le pipeline
        $match = [];
        $groupByCityAndState = [];
        $findAverage = [];
        
        $pipeline = [$match, $groupByCityAndState, $findAverage];
        $result = $this->zips->aggregate($pipeline)->toArray();

        $this->assertEquals(13122, round($result[0]['avg_city_pop']));
    }
}
?>