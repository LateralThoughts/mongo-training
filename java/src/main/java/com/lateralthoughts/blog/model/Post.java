package com.lateralthoughts.blog.model;

import lombok.Data;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Data
public class Post {

    private String title = "";
    private String body = "";
    private String permalink = "";
    private String author = "";
    private List<String> tags = new ArrayList<>();
    private List<Comment> comments = new ArrayList<>();
    private Date date = new Date();
    private int numComments;
}
