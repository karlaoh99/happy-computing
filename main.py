import math
from generators import generate_service_type, generate_arrival_time, generate_seller_time, generate_repair_time, generate_change_time
from services import *


class HappyComputing():
    def __init__(self):
        self.T = 480
        self.restart()

    def isEmpty(self):
        return self.seller_queue + self.repair_queue + self.change_queue == 0 and self.t_seller1 == self.t_seller2 == self.t_tech1 == self.t_tech2 == self.t_tech3 == self.t_sptech == math.inf 

    def restart(self):
        # Time variable
        self.t = 0

        # Counting variables
        self.count_s1 = 0
        self.count_s2 = 0
        self.count_s3 = 0
        self.count_s4 = 0

        # State variables
        self.seller_queue = 0
        self.repair_queue = 0
        self.change_queue = 0

        # Event list
        self.t_next_arrive = generate_arrival_time()
        self.t_seller1 = math.inf
        self.t_seller2 = math.inf
        self.t_tech1 = math.inf
        self.t_tech2 = math.inf
        self.t_tech3 = math.inf
        self.t_sptech = math.inf

    def print_time(self):
        t = int(self.t)
        h = int(t / 60)
        m = t - (h * 60)
        h += 8
        
        if m < 10:
            str_m = f'0{m}'
        else:
            str_m = f'{m}'

        if h < 12:
            print(f'\n{h}:{str_m} am')
        elif h < 13:
            print(f'\n{h}:{str_m} pm')
        else:
            print(f'\n{h - 12}:{str_m} pm') 
    
    def interate(self):
        time = min(self.t_next_arrive, self.t_seller1, self.t_seller2, self.t_tech1, self.t_tech2, self.t_tech3, self.t_sptech)
        self.t = time
        
        # The workshop is closed and there are no customers left to attend
        if time > self.T and self.isEmpty():
            print('\nThe workshop is closed')
            return 1
        
        # The workshop is closed and there are customers left to attend
        if time == self.t_next_arrive and time > self.T:
            self.t_next_arrive = math.inf
            return 0
        
        self.print_time()
        
        # A new customer enters the workshop
        if time == self.t_next_arrive:
            if time > self.T:
                self.t_next_arrive = math.inf
                return 0

            print('A new customer enters the workshop')
            self.t_next_arrive = self.t + generate_arrival_time() 
            
            if self.t_seller1 == math.inf:
                print('The customer is attended by seller 1')
                self.t_seller1 = self.t + generate_seller_time()
            elif self.t_seller2 == math.inf:
                print('The customer is attended by seller 2')
                self.t_seller2 = self.t + generate_seller_time()
            else:
                print('The customer joins the end of the queue')
                self.seller_queue += 1    

        # A seller finishes attending a customer
        elif time == self.t_seller1 or time == self.t_seller2:
            if time == self.t_seller1:
                print('Seller 1 finishes attending a customer')
                if self.seller_queue > 0:
                    self.seller_queue -= 1
                    self.t_seller1 = self. t + generate_seller_time()
                else:
                    self.t_seller1 = math.inf
            else:
                print('Seller 2 finishes attending a customer')
                if self.seller_queue > 0:
                    self.seller_queue -= 1
                    self.t_seller2 = self. t + generate_seller_time()
                else:
                    self.t_seller2 = math.inf

            service = generate_service_type()
            if service == Service.WARRANTY_REPAIR or service == Service.OUT_OF_WARRANTY_REPAIR:
                if service == Service.WARRANTY_REPAIR:
                    self.count_s1 += 1
                else:
                    self.count_s2 += 1
                
                if self.t_tech1 == math.inf:
                    print('The customer wants a repair so he goes to be attended by technician 1')
                    self.t_tech1 = self.t + generate_repair_time()
                elif self.t_tech2 == math.inf:
                    print('The customer wants a repair so he goes to be attended by technician 2')
                    self.t_tech2 = self.t + generate_repair_time()
                elif self.t_tech3 == math.inf:
                    print('The customer wants a repair so he goes to be attended by technician 3')
                    self.t_tech3 = self.t + generate_repair_time()
                elif self.t_sptech == math.inf:
                    print('The customer wants a repair so he goes to be attended by the specialized technician')
                    self.t_sptech = self.t + generate_repair_time()
                else:
                    print('The customer wants a repair so he joins the repair queue')
                    self.repair_queue += 1

            elif service == Service.CHANGE_OF_EQUIPMENT:
                self.count_s3 += 1
                if self.t_sptech == math.inf:
                    print('The customer wants a change of equipment so he goes to be attended by the specialized technician')
                    self.t_sptech = self.t + generate_change_time()
                else:
                    print('The customer wants a change of equipment so he joins the change queue')
                    self.change_queue += 1

            elif service == Service.SELL_OF_EQUIPMENT:
                print('The customer just wanted an equipment sell, so he left the workshop')
                self.count_s4 += 1

        # Technician 1 finishes attending a customer
        elif time == self.t_tech1:
            print('Technician 1 finishes attending a customer')

            if self.repair_queue > 0:
                self.repair_queue -= 1
                self.t_tech1 = self.t + generate_repair_time()
            else:
                self.t_tech1 = math.inf

        # Technician 2 finishes attending a customer
        elif time == self.t_tech2:
            print('Technician 2 finishes attending a customer')
            
            if self.repair_queue > 0:
                self.repair_queue -= 1
                self.t_tech2 = self.t + generate_repair_time()
            else:
                self.t_tech2 = math.inf

        # Technician 3 finishes attending a customer
        elif time == self.t_tech3:
            print('Technician 3 finishes attending a customer')

            if self.repair_queue > 0:
                self.repair_queue -= 1
                self.t_tech3 = self.t + generate_repair_time()
            else:
                self.t_tech3 = math.inf

        # Specialized technician finishes attending a customer
        elif time == self.t_sptech:
            print('Specialized technician finishes attending a customer')

            if self.change_queue > 0:
                self.change_queue -= 1
                self.t_sptech = self.t + generate_change_time()
            elif self.repair_queue > 0:
                self.repair_queue -= 1
                self.t_sptech = self.t + generate_repair_time()
            else:
                self.t_sptech = math.inf

        return 0

    def run(self):
        print('The store opens at 8:00 am')
        self.restart()

        state = 0
        while(state < 1):
            state = self.interate()

        profit = self.count_s1 * services_price[1] + self.count_s2 * services_price[2] + self.count_s3 * services_price[3] + self.count_s4 * services_price[4]
        print(f'\nThe profit in the working day was ${profit}')
        return profit


workshop = HappyComputing()
workshop.run()