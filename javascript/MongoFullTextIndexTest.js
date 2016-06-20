
function setup() {
    // TODO
}

function teardown() {
    // TODO
}

var tests = {

    /**
    Find how many times "Java" is present in queryText using standard search
    */
    testNumberOccurenceJavaInSearch : function() {
        var query = {}
        var result = db.searchEvents.count(query)
        assert.eq(result, 643);
    },

    /**
    Find how many times "Java" is present in queryText using full text search
    */
    testNumberOccurenceJavaInSearchUsingFullTextQuery : function() {
        var query = {}
        var result = db.searchEvents.count(query)
        assert.eq(result, 14978);
    },

    /**
    Retrieve all search of "Java" by relevance and verify the first result has the highest score
    */
    testSortByRelevance : function() {
        var query = {}
        var sort = {}
        var projection={}
        var result = []
        assert(result.count(), 1);
        var search = result.next();
        assert.eq(search["params"]["queryText"], "Java/Java EE");
        assert.eq(search["score"], 1.250000);
    },



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

