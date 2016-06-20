package com.lateralthoughts.blog.api;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.jayway.restassured.RestAssured;
import com.jayway.restassured.config.RedirectConfig;
import com.jayway.restassured.http.ContentType;
import com.lateralthoughts.blog.Application;
import com.lateralthoughts.blog.model.Post;
import com.lateralthoughts.blog.springdata.repositories.PostRepository;
import org.assertj.core.api.Assertions;
import org.jongo.Jongo;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.IntegrationTest;
import org.springframework.boot.test.SpringApplicationConfiguration;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;

import java.util.Arrays;

import static com.jayway.restassured.RestAssured.expect;
import static com.jayway.restassured.RestAssured.given;
import static org.assertj.core.api.Assertions.assertThat;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringApplicationConfiguration(classes = Application.class)
@WebAppConfiguration
@IntegrationTest("server.port:0")
@ActiveProfiles("test")
public class ApiTest {

    @Value("${local.server.port}")
    private int serverPort;

    @Autowired
    protected PostRepository postRepository;

    @Before
    public void setup() {
        RestAssured.port = serverPort;
        postRepository.deleteAll();
    }

    @Test
    public void should_add_post() {

        Post post = new Post("permalink");
        post.setAuthor("author");
        post.setBody("body");
        post.setTags(Arrays.asList("tag1", "tag2"));

        given().body(post).accept(ContentType.JSON)
                .contentType(ContentType.JSON)
                .expect().statusCode(201)
                .header("Location", RestAssured.baseURI + ":"+ serverPort + "/api/post/permalink")
                .when().post("/api/post");


        Post postFromDb = postRepository.findByPermalink("permalink");

        assertThat(postFromDb).isNotNull();
        assertThat(postFromDb.getAuthor()).isEqualTo("author");
        assertThat(postFromDb.getBody()).isEqualTo("body");
        assertThat(postFromDb.getTags()).isEqualTo(Arrays.asList("tag1", "tag2"));
    }

}
