
function setup() {
    // TODO
}

function teardown() {
    // TODO
}

var tests = {


    testFindSlowestQuery : function() {
        var query = {op : "query"}
        var sort = {millis : -1}
        var result = db.sysprofile.find(query).sort(sort).limit(1)
        assert.eq(result.count(), 317);
        var stat = result.next();
        assert.eq(stat["millis"], 15820);
        assert.eq(stat["op"], "query");
        assert.eq(stat["query"], {"student_id" : 80});
    },

    testFindAmountOfSlowQueries : function() {
        var query = {millis : {$gt : 100 }}
        var result = db.sysprofile.count(query)
        assert.eq(result, 100);
    },

    testFindSlowestCommand : function() {
        var query = {op : "command"}
        var sort = {millis : -1}
        var result = db.sysprofile.find(query).sort(sort).limit(1)
        assert.eq(result.count(), 4);
        var stat = result.next();
        assert.eq(stat["millis"], 47);
        assert.eq(stat["op"], "command");
        assert.eq(stat["command"], {"drop" : "gpa"});
    },

    testFindAllCollectionsInvolved : function() {
        var result = db.sysprofile.distinct("ns")
        assert.eq(result.length, 7);
        assert.eq(result.indexOf("school2.students") != -1, true);
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

