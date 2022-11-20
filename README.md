# Shopping Cart Kata
Repository for the shopping cart app.

## Contents
- [Problem Statement](#problem-statement)
- [How to Run](#how-to-run)
- [Module Description](#module-description)

## Problem Statement

You are implementing a simple checkout system, there are four products available, each with a price per unit.
Some products have a special price when bought in certain quantities (e.g. 3 of product A costs 140, not 150). 
Implement a checkout system that consumes a data source like this: [{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}], 
and return the sub total when queried.

| Item Code | Unit Price | Special Price |
|:---------:|:----------:|:-------------:|
|     A     |     50     |   3 for 140   |
|     B     |     35     |   2 for 60    |
|     C     |     25     |               |
|     D     |     12     |               |

## How to Run
CheckoutTest.py contains the automated tests. 

UserTest.py allows the user to control the input of the program.

## Module description

- ```Item.py``` Implementation of the Product
- ```Checkout.py``` Implementation of the Shop
- ```UserTest.py``` Allows the user to control input of program
- ```CheckoutTest.py``` Runs the automated tests
