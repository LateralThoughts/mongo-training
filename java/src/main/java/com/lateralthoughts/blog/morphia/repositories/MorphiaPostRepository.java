package com.lateralthoughts.blog.morphia.repositories;

import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.mongodb.morphia.Datastore;
import org.mongodb.morphia.query.UpdateOperations;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class MorphiaPostRepository {

    private Datastore datastore;

    @Autowired
    public MorphiaPostRepository(Datastore datastore) {
        this.datastore = datastore;
    }

    public void save(Post post) {
        datastore.save(post);
    }

    public Post findByPermalink(String permalink) {
        return datastore.createQuery(Post.class).filter("_id =", permalink).get();
    }

    public Iterable<Post> findAll() {
        return datastore.find(Post.class);

    }

    public Iterable<Post> findByAuthor(String author) {
        return datastore.createQuery(Post.class).filter("author =", author);

    }

    public Iterable<Post> findByTags(String tag) {
        return datastore.createQuery(Post.class).filter("tags =", tag);
    }

    public void addComment(String permalink, Comment comment) {
        UpdateOperations<Post> update = datastore.createUpdateOperations(Post.class).inc("numComments", 1).add("comments", comment);
        datastore.update(datastore.createQuery(Post.class).filter("_id =", permalink),update);
    }
}
