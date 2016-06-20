package com.lateralthoughts.blog.raw.repositories;

import com.github.fakemongo.Fongo;
import com.lateralthoughts.blog.model.Post;
import com.lateralthoughts.blog.springdata.repositories.MongoTestConfiguration;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

/**
 *
 * Objectif de ce test
 *
 * Utiliser l'api spring pour initialiser votre jeu de données
 * et faire passer vos tests
 *
 * Au programme : utilisation de {@link MongoTemplate}, parcours de cursor
 * Pensez à l'annotation {@link org.springframework.data.mongodb.core.mapping.Document}
 *
 *
 */
public class PostWithMongoTemplateTest {

    private MongoTemplate mongoTemplate;

    @Before
    public void setup() {

        initMongo();

        insertOnePost("authorName1", "body1");
        insertOnePost("authorName2", "body2");
    }

    private void initMongo() {
        mongoTemplate = new MongoTemplate(new Fongo("fakedb").getMongo(), "fakedb");
        mongoTemplate.dropCollection(Post.class);
    }

    private void insertOnePost(String author, String body) {
        final Post post = new Post();
        post.setAuthor(author);
        post.setBody(body);
        mongoTemplate.save(post);
    }

    @Test
    public void should_find_all_documents() {

        List<Post> posts = mongoTemplate.findAll(Post.class);

        assertThat(posts).hasSize(2);
    }


    @Test
    public void should_find_by_author() {

        List<Post> posts = mongoTemplate.find(new Query(Criteria.where("author").is("authorName1")), Post.class);

        assertThat(posts)
                .hasSize(1)
                .extracting("author").containsExactly("authorName1");

    }
}