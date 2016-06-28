
function setup() {
	db.cds.remove({});
}

function teardown() {
	db.cds.remove({});
}


var tests = {

    testThatDatabaseHas0Cds : function () {
        assert.eq(db.cds.find().count(), 0)        
    }
    ,

    testInsertWorks : function () {
        cd = {"name" : "cd1"}

        db.cds.insert(cd);

        assert.eq(db.cds.find().count(), 1)                
    }
    ,

    testBatchInsert : function () {
        cd1 = {"name" : "cd1"}
        cd2 = {"name" : "cd2"}

		db.cds.insertMany( [cd1, cd2] );

        assert.eq(db.cds.find().count(), 2)   
    }
    ,

    testUpdateName : function () {

        tests.testInsertWorks();

        db.cds.update({"name" : "cd1"}, {"$set" : {"name" : "new name"}})


        assert.eq(db.cds.find({"name" : "cd1"}).count(), 0)
        assert.eq(db.cds.find({"name" : "new name"}).count(), 1)
    }
    ,

    testUpdateAndIncr : function () {

        tests.testInsertWorks();

        db.cds.update({"name" : "cd1"}, 
                        {
                            "$push" : 
                            {
                                "artists" : {"name" : "Kurt Cobain"}
                            }, 
                            "$inc": {"nbArtists" : 1}
                        });

        assert.eq(db.cds.find({"name" : "cd1", "artists.name" : "Kurt Cobain", "nbArtists" : 1}).count(), 1)
    }
    ,


    testUpdateMulti: function () {

        tests.testBatchInsert();

        db.cds.update({}, {"$set" : {"rating" : 0}}, {'multi' : true})

        assert.eq(db.cds.find({"rating" : 0}).count(), 2)
    }
    ,


    testAddTag: function () {

        tests.testInsertWorks();

        var tagsToAdd = ['grunge', 'funk', 'soul', 'grunge']

        db.cds.update({}, {
                                "$addToSet" : 
                                {   
                                    "tags" : 
                                    {
                                        "$each" : tagsToAdd
                                    }
                                }
                            });

        var cd = db.cds.findOne();
        assert.eq(cd['tags'].length,  3);
    }
    ,


    testRemoveTag : function () {
        
        tests.testAddTag();

        var tagsToRemove = ['grunge', 'funk'];

        db.cds.update({}, {"$pullAll" : {"tags" : tagsToRemove}})

        var cd = db.cds.findOne();
        assert.eq(cd['tags'].length,  1);
    }
    ,


    testAddSortedRatingAndLimitBy3 : function () {

        tests.testInsertWorks();

        var ratings = [
                        {"rating" : 1, "date" : new Date(2010, 01, 15, 00, 00)},
                        {"rating" : 4, "date" : new Date(2011, 01, 15, 00, 00)},
                        {"rating" : 2, "date" : new Date(2009, 01, 15, 00, 00)},
                        {"rating" : 5, "date" : new Date(2013, 01, 15, 00, 00)}
                    ];

        db.cds.update({}, {"$push" : 
            {
                "ratings" : 
                {
                    "$each" :
                    ratings,
                    "$sort" : {"date" : 1}, 
                    "$slice" : -3
                }
            }});


        var cd = db.cds.findOne();
        assert.eq(Object.keys(cd['ratings']).length, 3)   ;
        assert.eq(cd['ratings'][2]['rating'], 5)  ;
        assert.eq(cd['ratings'][0]['rating'], 1);
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
