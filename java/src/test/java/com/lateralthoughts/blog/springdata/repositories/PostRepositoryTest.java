package com.lateralthoughts.blog.springdata.repositories;

import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.assertj.core.groups.Tuple;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = MongoTestConfiguration.class)
/**
 * Objectif de ce test
 *
 * Modifier Post et PostRepository pour pouvoir utiliser Spring Data
 *
 * Utiliser votre Repository pour faire fonctionner vos tests
 *
 *
 */
public class PostRepositoryTest {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Autowired
    private PostRepository postRepository;

    @Before
    public void setup() {
        insertOnePost("authorName1", "body1", "post1", Arrays.asList("tag1"));
        insertOnePost("authorName2", "body2", "post2", Arrays.asList("tag2"));
    }

    private void insertOnePost(String author, String body, String permalink, List<String> tags) {
        final Post post = new Post(permalink);
        post.setAuthor(author);
        post.setBody(body);
        post.setTags(tags);
        mongoTemplate.save(post);
    }

    @Test
    public void should_update_body() {
        Post post = postRepository.findByPermalink("post1");

        post.setBody("body2");
        postRepository.save(post);

        Post postFromDb = postRepository.findByPermalink("post1");

        assertThat(postFromDb)
                .extracting("body").containsExactly("body2");

    }

    @Test
    public void should_find_all_documents() {

        List<Post> posts = postRepository.findAll();

        assertThat(posts).hasSize(2);
    }


    @Test
    public void should_find_by_author() {

        List<Post> posts = postRepository.findByAuthor("authorName1");

        assertThat(posts)
                .hasSize(1)
                .extracting("author").containsExactly("authorName1");

    }

    @Test
    public void should_find_by_permalink() {

        Post post = postRepository.findByPermalink("post1");

        assertThat(post.getAuthor()).isEqualTo("authorName1");
        assertThat(post.getBody()).isEqualTo("body1");
    }

    @Test
    public void should_find_by_tag() {

        List<Post> posts = postRepository.findByTags("tag1");

        assertThat(posts)
                .hasSize(1)
                .extracting("tags").contains(Arrays.asList("tag1"));

    }

    @Test
    public void should_add_comment() {

        postRepository.addComment("post1", new Comment("authorName1", "bodyComment"));

        List<Post> posts = postRepository.findAll() ;

        assertThat(posts).hasSize(2);

        Post postFromDb = postRepository.findByPermalink("post1");

        assertThat(postFromDb)
                .extracting("numComments").containsExactly(1);

        assertThat(postFromDb.getComments())
                .hasSize(1)
                .extracting("author", "body").containsExactly(Tuple.tuple("authorName1", "bodyComment"));

    }
}