
function setup() {
    // TODO
}

function teardown() {
    // TODO
}

var tests = {


    testAllMovieComedyAndRomance : function() {
        var genres = ["Comedy", "Romance"]
        var project  = { $project: { genreComedyOrRomance: { $setIsSubset: [ genres, "$genres" ] } }}
        var redact = {$redact : {$cond: {
                        if: { $eq: [ "$genreComedyOrRomance" , true ] },
                        then: "$$DESCEND",
                        else: "$$PRUNE"
                    }}}
        var group = {$group : {_id: null, number_of_movies : {$sum : 1 }}}
        var pipeline = [project, redact, group]
        assert.eq(db.movies.aggregate(pipeline).toArray()[0]['number_of_movies'], 24)
    }
    ,

    testAllMovieNotComedyAndRomance : function() {
        var genres = ["Comedy", "Romance"]
        var project  = { $project: { genreComedyOrRomance: { $setIntersection: [ genres, "$genres" ] } }}
        var nbOfIntersection = {$project : {genresInCommon: {$size: "$genreComedyOrRomance"}}}
        var redact = {$redact : {$cond: {
                        if: { $eq: [ "$genresInCommon" , 0 ] },
                        then: "$$DESCEND",
                        else: "$$PRUNE"
                    }}}
        var group = {$group : {_id: null, number_of_movies : {$sum : 1 }}}
        var pipeline = [project, nbOfIntersection, redact, group]
        assert.eq(db.movies.aggregate(pipeline).toArray()[0]['number_of_movies'], 243)
    }
    ,

    testFindActorWithLargestPorfolio : function() {
        var unwind = {'$unwind' : '$actors' }
        var group = {"$group" : {
                                '_id' : '$actors', 'number_of_movies' : {'$sum' : 1}
                            }
        }
        var sort = {"$sort" : {"number_of_movies" : -1}}
        var limit = {"$limit" : 1}
        var pipeline = [unwind, group, sort, limit];
        var result = db.movies.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'Robert De Niro')
        assert.eq(result[0]['number_of_movies'], 9)
    }
}

for (var test in tests) {
    print ("####################");
    print (test);
    print ("####################");
    setup();
    tests[test]();
    teardown();
    print("SUCCESS\n");
}

