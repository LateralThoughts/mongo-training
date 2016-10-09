<?php
require 'vendor/autoload.php';

/**
 * Class MongoWriteTest
 * Test d'écritures en bases de données
 */
class MongoWriteTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $cds;

    public function setUp(){

        // Nécessaire pour les manipulations de dates que vous allez effectuer plus bas
        date_default_timezone_set('UTC');

        $this->mongoclient = new MongoDB\Client();
        $this->db = $this->mongoclient->selectDatabase("mediatheque");
        $this->cds = $this->db->selectCollection("cds");

        // Ce test repart d'une collection vide à chaque lancement
        // TODO
    }

    public function tearDown(){
    }

    /**
     *  Ce test d'exemple permet de vérifier que nous avons bien 0 CDs en base de données
     */
    public function testThatDatabaseHas0Movies(){
        $this->assertEquals($this->cds->count(), 0);
    }

    /**
     *  Ce test permet de vérifier qu'une insertion est prise en compte
     */
    public function testInsertWorks(){

        $cd = array(
            'name' => 'cd1'
        );

        // TODO faire l'insertion

        // FIN TODO

        $this->assertEquals($this->cds->count(), 1);
    }

    /**
     *  Ce test permet de vérifier qu'une insertion est prise en compte
     */
    public function testBatchInsert(){

        $cd1 = array(
            'name' => 'cd1'
        );
        $cd2 = array(
            'name' => 'cd2'
        );

        // TODO faire l'insertion

        // FIN TODO

        $this->assertEquals($this->cds->count(), 2);
    }


    /**
     *  Ce test permet de vérifier que nous pouvons mettre à jour le nom du CD qui a le nom "cd1"
     */
    public function testUpdateName(){

        $this->testInsertWorks();


        // TODO faire la mise à jour

        // FIN TODO

        $this->assertEquals($this->cds->count(array('name' => 'new name')), 1);
        $this->assertEquals($this->cds->count(array('name' => 'cd1')), 0);
    }

    /**
     *  Ce test permet de vérifier que nous pouvons ajouter un artiste sur le CD et incrémenter un compter nbArtiste par la même occasion
     */
    public function testUpdateAndIncr(){

        $this->testInsertWorks();

        // TODO faire la mise à jour en ajoutant un tableau d'artiste et un compteur pour suivre la taille de ce tableau

        // FIN TODO
        $this->assertEquals($this->cds->count(array('name' => 'cd1', 'artists.name' => 'Kurt Cobain', 'nbArtists' => 1)), 1);
    }

    /**
     *  Ce test permet de vérifier que nous pouvons mettre a jour plusieurs CD d'un coup en ajoutant une note par défaut de 0 (rating)
     */
    public function testUpdateMulti(){

        $this->testBatchInsert();

        // TODO faire la mise à jour

        // FIN TODO
        $this->assertEquals($this->cds->count(array('rating' => 0)), 2);
    }

    /**
     *  Ce test permet de vérifier l'ajout de tag. Un tag ne peut être en double
     */
    public function testAddTag(){

        $this->testInsertWorks();

        $tags = array ('grunge', 'funk', 'soul', 'grunge');

        // TODO faire la mise à jour en ajoutant ces tags sur tous les cds

        // FIN TODO

        $cd = $this->cds->findOne();
        $this->assertEquals(count($cd['tags']), 3);
    }

    /**
     *  Ce test permet de vérifier la suppression de tag.
     */
    public function testRemoveTag(){

        $this->testAddTag();
        $tagsToRemove = ['grunge', 'funk'];

        // TODO faire la mise à jour en supprimant deux tags

        // FIN TODO

        $cd = $this->cds->findOne();
        $this->assertEquals(count($cd['tags']), 1);
    }
    
}
?>