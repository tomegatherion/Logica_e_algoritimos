// 10 leds sequenciais
//
int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
int led6 = 7;
int led7 = 8;
int led8 = 9;
int led9 = 10;
int led10 = 11;

void setup()
{
pinMode (led2, OUTPUT);
pinMode (led4, OUTPUT);
pinMode (led5, OUTPUT);
pinMode (led8, OUTPUT);
pinMode (led9, OUTPUT);
pinMode (led10, OUTPUT);
}


void loop()
{
rotina_1();
rotina_2();
}

void rotina_1()
{
digitalWrite (led1, HIGH);
delay(500);
digitalWrite (led1, LOW);
  
digitalWrite (led2, HIGH);
delay(500);
digitalWrite (led2, LOW);
  
digitalWrite (led3, HIGH);
delay(500);
digitalWrite (led3, LOW);
  
digitalWrite (led4, HIGH);
delay(500);
digitalWrite (led4, LOW);
  
digitalWrite (led5, HIGH);
delay(500);
digitalWrite (led5, LOW);
  
digitalWrite (led6, HIGH);
delay(500);
digitalWrite (led6, LOW);
  
digitalWrite (led7, HIGH);
delay(500);
digitalWrite (led7, LOW);
  
digitalWrite (led8, HIGH);
delay(500);
digitalWrite (led8, LOW);
  
digitalWrite (led9, HIGH);
delay(500);
digitalWrite (led9, LOW);
  
digitalWrite (led10, HIGH);
delay(500);
digitalWrite (led10, LOW);
}



void rotina_2()
{
digitalWrite (led10, HIGH);
delay(500);
digitalWrite (led10, LOW);
 
digitalWrite (led9, HIGH);
delay(500);
digitalWrite (led9, LOW);
 
digitalWrite (led8, HIGH);
delay(500);
digitalWrite (led8, LOW);
  
digitalWrite (led7, HIGH);
delay(500);
digitalWrite (led7, LOW);
  
digitalWrite (led6, HIGH);
delay(500);
digitalWrite (led6, LOW);
  
digitalWrite (led5, HIGH);
delay(500);
digitalWrite (led5, LOW);
  
digitalWrite (led4, HIGH);
delay(500);
digitalWrite (led4, LOW);
  
digitalWrite (led3, HIGH);
delay(500);
digitalWrite (led3, LOW);
  
digitalWrite (led2, HIGH);
delay(500);
digitalWrite (led2, LOW);
  
digitalWrite (led1, HIGH);
delay(500);
digitalWrite (led1, LOW);
}