#include <Arduino.h>
#include <Servo.h>                                      //Biblioteka silniczka Servo
#include <Wire.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <SPI.h>

const int green_Pin = A2;                               //Inicjalizacja pinu od diody zielonej
const int red_Pin = A3;                                 //Inicjalizacja pinu od diody czerwonej
const int TRIG_PIN = 2;                                 //Inicjalizacja pinu od czujnika odleglosci
const int ECHO_PIN = 3;                                 //Inicjalizacja pinu od czujnika odleglosci
const int relay_module = 5;                             //Inicjalizacja pinu od modulu przekaznika
const int key_module = 7;                               //Inicjalizacja pinu od modulu zamka

byte succes_Read = false;
byte mac [] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(192,168,1,140);
unsigned int localPort = 5000;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
String datReq;                                          //String for our data
int packetSize;                                         //Size of the packet


EthernetUDP Udp;                                        // Create a UDP Object
Servo servo;                                            //Inicjalizacja silniczka Servo
EthernetServer server(80);

void setup()
{
    Serial.begin(9600);
    pinMode(green_Pin,OUTPUT);                          //Ustawienie diody zielonej na odczyt
    pinMode(red_Pin,OUTPUT);                            //Ustawienie diody czerwonej na odczyt
    pinMode(key_module, OUTPUT);                        //Ustawienie modulu zamka na odczyt
    pinMode(TRIG_PIN,OUTPUT);                           //Ustawienie czujnika odleglosci na odczyt
    pinMode(ECHO_PIN, INPUT);                           //Ustawienie czujnika odleglosci na zapis

    servo.attach(9);                                    //Inicjalizacja pinu silniczka Servo
    Ethernet.begin(mac,ip);
    Udp.begin(localPort);
    delay(1500);
}

void loop()
{
  if(Serial.available() > 0){
    String content = Serial.readStringUntil('\n');
    if (compare_ID(content))
    {
      Serial.println("Authorized access");
      granted();
      door_Open();
      wait_For_Entry();
      door_Close();
    }
  
   else   {
      Serial.println(" Access denied");
      denied();
    }
  }
}

bool compare_ID(String uid1){
    /*
   * Funkcja compareUids posiada 2 wska??niki jako argumenty
   * -uid1: pierwsza ilo???? byt??w pierwszej karty
   * -uid2: druga ilo???? byt??w drugiej karty\
   * Funkcja por??wnuje bajty w kartach. Je??li, kt??ry?? z bajt??w si?? nie zgadza funkcja zwraca FA??SZ.
   */
   Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());       //Inicjalizacja pakietu do wysy??ania
   Udp.print(uid1);                                         //Wys??anie pakietu z odczytanym kluczem
   Udp.endPacket();                                         //Koniec pakietu
   memset(packetBuffer, 0 , UDP_TX_PACKET_MAX_SIZE);         //Czyszczenie bufora

   while(true){
    Serial.println("Czekam na odebranie danych");
    packetSize = Udp.parsePacket();
    if(packetSize > 0){
      Serial.println("Odebra??em dane");
      Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
      String datReq(packetBuffer);
      if(datReq == "True"){
        memset(packetBuffer, 0 , UDP_TX_PACKET_MAX_SIZE);
        return true;
      }
      if(datReq == "False"){
        memset(packetBuffer, 0 , UDP_TX_PACKET_MAX_SIZE);
        return false;
      }
    }
   }

}

/////////////////////////////////////////  Access Granted    ///////////////////////////////////
void granted (){
    for(int i=0; i<3; i++){
        digitalWrite(green_Pin,HIGH);
        delay(300);
        digitalWrite(green_Pin,LOW);
    }
}

///////////////////////////////////////// Access Denied  ///////////////////////////////////
void denied(){
    for(int i=0; i<3; i++){
        digitalWrite(red_Pin,HIGH);
        delay(300);
        digitalWrite(red_Pin,LOW);
    }
}

void door_Open(){
    digitalWrite(key_module,true);
    digitalWrite(relay_module,HIGH);
    for(int pos = 0; pos < 90; pos++){
        servo.write(pos);
        delay(15);
    }
}

void door_Close(){
    for(int pos = 90; pos >= 0; pos--){
        servo.write(pos);
        delay(15);
    }
    digitalWrite(key_module,false);
}

void wait_For_Entry(){
    int distance = 0;
    int tempolary = 0;
    digitalWrite(TRIG_PIN,HIGH);
    delayMicroseconds(1000);
    digitalWrite(TRIG_PIN,LOW);
    distance = (pulseIn(ECHO_PIN,HIGH)/58);
    distance = tempolary;
    Serial.println("Czekam na wejscie osoby");
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        digitalWrite(TRIG_PIN,HIGH);
        delayMicroseconds(1000);
        digitalWrite(TRIG_PIN,LOW);
        tempolary = (pulseIn(ECHO_PIN,HIGH))/58;
    }
    Serial.println("Czekam na przejscie osoby");
    distance = tempolary;
    delay(1000);
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        digitalWrite(TRIG_PIN,HIGH);
        delayMicroseconds(1000);
        digitalWrite(TRIG_PIN,LOW);
        tempolary = (pulseIn(ECHO_PIN,HIGH))/58;
    }
    delay(1000);
}
