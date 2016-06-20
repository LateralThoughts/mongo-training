package com.lateralthoughts.blog.web;

import com.lateralthoughts.blog.model.ResourceNotFoundException;
import com.lateralthoughts.blog.model.Comment;
import com.lateralthoughts.blog.model.Post;
import com.lateralthoughts.blog.springdata.repositories.PostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class BlogController {

    @Autowired
    private PostRepository postRepository;

    @RequestMapping("/")
    public String index(ModelMap model) {

        model.addAttribute("posts", postRepository.findAll(new PageRequest(0, 10, new Sort(Sort.Direction.DESC, "date"))));

        return "index";
    }

    @RequestMapping("/post/{permalink}")
    public String displayPost(@PathVariable String permalink, ModelMap model) {

        Post post = postRepository.findByPermalink(permalink);
        if (post == null) {
            throw new ResourceNotFoundException();
        }

        model.addAttribute("post", post);
        model.addAttribute("comment", new Comment());

        return "post";
    }


    @RequestMapping(value = "/post/{permalink}/comment", method = RequestMethod.POST)
    public String addComment(@PathVariable String permalink, @ModelAttribute Comment comment) {

        postRepository.addComment(permalink, comment);

        return "redirect:/post/"+permalink;
    }

    @RequestMapping("/post")
    public String addPostForm() {


        return "addPost";
    }

    @RequestMapping("/tag/{tag}")
    public String displayPostByTags(@PathVariable String tag, ModelMap model) {

        model.addAttribute("posts", postRepository.findByTags(tag));
        return "index";
    }

    @RequestMapping(value = "/post", method = RequestMethod.POST)
    public String addPost(@ModelAttribute Post post) {

        postRepository.save(post);

        return "redirect:/";
    }

}
