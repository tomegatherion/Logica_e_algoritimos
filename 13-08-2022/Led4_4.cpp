// Vamos acender o LED
//
int led1 = 2;
int led2 = 4;
int led3 = 7;
int led4 = 8;
void setup()
{
}

void loop()
{
rotina_1();
rotina_2();
rotina_3();
}

void rotina_1()
{
  digitalWrite(led1, HIGH);
  delay(2000);
  digitalWrite(led1, LOW);
 
  digitalWrite(led2, HIGH);
  delay(2000);
  digitalWrite(led2, LOW);
 
  digitalWrite(led3, HIGH);
  delay(2000);
  digitalWrite(led3, LOW);
 
  digitalWrite(led4, HIGH);
  delay(2000);
  digitalWrite(led4, LOW);
}

void rotina_2()
{
  digitalWrite(led1, HIGH);
  digitalWrite(led3, HIGH);
  delay(2000);
  digitalWrite(led1, LOW);
  digitalWrite(led3, LOW);
     
  digitalWrite(led2, HIGH);
  digitalWrite(led4, HIGH);
  delay(2000);
  digitalWrite(led2, LOW);
  digitalWrite(led4, LOW);
 
}

void rotina_3()
{
  digitalWrite(led1, HIGH);
  digitalWrite(led4, HIGH);
  delay(2000);
  digitalWrite(led1, LOW);
  digitalWrite(led4, LOW);
     
  digitalWrite(led2, HIGH);
  digitalWrite(led3, HIGH);
  delay(2000);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);  
}