package com.lateralthoughts.blog.model;

import lombok.Data;
import org.bson.types.ObjectId;
import org.jongo.marshall.jackson.oid.MongoId;
import org.mongodb.morphia.annotations.Embedded;
import org.mongodb.morphia.annotations.Entity;
import org.mongodb.morphia.annotations.Reference;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Data
@Entity("posts")
@Document(collection="posts")
public class Post {

    private String title = "";
    private String body = "";
    @MongoId
    @Id
    @org.mongodb.morphia.annotations.Id
    private String permalink = "";
    private String author = "";
    private List<String> tags = new ArrayList<>();
    @Embedded
    private List<Comment> comments = new ArrayList<>();
    private Date date = new Date();
    private int numComments;

    public Post () {
        this (new ObjectId().toString());
    }

    public Post(String permalink) {
        date = new Date();
        this.permalink = permalink;
    }
}
