<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');


/**
 * Class MongoFindTest
 * Cette classe va nous permettre de faire nos premiers pas avec l'API de requêtage de MongoDB
 */
class MongoFindTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;
    private $db;
    private $movies;

    /**
     * Initialisation des membres privés à compléter
     */
    public function setUp(){
      $this->mongoclient = null; //TODO
      $this->db = null; //TODO sélectionner la base de données mediatheque
      $this->movies = null; //TODO sélectionner la collection movies
    }

    public function tearDown(){
        $this->mongoclient->close();
    }

    /**
     *  Ce test d'exemple permet de vérifier que nous avons bien 350 films en base de données
     */
    public function testThatDatabaseHas350Movies(){

        // TODO compter le nombre de films dans la base de données (count)
        $nbMoviesInDatabase = null;

        $this->assertEquals($nbMoviesInDatabase, 350);
    }

    /**
     * Ce test doit vérifier que nous avons 69 films de 'Crime'
     */
    public function testThatMovieWithGenreCrimeAre69(){
        // TODO compter le nombre de films dont l'un des genres est 'Crime'
        $nbCrimeMoviesInDatabase = null;

        $this->assertEquals($nbCrimeMoviesInDatabase, 69);
    }

    /**
     * Ce test ne doit récupérer que le champ 'title' de la base
     */
    public function testProjectionOnTitle(){

        // TODO faire une recherche d'un élément avec une projection sur le titre (et uniquement le titre)
        $query = null;
        $movie = null;

        $this->assertArrayHasKey('title', $movie);
        $this->assertTrue(count(array_keys($movie)) == 1);
    }

    /**
     * Ce test doit vérifier que nous avons 118 films avec une note comprise entre 7 et 8
     */
    public function testRatingBetween7And8(){

        // TODO faire un comptage des films dont la note est comprise entre 7 et 8 (inclus)
        $nbMoviesInRange78 = null;

        $this->assertEquals($nbMoviesInRange78, 118);
    }

    /**
     * Ce test vérifie que nous avons 24 films de 'Comedy' et de 'Romance' (simultanèment)
     */
    public function testAllMovieComedyAndRomance(){

        // TODO compter le nombre de films de genre Comedy et Romance
        $nbComedyAndRomanceMovies = null;

        $this->assertEquals($nbComedyAndRomanceMovies, 24);
    }

    /**
     * Ce test vérifie que nous avons 243 films qui ne sont ni des 'Comedy', ni des films de 'Romance'
     */
    public function testAllMovieNotComedyAndRomance(){

        // TODO
        $nbMoviesNeitherRomanceNeitherComedy = null;

        $this->assertEquals($nbMoviesNeitherRomanceNeitherComedy, 243);
    }

    /**
     * Ce test vérifie que nous avons 53 films de sciences fiction, ou dont l'un des acteurs est Morgan Freeman
     */
    public function testAllMovieScienceFictionOrWithMorganFreeman(){

        // TODO
        $nbSciFiMoviesOrWithMorganFreeman = null;

        $this->assertEquals($nbSciFiMoviesOrWithMorganFreeman, 53);
    }

    /**
     * Ce test vérifie que nous avons 335 films dont le champ also_known_as existe
     */
    public function testAllMoviesWithFieldAlsoKnownAs(){

        // TODO
        $nbMoviesWithAnAlias = null;

        $this->assertEquals($nbMoviesWithAnAlias, 335);
    }

    /**
     * Ce test vérifie que nous avons 21 films tournés à New York
     */
    public function testMoviesLocationMatchingNewYork(){

        // TODO
        $nbMoviesFilmedInNewYork = null;

        $this->assertEquals($nbMoviesFilmedInNewYork, 21);
    }

}
?>