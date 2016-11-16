//
// TestStringConstructor.cpp
// Chapter1
//
// Created by Brian Aguirre on 11/14/2016.
// Copyright © Brian Aguirre. All rights reserved.
// 
// Testing string = and string()

#include <iostream>
#include <string>


int main(){

  std::string s;        // empty string
  std::string t = s;    // string t contains copy of characters in s

  char c = '*';
  int n = 10;
  std::string z(n, c);     // string z contains 10 characters of the word Hello


  std::cout << z << std::endl;





  return 0;
}