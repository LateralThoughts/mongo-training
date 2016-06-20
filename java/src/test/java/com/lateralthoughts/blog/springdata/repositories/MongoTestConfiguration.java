package com.lateralthoughts.blog.springdata.repositories;

import com.github.fakemongo.Fongo;
import com.mongodb.Mongo;
import com.mongodb.client.MongoDatabase;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.config.AbstractMongoConfiguration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@Configuration
@EnableMongoRepositories
@ComponentScan(basePackages = {"com.lateralthoughts.blog.springdata.repositories"})
public class MongoTestConfiguration extends AbstractMongoConfiguration {

    @Override
    protected String getDatabaseName() {
        return "fakedb";
    }

    @Override
    @Bean
    public Mongo mongo() {
        return new Fongo("fakedb").getMongo();
    }

    @Override
    protected String getMappingBasePackage() {
        return "com.lateralthoughts.blog";
    }
}
