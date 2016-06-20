package com.lateralthoughts.blog.model;

import lombok.Data;

@Data
public class Comment {
    private String author = "";
    private String body = "";

    public Comment() {
    }

    public Comment(String author, String body) {
        this.author = author;
        this.body = body;
    }
}
