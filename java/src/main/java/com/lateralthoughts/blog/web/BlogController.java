package com.lateralthoughts.blog.web;

import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.Arrays;

@Controller
public class BlogController {

    @RequestMapping("/")
    public String index(ModelMap model) {

        model.addAttribute("posts", Arrays.asList(new Post()));


        return "index";
    }

    @RequestMapping("/post/{permalink}")
    public String displayPost(@PathVariable String permalink, ModelMap model) {

        model.addAttribute("post", new Post());
        model.addAttribute("comment", new Comment());

        return "post";
    }


    @RequestMapping(value = "/post/{permalink}/comment", method = RequestMethod.POST)
    public String addComment(@PathVariable String permalink, @ModelAttribute Comment comment) {


        return "redirect:/post/"+permalink;
    }

    @RequestMapping("/post")
    public String addPostForm() {


        return "addPost";
    }

    @RequestMapping("/tag/{tag}")
    public String displayPostByTags(@PathVariable String tag, ModelMap model) {

        model.addAttribute("posts", Arrays.asList(new Post()));
        return "index";
    }

    @RequestMapping(value = "/post", method = RequestMethod.POST)
    public String addPost(@ModelAttribute Post post) {


        return "redirect:/";
    }

}
