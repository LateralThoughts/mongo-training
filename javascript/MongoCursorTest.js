
var tests = [


    function testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne() {
        query = {"genres" : "Sci-Fi"};
        cursor = db.movies.find(query).skip(9).limit(1).sort({"rating":1});
        assert(cursor.count(), 1);
        var movie = cursor.next();
        assert.eq(movie["title"], 'Space Mutiny');

     }
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


