package com.lateralthoughts.blog.jongo.repositories;

import com.github.fakemongo.Fongo;
import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.assertj.core.groups.Tuple;
import org.jongo.Jongo;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * Objectif de ce test
 *
 * Utiliser jongo pour initialiser votre jeu de données
 *
 * Modifier Post et PostRepository (dans le package jongo) pour pouvoir utiliser Jongo
 *
 * Utiliser votre Repository pour faire fonctionner vos tests
 *
 *
 */
public class JongoPostRepositoryTest {

    private JongoPostRepository postRepository;

    @Before
    public void setup() {

        initJongoAndRepository();

        insertOnePost("authorName1", "body1", "post1", Arrays.asList("tag1"));
        insertOnePost("authorName2", "body2", "post2", Arrays.asList("tag2"));
    }

    private void initJongoAndRepository() {
        final Jongo fakeJongo = new Jongo(new Fongo("fake_db").getDB("fake_db"));
        postRepository = new JongoPostRepository(fakeJongo);
        postRepository.afterPropertiesSet();
    }

    private void insertOnePost(String author, String body, String permalink, List<String> tags) {
        final Post post = new Post(permalink);
        post.setAuthor(author);
        post.setBody(body);
        post.setTags(tags);
        postRepository.save(post);
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

        List<Post> posts = new ArrayList<>();
        postRepository.findAll().forEach(posts::add);

        assertThat(posts).hasSize(2);
    }


    @Test
    public void should_find_by_author() {

        List<Post> posts = new ArrayList<>();
        postRepository.findByAuthor("authorName1").forEach(posts::add);

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

        List<Post> posts = new ArrayList<>();
        postRepository.findByTags("tag1").forEach(posts::add);

        assertThat(posts)
                .hasSize(1)
                .extracting("tags").contains(Arrays.asList("tag1"));

    }

    @Test
    public void should_add_comment() {

        postRepository.addComment("post1", new Comment("authorName1", "bodyComment"));

        List<Post> posts = new ArrayList<>();
        postRepository.findAll().forEach(posts::add);

        assertThat(posts).hasSize(2);

        Post postFromDb = postRepository.findByPermalink("post1");

        assertThat(postFromDb)
                .extracting("numComments").containsExactly(1);

        assertThat(postFromDb.getComments())
                .hasSize(1)
                .extracting("author", "body").containsExactly(Tuple.tuple("authorName1", "bodyComment"));

    }
}