
var tests = [

    /**
    This test check that the 10th Sci-fi movie is 'Space mutiny' when we sort by ascending ratings
    */
    function testThatThe10thScifiMovieOrderedByRatingIsTheExpectedOne() {
        query = {};
        cursor = [];
        assert(cursor.count(), 1);
        var movie = cursor.next();
        assert.eq(movie["title"], 'Space Mutiny');

     }
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


