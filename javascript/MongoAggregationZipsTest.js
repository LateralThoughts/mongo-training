
function setup() {
}

function teardown() {
}

var tests = {

    /**
    this test only checks we have 29467 zipcodes in our database
    */
    testThatDatabaseHasZipcodes: function() {
        assert.eq(db.zips.find().count(), 29467)
    },
    /**
    Find the city with one of its zipcode has the largest popuplation
    Only use skip limit and sort

    Note : It is of course possible to find the result without the aggregation framework, 
    but this is not the exercise
    */
    testFindLargestZipCodeAmongstCity: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['city'], 'CHICAGO')
    },

    /**
    Same question, but this time, the field _id should be rewritten as follows : 
    par exemple : chicago IL - zipcode
    Must read documentation: 
    - concat : http://docs.mongodb.org/manual/reference/operator/aggregation/concat/
    - toLower : http://docs.mongodb.org/manual/reference/operator/aggregation/toLower/
    */
    testFindLargestCityWithNormalizedName: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'chicago IL - 60623')
    },

    /**
    Find the city where on its zipcode has the largest population in the state of New York (NY)
    */
    testFindLargestZipCodeAmongstCityOfNewYork: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['city'], 'BROOKLYN')
    },

    /**
    Find the state with the greatest number of zipcodes
    */
    testStateWithTheLargestNumberOfZipCodes: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'TX')
        assert.eq(result[0]['number_of_zipcode'], 1676)
    },

    /**
    Find the second state with the greatest number of zipcodes
    */
    testSecondStateWithTheLargestNumberOfZipCodes: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'NY')
        assert.eq(result[0]['number_of_zipcode'], 1596)
    },

    /**
    Find the state with the biggest population
    */
    testStateWithLargestPopulation: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'CA')
        assert.eq(result[0]['total_pop'], 29760021)
    },

    /**
    Find the biggest city in New York (without skip and limit but with $first or $last)
    Must read documentation:
    - $first http://docs.mongodb.org/manual/reference/operator/aggregation/first/
    - $last : http://docs.mongodb.org/manual/reference/operator/aggregation/last/
    */
    testLargestCityInNewYork: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['largest_city'], 'BROOKLYN')
        assert.eq(result[0]['largest_pop'], 2300504)
    },

    /**
    What is the average population in a city of New York (NY)
    */
    testAvgPopulationByCityInNewYork: function() {
        var pipeline = [];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(Math.round(result[0]['avg_city_pop']), 13122)
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
