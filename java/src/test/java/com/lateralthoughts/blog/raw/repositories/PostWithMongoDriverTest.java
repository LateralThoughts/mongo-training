package com.lateralthoughts.blog.raw.repositories;

import com.lateralthoughts.blog.model.Post;
import com.lateralthoughts.blog.springdata.repositories.MongoTestConfiguration;
import com.mongodb.BasicDBObject;
import com.mongodb.Mongo;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.List;

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

    private Mongo mongo;

    @Before
    public void setup() {

        initMongo();

        insertOnePost("authorName1", "body1");
        insertOnePost("authorName2", "body2");
    }

    private void initMongo() {
        // TODO
    }

    private void insertOnePost(String author, String body) {

        // TODO

    }

    @Test
    public void should_find_all_documents() {

        List<Post> posts = null;

        // TODO

        assertThat(posts).hasSize(2);
    }


    @Test
    public void should_find_by_author() {

        List<Post> posts = null;

        // TODO

        assertThat(posts)
                .hasSize(1)
                .extracting("author").containsExactly("authorName1");

    }
}