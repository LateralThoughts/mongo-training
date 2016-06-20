package com.lateralthoughts.blog.model;

import lombok.Data;
import org.springframework.data.annotation.Id;

@Data
public class Comment {
    private String author = "";
    private String body = "";
}
