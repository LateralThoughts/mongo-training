

ops = [{op: "findOne", ns: "enron.messages", query: {'headers.From': 'reservations@marriott.com'}},
       {op: "update", ns: "enron.messages", query: {'headers.From': 'reservations@marriott.com'}, update: {$inc: {x: 1}}},
	   {op: "findOne", ns: "enron.messages", query: {'x': {'$exists' : true}}}
	   ]


for ( var x = 1; x <= 128; x *= 2) {
    res = benchRun( {
        parallel : x ,
        seconds : 5 ,
        ops : ops
    } );
    print( "threads: " + x + "\t queries/sec: " + res.query );
}