class CoffeeMachine():
  state = 'start'
  def __init__(self):
    # $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
    self.total_water = 400
    self.total_milk = 540
    self.total_coffee_beans = 120
    self.total_disposable_cups = 9
    self.total_money = 550

  def show_info(self):
      print('The coffee machine has:')
      print(self.total_water, 'of water')
      print(self.total_milk, 'of milk')
      print(self.total_coffee_beans, 'of coffee beans')
      print(self.total_disposable_cups, 'of disposable cups')
      print(self.total_money, 'of money')

  def check_ingredients(self, water, milk, beans, cups):
      ingredientName = ''
      if self.total_water < water:
          ingredientName =  'water'
      elif self.total_milk < milk:
          ingredientName = 'milk'
      elif self.total_coffee_beans < beans:
          ingredientName = 'coffee beans'
      elif self.total_disposable_cups < cups:
          ingredientName = 'cup'
      
      return ingredientName  

  def change_stock(self, water, milk, beans, cups, money):
      self.total_water += water
      self.total_milk += milk
      self.total_coffee_beans += beans
      self.total_disposable_cups += cups
      self.total_money += money
      
  def make_espresso(self):
      #For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
      missing_ingredient = self.check_ingredients(250, 0, 16, 1)
      if len(missing_ingredient) > 0:
          print(f'Sorry, not enough {missing_ingredient}!')
      else:
          print('I have enough resources, making you a coffee!')
          self.change_stock(-250, 0, -16, -1, 4)
      
  def make_latte(self):
      #For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
      missing_ingredient = self.check_ingredients(350, 75, 20, 1)
      if len(missing_ingredient) > 0:
          print(f'Sorry, not enough {missing_ingredient}!')
      else:
          print('I have enough resources, making you a coffee!')
          self.change_stock(-350, -75, -20, -1, 7)
      
  def make_cappuccino(self):
      #And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.   
      missing_ingredient = self.check_ingredients(200, 100, 12, 1)
      if len(missing_ingredient) > 0:
          print(f'Sorry, not enough {missing_ingredient}!')
      else:
          print('I have enough resources, making you a coffee!')
          self.change_stock(-200, -100, -12, -1, 6)

  def buy_coffee(self): 
      coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
      if coffee_type == '1':
          self.make_espresso()
      elif coffee_type == '2':
          self.make_latte()
      elif coffee_type == '3':
          self.make_cappuccino()

  def fill_machine(self):   
      water = int(input('Write how many ml of water do you want to add:'))
      milk = int(input('Write how many ml of milk do you want to add:'))
      coffee_beans = int(input('Write how many grams of coffee beans do you want to add:'))
      disposable_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
      self.change_stock(water, milk,coffee_beans, disposable_cups, 0)

  def take_money(self):
      print('I gave you $' + str(self.total_money))
      self.change_stock(0,0,0,0,-self.total_money)

  def doAction(self):
      if action == 'buy': 
          self.buy_coffee()
      elif action == 'fill':
          self.fill_machine()
      elif action == 'take':
          self.take_money()
      elif action == 'remaining':
          self.show_info()
    
coffee_machine = CoffeeMachine()
while coffee_machine.state != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):')
    coffee_machine.state = action
    coffee_machine.doAction()
    