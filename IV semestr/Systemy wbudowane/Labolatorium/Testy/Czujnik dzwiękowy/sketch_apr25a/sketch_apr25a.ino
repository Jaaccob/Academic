#define trig 2
#define echo 3

void setup() {
  // put your setup code here, to run once:
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
  Serial.print("Wszystko działa");
}

void loop() {
  // put your main code here, to run repeatedly:
  int czas, diast;
  digitalWrite(trig,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig,LOW);
  czas = pulseIn(echo,HIGH);
  Serial.println("Czas:");
  Serial.println(czas);
  diast = (czas/58);
  Serial.println("Dystans:");
  Serial.println(diast);
  delay(500);
}
