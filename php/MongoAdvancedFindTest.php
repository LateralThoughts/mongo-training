<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');


/**
 * Class MongoFindTest
 */
class MongoAdvancedFindTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $grades;

    /**
     * Initialisation des membres privés à compléter
     */
    public function setUp(){
      $this->mongoclient = new MongoClient();
      $this->db = $this->mongoclient->selectDB("grades");
      $this->grades = $this->db->selectCollection("grades");
    }

    public function tearDown(){
//        $this->mongoclient->close();
    }

    /**
     *  Ce test d'exemple permet de vérifier que nous avons bien 280 notes en base de données
     */
    public function testThatDatabaseHas280Grades(){
        $this->assertEquals($this->grades->count(), 280);
    }

    /**
     * Ce test doit vérifier que nous avons 77 enregistrements qui n'ont que 3 notes
     */
    public function testThatWeHave77LinesWith3Grades(){
        $this->assertEquals($this->grades->count(array('scores' => array('$size'=>3))), 77);
    }

    /**
     * Ce test doit vérifier que toutes les notes ont des examens
     */
    public function testNumberOfGradesWithExam(){
        $this->assertEquals($this->grades->count(array('scores.type' => 'exam')), 280);
    }

    /**
     * Ce test doit vérifier que toutes les notes ont des examens
     */
    public function testNumberOfGradesWithExamGreaterThan60(){
        $this->assertEquals($this->grades->count(array(
                                                    'scores' => array(
                                                                    '$elemMatch'=> array(
                                                                                        'type' => 'exam',
                                                                                        'score'=>array(
                                                                                                      '$gt'=>60
                                                                                                 )
                                                                                   )
                                                                )
                                                 )
                                                ), 117);
    }

    /**
     * Ce test doit vérifier que nous pouvons ne renvoyer qu'une seule note par grade
     */
    public function testWeCanRetrieveOnlyOneScorePerGrade(){
        $grade = $this->grades->findOne(array(),array('scores'=>array('$slice'=>1)));
        $this->assertArrayHasKey('scores', $grade);
        $this->assertEquals(count($grade['scores']) , 1);
    }
}
?>