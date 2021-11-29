#define trig 8
#define echo 10
#define red A0
#define green A1
int distance1 = 0;
int distance2 = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  
  Serial.begin(9600);
  Serial.print("Wszystko działa");
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig,LOW);
  distance1 = (pulseIn(echo,HIGH)/2)/29.1;
  Serial.println(distance1);
  distance2= distance1;
  Serial.println("Dystans poczatkowy1:");
  Serial.println(distance1);
  while(distance1 + 2 >distance2 or distance1 - 2 > distance2){
    digitalWrite(trig,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trig,LOW);
    distance2 = (pulseIn(echo,HIGH)/2)/29.1;
    digitalWrite(red,HIGH);
    Serial.println("Dystans przejściowy");
    Serial.println(distance2);
  }
  digitalWrite(red,LOW);
  delay(1000);
  distance1= distance2;
  while(distance1 + 2 >distance2 or distance1 - 2 > distance2){
    digitalWrite(trig,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trig,LOW);
    distance2 = (pulseIn(echo,HIGH)/2)/29.1;
    digitalWrite(green,HIGH);
    Serial.println("Dystans przejściowy");
    Serial.println(distance2);
  }
 digitalWrite(green,LOW);
 delay(1000);
}
