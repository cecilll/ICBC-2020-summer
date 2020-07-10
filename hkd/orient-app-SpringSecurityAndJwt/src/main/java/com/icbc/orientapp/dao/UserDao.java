package com.icbc.orientapp.dao;


import com.icbc.orientapp.entity.User;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserDao {

	void save(User user);

	User findByUsername(String name);
	
}
