package com.lateralthoughts.blog.raw.repositories;

import com.github.fakemongo.Fongo;
import com.lateralthoughts.blog.model.Post;
import com.mongodb.*;
import com.lateralthoughts.blog.springdata.repositories.MongoTestConfiguration;
import com.mongodb.BasicDBObject;
import com.mongodb.Mongo;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.model.Filters;
import org.bson.Document;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.ArrayList;
import java.util.List;

import static com.mongodb.client.model.Filters.eq;
import static org.assertj.core.api.Assertions.assertThat;

/**
 * Objectif de ce test
 *
 * Utiliser l'api standard du driver Mongo pour initialiser votre jeu de données
 * et faire passer vos tests
 *
 * Au programme : utilisation de {@link BasicDBObject}, parcours de cursor
 *
 */
public class PostWithMongoDriverTest {

    private MongoClient mongo;
    private MongoCollection<Document> mongoPosts;

    @Before
    public void setup() {

        initMongo();

        insertOnePost("authorName1", "body1");
        insertOnePost("authorName2", "body2");
    }

    private void initMongo() {
        mongo = new Fongo("fakedb").getMongo();
        mongoPosts = mongo.getDatabase("fakedb").getCollection("posts");

        mongoPosts.deleteMany(new Document());
    }

    private void insertOnePost(String author, String body) {
        final Document post = new Document();
        post.append("author", author).append("body", body);
        mongoPosts.insertOne(post);
    }

    @Test
    public void should_find_all_documents() {

        List<Post> posts = new ArrayList<>();

        MongoCursor<Document> cursor = mongoPosts.find().iterator();
        while(cursor.hasNext()) {
            Document post = cursor.next();
            Post p = new Post();
            p.setAuthor((String) post.get("author"));
            p.setBody((String) post.get("body"));
            posts.add(p);
        }

        assertThat(posts).hasSize(2);
    }


    @Test
    public void should_find_by_author() {

        List<Post> posts = new ArrayList<>();

        MongoCursor<Document> cursor = mongoPosts.find(eq("author", "authorName1")).iterator();
        while(cursor.hasNext()) {
            Document post = cursor.next();
            Post p = new Post();
            p.setAuthor((String) post.get("author"));
            p.setBody((String) post.get("body"));
            posts.add(p);
        }

        assertThat(posts)
                .hasSize(1)
                .extracting("author").containsExactly("authorName1");

    }
}