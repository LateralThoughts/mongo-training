<?php
require 'vendor/autoload.php';

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
        $this->mongoclient = new MongoDB\Client();
        $this->db = $this->mongoclient->selectDatabase("mediatheque");
        $this->movies = $this->db->selectCollection("movies");
    }

    public function tearDown(){
    }

    /**
     *  Ce test d'exemple permet de vérifier que nous avons bien 350 films en base de données
     */
    public function testThatDatabaseHas350Movies(){

        // TODO compter le nombre de films dans la base de données (count)
        $nbMoviesInDatabase = $this->movies->count();

        $this->assertEquals($nbMoviesInDatabase, 350);
    }

    /**
     * Ce test doit vérifier que nous avons 69 films de 'Crime'
     */
    public function testThatMovieWithGenreCrimeAre69(){
        // TODO compter le nombre de films dont l'un des genres est 'Crime'
        $nbCrimeMoviesInDatabase = $this->movies->count();

        $this->assertEquals($nbCrimeMoviesInDatabase, 69);
    }

    /**
     * Ce test ne doit récupérer que le champ 'title' de la base
     */
    public function testProjectionOnTitle(){

        // TODO faire une recherche d'un élément avec une projection sur le titre (et uniquement le titre)
        $movie = $this->movies->findOne([], []);

        $this->assertArrayHasKey('title', $movie);
        $this->assertArrayNotHasKey('_id', $movie);
    }

    /**
     * Ce test doit vérifier que nous avons 224 films avec une note comprise entre 8 et 9
     */
    public function testRatingBetween8And9(){

        // TODO faire un comptage des films dont la note est comprise entre 8 et 9 (exclus)
        $nbMoviesInRange89 = $this->movies->count();

        $this->assertEquals($nbMoviesInRange89, 224);
    }

    /**
     * Ce test vérifie que nous avons 24 films de 'Comedy' et de 'Romance' (simultanèment)
     */
    public function testAllMovieComedyAndRomance(){

        // TODO compter le nombre de films de genre Comedy et Romance
        $nbComedyAndRomanceMovies = $this->movies->count();

        $this->assertEquals($nbComedyAndRomanceMovies, 24);
    }

    /**
     * Ce test vérifie que nous avons 243 films qui ne sont ni des 'Comedy', ni des films de 'Romance'
     */
    public function testAllMovieNotComedyAndRomance(){

        // TODO
        $nbMoviesNeitherRomanceNeitherComedy = $this->movies->count();

        $this->assertEquals($nbMoviesNeitherRomanceNeitherComedy, 243);
    }

    /**
     * Ce test vérifie que nous avons 53 films de sciences fiction, ou dont l'un des acteurs est Morgan Freeman
     */
    public function testAllMovieScienceFictionOrWithMorganFreeman(){

        // TODO
        $nbSciFiMoviesOrWithMorganFreeman = $this->movies->count();

        $this->assertEquals($nbSciFiMoviesOrWithMorganFreeman, 53);
    }

    /**
     * Ce test vérifie que nous avons 335 films dont le champ also_known_as existe
     */
    public function testAllMoviesWithFieldAlsoKnownAs(){

        // TODO
        $nbMoviesWithAnAlias = $this->movies->count();

        $this->assertEquals($nbMoviesWithAnAlias, 335);
    }

    /**
     * Ce test vérifie que nous avons 21 films tournés à New York
     */
    public function testMoviesLocationMatchingNewYork(){

        // TODO
        $nbMoviesFilmedInNewYork = $this->movies->count();

        $this->assertEquals($nbMoviesFilmedInNewYork, 21);
    }

}
?>