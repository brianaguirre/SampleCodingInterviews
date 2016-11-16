//
// TestString.cpp
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


  // 1-1
  const std::string hello = "Hello";
  const std::string message = hello + ", world" + "!";     //Compiles

  // Why?
  // Compiles because you're following the rules of concatinating a string lit and a string object.
  // The left-associative property of + makes it so that hello + ", world" is processed first.



  // 1-2
  const std::string exclam = "!";
  const std::string message1 = "Hello" + ", world" + exclam;      //Fails 

  // Why?
  // Because of left-associative property: s.t. ("Hello" + ", world") + exclam. 
  // Cannnot + two string literals because they're an array of chars.
  // So it's like adding to pointers together: const char* s1 + const char* s2. 
  // Doesn't make sense. We can fix this by adding () arround ", world" + exclam
  // const std::string exclam = "!";
  // const std::string message1 = "Hello" + (", world" + exclam);

  // 1-3
  {
    const std::string s = "a string";
    std::cout << s << std::endl;
  }

  {
    const std::string s = "another string";
    std::cout << s << std::endl;
  }

  // Valid because the scope is limited by the {}.
  // So s soon as s is printed in the first statement, that variable is destroyed and memory is freed up for another variable.
  // In this case that variable has the same name, but that's still valid.

  // 1-4
  { 
    const std::string s = "a string";
    std::cout << s << std::endl;
    { 
      const std::string s = "another string";
      std::cout << s << std::endl; 
    };
  }
  // Yes. Still valid, since scope is different due toe defining second string object s under second set of {}
  // We can use same name for variables if their scopes are different in C++.

  // 1-5
  {
    std::string s = "a string";
    {
      std::string x = s + ", really";
      std::cout << s << std::endl;
    }
      std::cout << x << std::endl;
  }

  // Not a valid program. String object x is referenced outside of its scope. Which makes it so that the compiler thinks it's undefined.
  // Solution: Either define x within the first set of brackets as an empty string, and then modify it within the second set of {}
  // {
  //   std::string s = "a string";
  //   std::string x;
  //   {
  //     x = s + ", really";
  //     std::cout << s << std::endl;
  //   }
  //     std::cout << x << std::endl;
  // }


  return 0;

}

