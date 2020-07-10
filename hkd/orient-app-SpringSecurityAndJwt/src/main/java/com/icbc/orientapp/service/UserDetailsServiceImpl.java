package com.icbc.orientapp.service;


import com.icbc.orientapp.dao.UserDao;
import com.icbc.orientapp.entity.JwtUser;
import com.icbc.orientapp.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

/**
 * Created by echisan on 2018/6/23
 */
@Service
public class UserDetailsServiceImpl implements UserDetailsService {

	@Autowired
	private UserDao dao;
	
    @Override
    public UserDetails loadUserByUsername(String s) throws UsernameNotFoundException {
    	
        User user = dao.findByUsername(s);
        
        return new JwtUser(user);
    }

}
