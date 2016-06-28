
function setup() {
    // TODO
}

function teardown() {
    // TODO
}

var tests = {

    /**
    Find the slowest query
    */
    testFindSlowestQuery : function() {
        var query = {};
        var sort = {};
        var result = [];
        assert.eq(result.count(), 317);
        var stat = result.next();
        assert.eq(stat["millis"], 15820);
        assert.eq(stat["op"], "query");
        assert.eq(stat["query"], {"student_id" : 80});
    },

    /**
    Find how many query are slower than 100ms
    */
    testFindAmountOfSlowQueries : function() {
        var query = {};
        var result = db.sysprofile.count(query);
        assert.eq(result, 100);
    },

    /**
    Find the slowest command
    */
    testFindSlowestCommand : function() {
        var query = {};
        var sort = {};
        var result = [];
        assert.eq(result.count(), 4);
        var stat = result.next();
        assert.eq(stat["millis"], 47);
        assert.eq(stat["op"], "command");
        assert.eq(stat["command"], {"drop" : "gpa"});
    },

    /**
    Find all collections involved in this profiling session
    */
    testFindAllCollectionsInvolved : function() {
        var result = []; // replace by the full command
        assert.eq(result.length, 7);
        assert.eq(result.indexOf("school2.students") != -1, true);
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

