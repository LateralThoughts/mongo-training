package com.lateralthoughts.blog.jongo.repositories;

import com.lateralthoughts.blog.model.Post;
import org.assertj.core.groups.Tuple;
import org.jongo.Jongo;
import org.junit.Before;
import org.junit.Test;

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

    private Jongo jongo;
    private JongoPostRepository postRepository;

    @Before
    public void setup() {

        initJongoAndRepository();

        insertOnePost("authorName1", "body1", "post1", Arrays.asList("tag1"));
        insertOnePost("authorName2", "body2", "post2", Arrays.asList("tag2"));
    }

    private void insertOnePost(String author, String body, String permalink, List<String> tags) {

        // TODO

    }

    private void initJongoAndRepository() {

        // TODO

    }

    @Test
    public void should_update_body() {
        Post post = null;

        // TODO

        Post postFromDb = null;

        // TODO

        assertThat(postFromDb)
                .extracting("body").containsExactly("body2");

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

    @Test
    public void should_find_by_permalink() {

        Post post = null;

        // TODO

        assertThat(post.getAuthor()).isEqualTo("authorName1");
        assertThat(post.getBody()).isEqualTo("body1");
    }

    @Test
    public void should_find_by_tag() {

        List<Post> posts = null;

        // TODO

        assertThat(posts)
                .hasSize(1)
                .extracting("tags").contains(Arrays.asList("tag1"));

    }

    @Test
    public void should_add_comment() {

        // TODO

        List<Post> posts = null;

        // TODO

        assertThat(posts).hasSize(2);

        Post postFromDb = null;

        // TODO

        assertThat(postFromDb.getPermalink()).isEqualTo("post1");

        assertThat(postFromDb.getNumComments()).isEqualTo(1);

        assertThat(postFromDb.getComments())
                .hasSize(1)
                .extracting("author", "body").containsExactly(Tuple.tuple("authorName1", "bodyComment"));

    }
}