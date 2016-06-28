
var tests = [

    function testThatDatabaseHas280Grades() {
        assert.eq(db.grades.count(), 280)
    }
    ,

    function testThatWeHave77LinesWith3Grades() {
        query={"scores" : {"$size" : 3}}
        assert.eq(db.grades.find(query).count(), 77)
    }
    ,

    function testNumberOfGradesWithScoreLowerThan20() {
        query={"scores.score" : {$lt : 20}}
        assert.eq(db.grades.find(query).count(), 182)
    },

    function testNumberOfGradesWithExamGreaterThan60() {
        query={
           "scores":{
              "$elemMatch":{
                 "type":"exam",
                 "score":{
                    '$gt':60
                 }
              }
           }
        }
        assert.eq(db.grades.find(query).count(), 117)
    }
    ,

    function testWeCanRetrieveOnlyOneScorePerGrade() {
        query={}
        projection = {"scores" : {'$slice' : 1}}
        grade = db.grades.findOne(query, projection)
        assert( grade.hasOwnProperty('scores'))
        assert.eq(Object.keys(grade['scores']).length, 1)
    }
   
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


