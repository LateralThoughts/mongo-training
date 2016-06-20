package com.lateralthoughts.blog.jongo.repositories;

import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.jongo.Jongo;
import org.jongo.MongoCollection;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.util.List;

@Service
public class JongoPostRepository {

    private Jongo jongo;
    private MongoCollection posts;

    @Autowired
    public JongoPostRepository(Jongo jongo) {
        this.jongo = jongo;
    }

    @PostConstruct
    public void afterPropertiesSet() {
        posts = jongo.getCollection("posts");
    }

    public void save(Post post) {
        posts.save(post);
    }

    public Post findByPermalink(String permalink) {
        return posts.findOne("{_id : #}", permalink).as(Post.class);
    }

    public Iterable<Post> findAll() {
        return posts.find().as(Post.class);

    }

    public Iterable<Post> findByAuthor(String author) {
        return posts.find("{author : #}", author).as(Post.class);

    }

    public Iterable<Post> findByTags(String tag) {
        return posts.find("{tags : #}", tag).as(Post.class);
    }

    public void addComment(String permalink, Comment comment) {
        posts.update("{_id : #}", permalink).with("{$inc : {numComments:1} , $push : {comments : #}}" , comment);
    }
}
