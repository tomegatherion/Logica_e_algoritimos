// semáforo

int ledVd = 2;
int ledAm = 4;
int ledVe = 7;

void setup()
{
pinMode (ledVd, OUTPUT);
pinMode (ledAm, OUTPUT);
pinMode (ledVe, OUTPUT);
}

void loop()
{
digitalWrite (ledVd, HIGH);
delay(10000);
digitalWrite (ledVd, LOW);

digitalWrite (ledAm, HIGH);
delay(3000);
digitalWrite (ledAm, LOW);

digitalWrite (ledVe, HIGH);
delay(10000);
digitalWrite (ledVe, LOW);
}