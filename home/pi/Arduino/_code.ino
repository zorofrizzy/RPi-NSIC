int countTeam1=0;
int countTeam2=0;

void setup()
{
  
  // SENSOR
  
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  
  
  // LEDS
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(3., OUTPUT);
  
  
}

void loop()
{
 
 
  
  if(digitalRead(6)==HIGH)
  {
    countTeam1++;
  }
  
    
  if(digitalRead(7)==HIGH)
  {
    countTeam2++;
  }


if((countTeam2 ==1) || (countTeam1 ==1))
{
   digitalWrite(10, HIGH);
}

switch(countTeam1)
{
  case '4' : 
                digitalWrite(8, HIGH);
                break;
  case '5' :    digitalWrite(9, HIGH);
                break;
              
}                

switch(countTeam2)
{
  case '4' : 
                digitalWrite(11, HIGH);
                break;
  case '5' :    digitalWrite(12, HIGH);
                break;
              
} 

if((countTeam2 ==10) || (countTeam1 ==10))
{
   digitalWrite(3, HIGH);
}
}
