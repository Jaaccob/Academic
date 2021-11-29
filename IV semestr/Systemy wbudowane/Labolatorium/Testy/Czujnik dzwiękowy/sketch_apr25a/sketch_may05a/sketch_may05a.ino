#define trigPin 8
#define echoPin 10
const int greenPin = A0;                              //Inicjalizacja pinu odpowiedzialnego za zielony kolor
const int redPin = A1;                                //Inicjalizacja pinu odpowiedzialnego za czerwony kolor

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
  Serial.begin(9600);
  Serial.print("Wszystko działa");
}

void loop() {
  // put your main code here, to run repeatedly:
  zakres(1,25);
}

int zmierzOdleglosc() {
  long czas, dystans;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  dystans = (pulseIn(echoPin,HIGH)/2)/29.1;
  Serial.println(dystans);
  return dystans;
}

 
void zakres(int a, int b) {
  int jakDaleko = zmierzOdleglosc();
  Serial.println("Tak Daleko:");
  Serial.println(jakDaleko);
  if ((jakDaleko > a) && (jakDaleko < b)) {
      digitalWrite(redPin, HIGH); //Włączamy buzzer
      delay(500);
  } else {
      digitalWrite(redPin, LOW); //Wyłączamy buzzer, gdy obiekt poza zakresem
      delay(500);
  }
}
