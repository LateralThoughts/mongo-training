var tests = [

	function testThatDatabaseHas350Movies() {
	    assert.eq(db.movies.find().count(), 350);
	}
	,
    function testThatMovieWithGenreCrimeAre69() {
        assert.eq(db.movies.find({"genres" : 'Crime'}).count(), 69)
    }
    ,

    function testProjectionOnTitle() {
        var movie = db.movies.findOne({}, {"title": 1})
        assert.contains( 'title', movie);
        assert.eq(Object.keys(movie).length, 2);
    }
    ,

    function testRatingBetween7And8() {
        assert.eq(db.movies.find(
            {
           "rating":{ "$gt": 8, "$lt": 9 }
           }).count(), 224)
    }
    ,
    function testAllMovieComedyAndRomance() {
        assert.eq(db.movies.find({"genres" : {'$all' : ['Comedy', 'Romance']}}).count(), 24)
    }
    ,
    function testAllMovieNotComedyAndRomance() {
        assert.eq(db.movies.find({"genres" : {"$nin" : ['Comedy', 'Romance']}}).count(), 243)
    }
    ,
    function testAllMovieScienceFictionOrWithMorganFreeman() {
        assert.eq(db.movies.find({"$or" : [{"genres" : "Sci-Fi"}, {'actors' : 'Morgan Freeman'}]}).count(), 53)
    }
    ,
    function testAllMoviesWithFieldAlsoKnownAs() {
        assert.eq(db.movies.find({"also_known_as" : {"$exists" : 1}}).count(), 335)
    }
    ,
    function testMoviesLocationMatchingNewYork() {
        assert.eq(db.movies.find({"filming_locations" : {"$regex" : 'new york', '$options': 'i'}}).count(), 21)
    }
    
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


