<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');

/**
 * Class MongoAnalyticsTest
 * Framework d'aggrégation et MapReduce pour manipuler des données analytiques
 */
class MongoAnalyticsTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $hits;

    public function setUp(){
      $this->mongoclient = new MongoClient();
      $this->db = $this->mongoclient->selectDB("analytics");
      $this->hits = $this->db->selectCollection("hits");
    }

    public function tearDown(){
        $this->mongoclient->close();
    }

    /**
     * Trouver la plus grande affluence (nombre de requêtes par jour) pour l'url http://www.lateral-thoughts.com
     * avec le framework d'aggrégation
     */
    public function testFindHighestHitsForUrl(){
        // TODO définir le pipeline

        $result = $this->zips->aggregate();
        $this->assertEquals(66, $result['result'][0]['hits']);
        $this->assertEquals(2012, $result['result'][0]['_id']['y']);
        $this->assertEquals(3, $result['result'][0]['_id']['m']);
        $this->assertEquals(23, $result['result'][0]['_id']['d']);
    }

    /**
     * Trouver la plus grande affluence (nombre de requêtes par jour) pour l'url http://www.lateral-thoughts.com
     * avec un map reduce
     */
    public function testFindHighestHitsForUrlWithMapReduce(){
        $map = null;
        $reduce = null;

        $this->db->command(array(
            "mapreduce" => "hits",
            "map" => $map,
            "query" => array("url" => 'http://www.lateral-thoughts.com'),
            "reduce" => $reduce,
            "out" => "hits_per_url"));

        $hits_per_url = $this->db->selectCollection("hits_per_url");
        $query = array('_id.url'=>'http://www.lateral-thoughts.com');
        $this->assertTrue($hits_per_url->count($query)>0);
        $stats = $hits_per_url->find($query)->sort(array('value'=>-1))->limit(1);
        foreach($stats as $stat) {
            $this->assertEquals(66, $stat['value']);
            $this->assertEquals(2012, $stat['_id']['y']);
            $this->assertEquals(3, $stat['_id']['m']);
            $this->assertEquals(23, $stat['_id']['d']);
        }
    }
}
?>