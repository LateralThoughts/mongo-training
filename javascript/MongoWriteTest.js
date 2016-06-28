
function setup() {
    // TODO
}

function teardown() {
	// TODO
}

var tests = {



    /**
    This test check the collection is empty. 
    */

    testThatDatabaseHas0Cds : function () {
        assert.eq(db.cds.find().count(), 0)        
    }
    ,


    /**
    First insert
    */

    testInsertWorks : function() {
        cd = {"name" : "cd1"}

        // TODO

        assert.eq(db.cds.find().count(), 1)                
    }
    ,
    /**
    Batch insert
    */

    testBatchInsert : function () {
        cd1 = {"name" : "cd1"}
        cd2 = {"name" : "cd2"}

        // TODO

        assert.eq(db.cds.find().count(), 2)   
    }
    ,
    /**
    This test check we can update the CD's name
    */

    testUpdateName : function () {

        tests.testInsertWorks();

        // TODO

        assert.eq(db.cds.find({"name" : "cd1"}).count(), 0)
        assert.eq(db.cds.find({"name" : "new name"}).count(), 1)
    }
    ,
    /**
    Test with multiple partial updates.
    We increment the counter nbArtiste and we add an object artists : {name : "Kurt Cobain"}
    */

    testUpdateAndIncr : function () {

        tests.testInsertWorks();

        // TODO

        assert.eq(db.cds.find({"name" : "cd1", "artists.name" : "Kurt Cobain", "nbArtists" : 1}).count(), 1)
    }
    ,
    /**
    Test for multiple updates
    */

    testUpdateMulti: function () {

        tests.testBatchInsert();

        // TODO

        assert.eq(db.cds.find({"rating" : 0}).count(), 2)
    }
    ,
    /**
    Add tags but without duplicates
    */

    testAddTag: function () {

        tests.testInsertWorks();

        var tagsToAdd = ['grunge', 'funk', 'soul', 'grunge']

        // TODO

        var cd = db.cds.findOne()
        assert.eq(Object.keys(cd['tags'].length), 3)
    }
    ,
    /**
    Remove the specified tags
    */

    testRemoveTag : function () {
        
        tests.testAddTag();

        var tagsToRemove = ['grunge', 'funk']

        // TODO

        var cd = db.cds.findOne()
        assert.eq(Object.keys(cd['tags'].length), 1)
    }
    ,

    /**
    In this test, we update a document to add 4 new ratings
    On those 4 new ratings, we only keep 3 of them, the most recent
    */

    testAddSortedRatingAndLimitBy3 : function () {

        tests.testInsertWorks();

        ratings = [
                        {"rating" : 1, "date" : new Date(2010, 01, 15, 00, 00)},
                        {"rating" : 4, "date" : new Date(2011, 01, 15, 00, 00)},
                        {"rating" : 2, "date" : new Date(2009, 01, 15, 00, 00)},
                        {"rating" : 5, "date" : new Date(2013, 01, 15, 00, 00)}
                    ]

        // TODO


        cd = db.cds.findOne()
        assert.eq(Object.keys(cd['ratings']).length, 3)   
        assert.eq(cd['ratings'][2]['rating'], 5)  
        assert.eq(cd['ratings'][0]['rating'], 1)       
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


