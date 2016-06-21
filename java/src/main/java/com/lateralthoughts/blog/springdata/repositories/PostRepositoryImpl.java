package com.lateralthoughts.blog.springdata.repositories;

import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;

import static org.springframework.data.mongodb.core.query.Criteria.where;

public class PostRepositoryImpl implements PostRepositoryCustom {

    @Autowired
    private MongoTemplate template;

    @Override
    public void addComment(String permalink, Comment comment) {

        Update update = new Update();
        update.inc("numComments", 1);
        update.push("comments", comment);

        template.updateFirst(new Query(where("_id").is(permalink)), update, Post.class);
    }
}
