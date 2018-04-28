# front is ball pickup side
#right_motor = 47248342900055530062059
right_motor = 47242605650456384055223
left_motor= 47258300902698974728146
belt_motor = 47252602797606497861699
#rfid_id = 51965404755240632817534
rfid_id = 51982457885618539128580

#print("hello")
def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    #Robot.run(autonomous_actions)
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    # go straight
    drive_forward()
    # while running belt
    belt_up()
    await Actions.sleep(1.9)
    drive_stop()
    await Actions.sleep(7.0)
    print("1 second has passed in autonomous mode")
    belt_stop()

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    #print("hi")
    #id_num = Robot.get_value(rfid_id, "id")
    #print(id_num)
    if Gamepad.get_value("joystick_left_x") > 0.5:
        drive_right()
    elif Gamepad.get_value("joystick_left_x") < -0.5:
        drive_left()
    elif Gamepad.get_value("joystick_left_y") < -0.5:
        drive_forward()
    elif Gamepad.get_value("joystick_left_y") > 0.5:
        drive_backward()
    else:
        drive_stop()
        
    if Gamepad.get_value("button_a") > 0.5:
        belt_up()
    elif Gamepad.get_value("button_b") > 0.5:
        belt_down()
    else:
        belt_stop()
        
    if Gamepad.get_value("button_x") > 0.5:
        has_rfid = Robot.get_value(rfid_id, "tag_detect")
        print("Is there RFID?: ", has_rfid)
        rfid_number = Robot.get_value(rfid_id, "id")
        print("RFID value: ", rfid_number)
        rfid_result = Robot.decode_message(rfid_number)
        print("Attempt was successful: ", rfid_result)
        
        #print("Attempt for 0 was successful: ", Robot.decode_message(0))
        #print("Attempt for 1 was successful: ", Robot.decode_message(1))
        #print("Attempt for 2 was successful: ", Robot.decode_message(2))
        #print("Attempt for 3 was successful: ", Robot.decode_message(3))
        #print("Attempt for 4 was successful: ", Robot.decode_message(4))
        #print("Attempt for 5 was successful: ", Robot.decode_message(5))
        #print("Attempt for 6 was successful: ", Robot.decode_message(6))
    # if not Robot.get_value(limit_switch_id, "switch1"):
    #     print("switch 1 pressed")
    #     drive_forward()
    # else:
    #     print("switch 1 unpressed")
    #     drive_stop()
    # if  not Robot.get_value(limit_switch_id, "switch0"):
    #     print("Switch 0 pressed")
    #     drive_forward()
    # else:
    #     print("Switch 0 unpressed")
    #     drive_stop()
    
def drive_forward():
    Robot.set_value(left_motor, "duty_cycle", 1.0)
    Robot.set_value(right_motor, "duty_cycle", 1.0)
        
def drive_backward():
    Robot.set_value(left_motor, "duty_cycle", -1.0)
    Robot.set_value(right_motor, "duty_cycle", -1.0)
        
def drive_left():
    Robot.set_value(left_motor, "duty_cycle", -1.0)
    Robot.set_value(right_motor, "duty_cycle", 1.0)
        
def drive_right():
    Robot.set_value(left_motor, "duty_cycle", 1.0)
    Robot.set_value(right_motor, "duty_cycle", -1.0)
        
def drive_stop():
    Robot.set_value(left_motor, "duty_cycle", 0.0)
    Robot.set_value(right_motor, "duty_cycle", 0.0)
        
def belt_up():
    Robot.set_value(belt_motor, "duty_cycle", 1.0)
        
def belt_down():
    Robot.set_value(belt_motor, "duty_cycle", -1.0)
        
def belt_stop():
    Robot.set_value(belt_motor, "duty_cycle", 0.0)
    

    
    
def next_power(num):
  # YOUR CODE HERE
  power = 1
  while True:
    if power >= num:
      return power
    power *= 2

def reverse_digits(num):
  #YOUR CODE HERE
  new_num = 0
  while num > 0:
    digit = num % 10
    new_num = new_num * 10 + digit
    num //= 10
  return new_num

primes = []
def is_prime(i):
  if i in primes:
    return True
  for f in primes:
    if i % f == 0:
      return False
  primes.append(i)
  return True
def smallest_prime_fact(num):
  #YOUR CODE HERE
  if num < 2:
    return num
  i = 2
  while True:
    if is_prime(i):
      if num % i == 0:
        return i
    i += 1
  return 0

def most_common_digit(num):
  #YOUR CODE HERE
  if num == 0:
    return num
  buckets = [0,0,0,0,0, 0,0,0,0,0]
  while num > 0:
    buckets[num % 10] += 1
    num //= 10
  return max(range(9,0,-1), key=(lambda x: buckets[x]))

def silly_base_two(num):
  # YOUR CODE HERE
  bin_num = 0
  multiplier = 1
  while num > 0:
    digit = num % 2
    bin_num = bin_num + multiplier * digit
    num //= 2
    multiplier *= 10
  return bin_num

def double_caesar_cipher(num):
  # YOUR CODE HERE
  pi = 3141592653
  num2 = num
  new_num = 0
  multiplier = 1
  while pi > 0:
    new_num += multiplier * ((pi % 10 + num2 % 10) % 10)
    pi //= 10
    num2 //= 10
    if num2 == 0:
      num2 = num
    multiplier *= 10
  return new_num

def valid_isbn_ten(num):
    #YOUR CODE HERE
    i = 1
    num2 = num
    summ = 0
    while num2 > 0:
      summ += (num2 % 10) * i
      i += 1
      num2 //= 10
    
    #return summ + (11 - summ % 11) % 11
    if summ % 11 == 0:
      return num
    return valid_isbn_ten(num + 1)

def simd_four_square(num):
    #YOUR CODE HERE
    num2 = num
    digits = 0
    while num2 > 0:
      digits += 1
      num2 //= 10
    chunk_size = digits // 4 + (digits % 4 != 0)
    
    summ = 0
    num2 = num
    multiplier = 1
    for i in range(4):
      ten_chunk_size = 10**chunk_size
      chunk = num2 % ten_chunk_size
      num2 //= ten_chunk_size
      square = (chunk * chunk) % ten_chunk_size
      summ += square* multiplier
      multiplier *= ten_chunk_size
      
    return summ


    
