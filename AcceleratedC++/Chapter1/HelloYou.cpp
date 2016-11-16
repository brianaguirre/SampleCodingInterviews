//
// HelloYou.cpp
// Chapter1
//
// Created by Brian Aguirre on 11/14/2016.
// Copyright © Brian Aguirre. All rights reserved.
// 
// ask for a person's name, and greet the person

#include <iostream>
#include <string>

int main(){

  // ask for a person's name:
  std::cout << "Please enter your first name: ";

  // read the name:
  std::string name;         // define name
  std::cin >> name;         // read into name variable

  // write a greeting:
  std::cout << "Hello " << name << "!" << std::endl;

  
  return 0;
}