
var tests = [

	/**
 	This test should verify we have 350 movies in our database
    There is nothing to do here
    */
	function testThatDatabaseHas350Movies() {
	    assert.eq(db.movies.find().count(), 350);
	}
	,
    /**  
    This test should verify we have 69 films of 'Crime'
    */
    function testThatMovieWithGenreCrimeAre69() {
    	var query = {};
        assert.eq(db.movies.find(query).count(), 69)
    }
    ,

    /**  
    In this test, you should use projection to retrieve only the 'title' and the 'id' of one document
    We will use findOne and we check that the number of properties of the document is equals to two:
    'title' and '_id'
    */
    function testProjectionOnTitle() {
    	var query = {}
        projection = {}
        var movie = db.movies.findOne(query, projection)
        assert.contains( 'title', movie);
        assert.eq(Object.keys(movie).length, 2);
    }
    ,

    /** 
    This test should check that we have 224 movies with a rating between 8 and 9 (excluded)
    */
    function testRatingBetween8And9() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 224)
    }
    ,
    /** This test verify we have 24 movies with genres 'Comedy' and 'Romance' (simultaneously) */
    function testAllMovieComedyAndRomance() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 24)
    }
    ,
    /** Verify we have 243 movies that are not 'Comedy' or 'Romance' */
    function testAllMovieNotComedyAndRomance() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 243)
    }
    ,
     /** Verify we have 53 movies of science fiction or with Morgan Freeman
     Hint: use a db.movies.distinct to retrieve all different values for a field
      */
    function testAllMovieScienceFictionOrWithMorganFreeman() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 53)
    }
    ,
     /** Verify we have 335 movies with the field also_known_as  */
    function testAllMoviesWithFieldAlsoKnownAs() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 335)
    }
    ,
     /** Verify we have 21 movies made in New York */
    function testMoviesLocationMatchingNewYork() {
    	var query = {}
        assert.eq(db.movies.find(query).count(), 21)
    }
    
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


