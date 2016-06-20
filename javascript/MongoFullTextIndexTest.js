
function setup() {
    db.searchEvents.ensureIndex({"params.queryText" : "text"})
}

function teardown() {
    // TODO
}

var tests = {

    testNumberOccurenceJavaInSearch : function() {
        var query = {"params.queryText" : "Java"}
        var result = db.searchEvents.count(query)
        assert.eq(result, 643);
    },

    testNumberOccurenceJavaInSearchUsingFullTextQuery : function() {
        var query = {"$text" : {$search : "Java"}}
        var result = db.searchEvents.count(query)
        assert.eq(result, 14978);
    },

    testSortByRelevance : function() {
        var query = {"$text" : {$search : "Java"}}
        var projection= {score: { $meta: "textScore" }}
        var sort = {score: { $meta: "textScore" } }
        var result = db.searchEvents.find(query, projection ).sort(sort).limit(1)
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

