package com.icbc.orient.service;

import com.icbc.orient.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.icbc.orient.dao.UserDao;

@Service
public class UserService {

    @Autowired
    private UserDao userDao;

    public void save(User user) {
        user.setId(1);
        userDao.save(user);
    }

}

