package com.icbc.orientapp.service;


import com.icbc.orientapp.dao.UserDao;
import com.icbc.orientapp.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
	
	@Autowired
	private UserDao userDao;

	public void save(User user) {
		user.setId(1);
		userDao.save(user);
	}
	
}
