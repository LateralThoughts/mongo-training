
function setup() {
}

function teardown() {
}

var tests = {


    testThatDatabaseHasZipcodes: function() {
        assert.eq(db.zips.find().count(), 29467)
    },

    testFindLargestZipCodeAmongstCity: function() {
        var sort = {"$sort" : {"pop" : -1}}
        var limit = {"$limit" : 1}
        var pipeline = [sort, limit];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['city'], 'CHICAGO')
    },


    testFindLargestCityWithNormalizedName: function() {
        var sort = {"$sort" : {"pop" : -1}}
        var limit = {"$limit" : 1}
        var project = {"$project" : {
                                   "_id" : {
                                        "$concat" : [{"$toLower" : "$city"}, ' ', '$state', ' - ', '$_id'] 
                                   }, 
                                   "pop" : 1
                               }
                  }
        var pipeline = [sort, limit, project];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'chicago IL - 60623')
    },


    testFindLargestZipCodeAmongstCityOfNewYork: function() {
        var sort = {"$sort" : {"pop" : -1}}
        var limit = {"$limit" : 1}
        var match = {"$match" : { "state" : 'NY' }}
        var pipeline = [match, sort, limit];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['city'], 'BROOKLYN')
    },


    testStateWithTheLargestNumberOfZipCodes: function() {
        var group = {"$group" : {'_id' : '$state', 'number_of_zipcode' : {'$sum' : 1}}}
        var sort = {"$sort" : {"number_of_zipcode" : -1}}
        var limit = {"$limit" : 1}        
        var pipeline = [group, sort, limit];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'TX')
        assert.eq(result[0]['number_of_zipcode'], 1676)
    },


    testSecondStateWithTheLargestNumberOfZipCodes: function() {
        var group = {"$group" : {'_id' : '$state', 'number_of_zipcode' : {'$sum' : 1}}}
        var sort = {"$sort" : {"number_of_zipcode" : -1}}
        var skip = {'$skip' : 1};
        var limit = {"$limit" : 1}        
        var pipeline = [group, sort, skip, limit];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'NY')
        assert.eq(result[0]['number_of_zipcode'], 1596)
    },


    testStateWithLargestPopulation: function() {
        var group = {"$group" : {'_id' : '$state', 'total_pop' : {'$sum' : "$pop"}}}
        var sort = {"$sort" : {"total_pop" : -1}}
        var limit = {"$limit" : 1}        
        var pipeline = [group, sort, limit];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['_id'], 'CA')
        assert.eq(result[0]['total_pop'], 29760021)
    },


    testLargestCityInNewYork: function() {
        var match = {"$match" : { "state" : 'NY' }}
        var groupByCity = {"$group" : {'_id' : {"state" : '$state', "city" : "$city"}, 'pop_by_city' : {'$sum' : "$pop"}}}
        var sort = {"$sort" : {"pop_by_city" : -1}}
        var findLargest = {"$group" : {'_id' : "$_id.state", 'largest_city' : {'$first' : "$_id.city"}, 'largest_pop' : {'$first' : "$pop_by_city"}}}

        var pipeline = [match, groupByCity, sort, findLargest];
        var result =db.zips.aggregate(pipeline).toArray()
        assert.eq(result[0]['largest_city'], 'BROOKLYN')
        assert.eq(result[0]['largest_pop'], 2300504)
    },


    testAvgPopulationByCityInNewYork: function() {
        var match = {"$match" : { "state" : 'NY' }}
        var groupByCityAndState = {"$group" : {'_id' : {"state" : '$state', "city" : "$city"}, 'pop_by_city' : {'$sum' : "$pop"}}}
        var findAverage = {"$group" : {'_id' : "$_id.state", 'avg_city_pop' : {'$avg' : "$pop_by_city"}}}
        
        var pipeline = [match, groupByCityAndState, findAverage];
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
