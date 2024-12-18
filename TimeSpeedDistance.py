print('              ****** TIME SPEED DISTANCE CALCULATOR ******               ')
print('')
print('I KNOW FINDING TIME/SPEED/DISTANCE IS VERY BORING WORK, SO THATS WHY I AM HERE')
print('')
choice = str(input('Please select, what you want to find = '))


#if choice is time 
if choice == "time":
  timeType = str(input('In which format do u want to find time? = '))

# code to find time in hours
  if timeType == "hours":
    speedType = str(input('In which format do you have Speed? 1) m/s 2) km/hr = '))
    distanceType = str(input("In which format do you have distance? 1) kilometers 2) meters = "))

    if speedType == "m/s" and distanceType == "meters":
      speedMs = float(input("Enter your m/s Speed = "))
      distanceM = float(input('Enter your Distance = '))
      Skm = speedMs*(18/5)
      Dm = distanceM/1000

      time1 = Dm/Skm
      print("Your required time is", time1, " hrs")

    elif speedType == "m/s" and distanceType == 'kilometers':
      speedMs = float(input('Enter your m/s Speed = '))
      distanceM = float(input('Enter your Distance = '))
      Skm = speedMs*(18/5)
      
      time2 = distanceM/Skm
      print("Your required time is", time2, " hrs" )

    elif speedType == "km/hr" and distanceType == 'meters':
      speedMs = float(input('Enter your km/hr Speed = '))
      distanceM = float(input('Enter your Distance = '))
      Dm = distanceM/1000
      
      time3 = Dm/speedMs
      print("Your required time is", time3, " hrs" )

    elif speedType == "km/hr" and distanceType == 'kilometers':
      speedMs = float(input('Enter your km/hr Speed = '))
      distanceM = float(input('Enter your Distance = '))
      
      time4 = distanceM/speedMs
      print("Your required time is", time4, " hrs" )
    
# code to find time in seconds 
  elif timeType == "seconds":
    speedType = str(input('In which format do you have speed? 1) m/s 2) km/hr = '))
    distanceType = str(input("In which format do you have distance? 1) kilometers 2) meters = "))

    if speedType == "m/s" and distanceType == "meters":
      speedMs = float(input("Enter your m/s Speed = "))
      distanceM = float(input('Enter your Distance = '))

      time5 = distanceM/speedMs
      print("Your required time is", time5, " sec")

    elif speedType == "m/s" and distanceType == 'kilometers':
      speedMs = float(input('Enter your m/s Speed = '))
      distanceM = float(input('Enter your Distance = '))
      Dm = distanceM*1000
      
      time6 = Dm/speedMs
      print("Your required time is", time6, " sec" )

    elif speedType == "km/hr" and distanceType == 'meters':
      speedMs = float(input('Enter your km/hr Speed = '))
      distanceM = float(input('Enter your Distance = '))
      Skm = speedMs*(5/18)
      
      time7 = distanceM/Skm
      print("Your required time is", time7, " sec" )

    elif speedType == "km/hr" and distanceType == 'kilometers':
      speedMs = float(input('Enter your km/hr Speed = '))
      distanceM = float(input('Enter your Distance = '))
      Dm = distanceM*1000
      Skm = speedMs*(5/18)
      
      time8 = Dm/Skm
      print("Your required time is", time8, " sec" )

#if choice is speed
elif choice == "speed":
  Speedtype = str(input("In which format do you want to find Speed? = "))

  #if code to find speed in km/hr
  if Speedtype == "km/hr":
    distanceS = str(input('In which format do u have distance?? 1) kilometers 2) meters = '))
    timeS= str(input('In which format do you have time?? 1) hours 2) seconds = '))

    if distanceS == "kilometers" and timeS == 'hours':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      speed = distanceSp/timeSp
      print('This is your required Speed = ',speed, ' km/hr')

    elif distanceS == "meters" and timeS == 'hours':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ds = distanceSp/1000 

      speed = Ds/timeSp
      print('This is your required Speed = ',speed, ' km/hr')

    elif distanceS == "meters" and timeS == 'seconds':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ds = distanceSp/1000 
      Ts = timeSp/3600

      speed = Ds/Ts
      print('This is your required Speed = ',speed, ' km/hr')

    elif distanceS == "kilometers" and timeS == 'seconds':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ts = timeSp/3600 

      speed = distanceSp/Ts
      print('This is your required Speed = ',speed, ' km/hr')

#if code to find speed in m/s
  elif Speedtype == "m/s":
    distanceS = str(input('In which format do u have distance?? 1) kilometers 2) meters = '))
    timeS= str(input('In which format do you have time?? 1) hours 2) seconds = '))

    if distanceS == "meters" and timeS == 'seconds':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))

      speed = distanceSp/timeSp
      print('This is your required Speed = ',speed, ' m/s')

    elif distanceS == "meters" and timeS == 'hours':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ts = timeSp*3600 

      speed = distanceSp/Ts
      print('This is your required Speed = ',speed, ' m/s')

    elif distanceS == "kilometers" and timeS == 'seconds':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ds = distanceSp*1000 
      

      speed = Ds/timeSp
      print('This is your required Speed = ',speed, ' m/s')

    elif distanceS == "kilometers" and timeS == 'hours':
      distanceSp = float(input('Enter your Distance here = '))
      timeSp = float(input('Enter your Time here = '))
      Ts = timeSp*3600 
      Ds = distanceSp*1000

      speed = Ds/Ts
      print('This is your required Speed = ',speed, ' m/s')

#if choice is distance

elif choice == "distance":
  distancetype = str(input('In which format do you want to find Distance? = '))

#code to find distance in km
  if distancetype == "km":
    speedD = str(input('In which format do u have Speed?? 1) km/hr 2) m/s = '))
    timeD= str(input('In which format do you have Time?? 1) hours 2) seconds = '))

    if speedD == "km/hr" and timeD == 'hours':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))

      distance = speedDi*timedi
      print('This is your required Distance = ',distance, ' km')

    elif speedD == "km/hr" and timeD == 'seconds':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Td = timedi/3600

      distance = speedDi*Td
      print('This is your required Distance = ',distance, ' km')

    elif speedD == "m/s" and timeD == 'hours':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Sd = speedDi*(18/5)

      distance = Sd*timedi
      print('This is your required Distance = ',distance, ' km')

    elif speedD == "m/s" and timeD == 'seconds':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Sd = speedDi*(18/5)
      Td = timedi/3600

      distance = Sd*Td
      print('This is your required Distance = ',distance, ' km')

#code to find diatnce in meters
  elif distancetype == "m":
    speedD = str(input('In which format do u have Speed?? 1) km/hr 2) m/s = '))
    timeD= str(input('In which format do you have Time?? 1) hours 2) seconds = '))

    if speedD == "km/hr" and timeD == 'hours':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Sd = speedDi*(5/18)
      Td = timedi*3600

      distance = Sd*Td
      print('This is your required Distance = ',distance, ' m')

    elif speedD == "km/hr" and timeD == 'seconds':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Sd = speedDi*(5/18)

      distance = Sd*timedi
      print('This is your required Distance = ',distance, ' m')

    elif speedD == "m/s" and timeD == 'hours':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))
      Td = timedi*3600

      distance =speedDi*Td
      print('This is your required Distance = ',distance, ' m')

    elif speedD == "m/s" and timeD == 'seconds':
      speedDi = float(input('Enter your Speed here = '))
      timedi = float(input('Enter your Time here = '))

      distance = speedDi*timedi
      print('This is your required Distance = ',distance, ' m')






  

  










    

            

    


  




