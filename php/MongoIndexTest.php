<?php
require_once ('PHPUnit/Framework/Assert.php');
require_once ('PHPUnit/Framework/TestCase.php');

/**
 * Class MongoIndexTest
 * Interdit de décoder le code !!
 * Sinon l'exercice n'a plus de sens ;)
 */
class MongoIndexTest extends PHPUnit_Framework_TestCase {

    private $mongoclient;

    public function setUp(){
      $this->mongoclient = new MongoClient();
    }

    public function tearDown(){
        $this->mongoclient->close();
    }

    /**
     *
     */
    public function testThatIndexesAreOk(){
        eval(base64_decode("ICAgICAgICBkYXRlX2RlZmF1bHRfdGltZXpvbmVfc2V0KCdVVEMnKTsNCiAgICAgICAgJG1lc3NhZ2VzID0gJHRoaXMtPm1vbmdvY2xpZW50LT5lbnJvbi0+bWVzc2FnZXM7DQoNCg0KICAgICAgICAkY3Vyc29yID0gJG1lc3NhZ2VzLT5maW5kKGFycmF5KCdib2R5JyA9PiBuZXcgTW9uZ29SZWdleCgiL1JPT00vaSIpKSk7DQogICAgICAgIGZvcmVhY2ggKCRjdXJzb3IgYXMgJG1lc3NhZ2UpIHsNCiAgICAgICAgICAgIC8vIGRvIG5vdGhpbmcNCiAgICAgICAgfQ0KICAgICAgICAkY3Vyc29yID0gJG1lc3NhZ2VzLT5maW5kKGFycmF5KCdoZWFkZXJzLlgtRnJvbScgPT4gIlJlc2VydmF0aW9uc0BNYXJyaW90dC5jb20iLCAiaGVhZGVycy5YLVRvIiA9PiAiRUJBU1NARU5ST04uQ09NIikpOw0KICAgICAgICBmb3JlYWNoICgkY3Vyc29yIGFzICRtZXNzYWdlKSB7DQogICAgICAgICAgICAvLyBkbyBub3RoaW5nDQogICAgICAgIH0NCiAgICAgICAgJGN1cnNvciA9ICRtZXNzYWdlcy0+ZmluZChhcnJheSgnbWFpbGJveCcgPT4gInNlbnQiLCAiaGVhZGVycy5YLWNjIiA9PiAiIikpLT5zb3J0KGFycmF5KCdoZWFkZXJzLkZyb20nPT4xKSk7DQogICAgICAgIGZvcmVhY2ggKCRjdXJzb3IgYXMgJG1lc3NhZ2UpIHsNCiAgICAgICAgICAgIC8vIGRvIG5vdGhpbmcNCiAgICAgICAgfQ0KICAgICAgICAkY3Vyc29yID0gJG1lc3NhZ2VzLT5maW5kKGFycmF5KCdoZWFkZXJzLkZyb20nID0+ICJlcmljLmJhc3NAZW5yb24uY29tIikpLT5zb3J0KGFycmF5KCdoZWFkZXJzLkRhdGUnPT4tMSkpOw0KICAgICAgICBmb3JlYWNoICgkY3Vyc29yIGFzICRtZXNzYWdlKSB7DQogICAgICAgICAgICAvLyBkbyBub3RoaW5nDQogICAgICAgIH0="));
    }


}
?>