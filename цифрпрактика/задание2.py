class Recipe:
    def __init__(self, name,ingredients):
        self.name = name         
        self.ingredients = ingredients         

    def print_ingredients(self):
        print(f'Ингредиенты для {self.name}:')
        for i in self.ingredients:
            print(f'- {i}')
    
    def cook(self):
        print( f'Сегодня мы готовим {self.name}.')
        print( f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print( f'Блюдо {self.name} готово!')

# создаем рецепт спагетти болоньезе
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()  

# создаем рецепт для торта
cake = Recipe("Торт", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт торта
cake.print_ingredients()

# готовим торт
cake.cook()
