package com.icbc.orient.dao;

import org.apache.ibatis.annotations.Mapper;

import com.icbc.orient.entity.User;

@Mapper
public interface UserDao {

    void save(User user);

    User findByUsername(String name);

}
