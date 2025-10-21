# 🛒 ONLINE SHOPPING PROGRAM

## 💡 Overview

This program demonstrates **how an online shopping system works** using Python **classes and objects**.  
It focuses on creating and managing a **shopping cart** where users can add, view, and remove items, and calculate the total price of their purchases.

---

## ⚙️ Step 1: Engine Class

- A class named **`Engine`** is created.  
- It contains the following attributes:
  - **`engine_id`** → Unique ID for each engine  
  - **`name`** → Name of the engine  
  - **`horsepower`** → Engine power (in HP)  

This class represents the **product** available for purchase.

---

## 🧺 Step 2: CartItem Class

- A class named **`CartItem`** is created.  
- It represents a single item added to the shopping cart.  
- The class includes:
  - **`quantity`** → The number of units selected by the user  
  - **`engine`** → The engine object chosen from the Engine class  
  - **`total_price`** → The total cost calculated based on quantity and engine price  

This class connects the **product (engine)** and its **quantity** in the user’s cart.

---

## 🛍️ Step 3: ShoppingCart Class

- A class named **`ShoppingCart`** is created.  
- It allows the user to:
  - **Add items** → Add one or more engines to the cart  
  - **Remove items** → Remove any engine from the cart  
  - **View items** → Display all the products currently in the cart  
  - **Calculate total amount** → Compute the total price of all added items  

This class simulates the core behavior of an **online shopping system** —  
allowing users to manage their shopping experience efficiently.

---

## ✅ Summary

By combining these three classes — **Engine**, **CartItem**, and **ShoppingCart** —  
this program models a simple yet functional **online shopping platform**.  
It demonstrates how **object-oriented programming (OOP)** concepts like **classes**, **objects**, and **methods** can be used to represent real-world systems.
