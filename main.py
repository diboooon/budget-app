from budget import Category, create_spend_chart

# Example usage of Category class
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
food_category.transfer(50, clothing_category)

print(food_category)

# Example usage of create_spend_chart function
categories = [food_category, clothing_category, entertainment_category]
chart = create_spend_chart(categories)
print(chart)
