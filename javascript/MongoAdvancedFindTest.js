
var tests = [

    /**
    This test should verify we have 280 grades movies in our database
    There is nothing to do here
    */
    function testThatDatabaseHas280Grades() {
        assert.eq(db.grades.count(), 280)
    }
    ,

    /** 
    77 documents should have exactly 3 grades 
    */
    function testThatWeHave77LinesWith3Grades() {
        query={}
        assert.eq(db.grades.find(query).count(), 77)
    }
    ,

    /** 
    This test check that all grades has an exam
    */
    function testNumberOfGradesWithExam() {
        query={}
        assert.eq(db.grades.find(query).count(), 280)
    }
    ,

    /** 
    Verify that there is 117 grades having an exam whose score is > 60
    */
    function testNumberOfGradesWithExamGreaterThan60() {
        query={}
        assert.eq(db.grades.find(query).count(), 117)
    }
    ,

    /** 
    This test use a projection to retrieve only one score for a grade.
    The array "scores" should have only one element
    */
    function testWeCanRetrieveOnlyOneScorePerGrade() {
        query={}
        projection = {}
        grade = db.grades.findOne(query, projection)
        assert.contains( 'scores' , grade)
        assert.eq(Object.keys(grade['scores']).length, 1)
    }
   
]

for (var i=0 ; i < tests.length ; i++) {
	tests[i]();
}


