
function setup() {
    // TODO
}

function teardown() {
    // TODO
}

var tests = {

    /** This test verify we have 24 movies with only genres 'Comedy' and 'Romance' (simultaneously) 
    you have to use set operators (http://docs.mongodb.org/manual/reference/operator/aggregation-set/) 
    and redact
    you should not use a $match 
    */
    testAllMovieComedyAndRomance : function() {
        var pipeline = []
        assert.eq(db.movies.aggregate(pipeline).toArray()[0]['number_of_movies'], 24)
    }
    ,
    /** This test verify we have 243 movies without genres 'Comedy' and 'Romance' (simultaneously) 
    you have to use set operators (http://docs.mongodb.org/manual/reference/operator/aggregation-set/) 
    and redact
    you should not use a $match 
    */
    testAllMovieNotComedyAndRomance : function () {
        var pipeline = []
        assert.eq(db.movies.aggregate(pipeline).toArray()[0]['number_of_movies'], 243)
    },

    /**
    Find the actor with the greatest number of films to his credit
    */
    testFindActorWithLargestPorfolio : function() {
        var pipeline = []
        var result = db.movies.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'Robert De Niro')
        assert.eq(result[0]['number_of_movies'], 9)
    }
};

for (var test in tests) {
    print ("####################");
    print (test);
    print ("####################");
    setup();
    tests[test]();
    teardown();
    print("SUCCESS\n");
}

