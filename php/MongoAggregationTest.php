<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');

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
      $this->mongoclient = new MongoClient();
      $this->db = $this->mongoclient->selectDB("zips");
      $this->zips = $this->db->selectCollection("zips");
    }

    public function tearDown(){
        $this->mongoclient->close();
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

        $result = $this->zips->aggregate();
        $this->assertEquals('CHICAGO', $result['result'][0]['city']);
    }

    /**
     *  Même question que précedemment mais en normalisant le nom de la ville dans l'id
     * par exemple : chicago IL - zipcode
     */
    public function testFindLargestCityWithNormalizedName(){

        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('chicago IL - 60623', $result['result'][0]['_id']);
    }

    /**
     *  Quelle est la ville dont l'un des quartiers (code postal) a la plus grande population uniquement dans l'état de New York (NY)
     */
    public function testFindLargestZipCodeAmongstCityOfNewYork(){

        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('BROOKLYN', $result['result'][0]['city']);
    }

    /**
     *  Trouver l'état avec le plus de quartier
     */
    public function testStateWithTheLargestNumberOfZipCodes(){
        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('TX', $result['result'][0]['_id']);
        $this->assertEquals('1676', $result['result'][0]['number_of_zipcode']);
    }

    /**
     *  Trouver le second état avec le plus de quartier
     */
    public function testSecondStateWithTheLargestNumberOfZipCodes(){
        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('NY', $result['result'][0]['_id']);
        $this->assertEquals('1596', $result['result'][0]['number_of_zipcode']);
    }

    /**
     *  Trouver l'état avec la plus grande population
     */
    public function testStateWithLargestPopulation(){
        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('CA', $result['result'][0]['_id']);
        $this->assertEquals('29760021', $result['result'][0]['total_pop']);
    }

    /**
     *  Quelle est la plus grande ville de l'état de New York (sans utiliser skip et limit mais avec first ou last)
     */
    public function testLargestCityInNewYork(){

        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals('BROOKLYN', $result['result'][0]['largest_city']);
        $this->assertEquals(2300504, $result['result'][0]['largest_pop']);
    }


    /**
     *  Quelle est la moyenne de population d'une ville dans l'état de New York (NY)
     */
    public function testAvgPopulationByCityInNewYork(){

        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals(13122, round($result['result'][0]['avg_city_pop']));
    }
}
?>