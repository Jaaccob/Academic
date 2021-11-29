#include <Arduino.h>
#include <MFRC522.h>                                    //Biblioteka RFID'a
#include <Servo.h>                                      //Biblioteka silniczka Servo
#include "Adafruit_MCP23017.h"
#include <Wire.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include "Wire.h"

const int green_Pin = A2;                               //Inicjalizacja pinu od diody zielonej
const int red_Pin = A3;                                 //Inicjalizacja pinu od diody czerwonej
const int SS_PIN = 9;                                   //Inicjalizacja pinu od RFID'a
const int RST_PIN = 8;                                  //Inicjalizacja pinu od RFID'a
const int TRIG_PIN = 2;                                 //Inicjalizacja pinu od czujnika odleglosci
const int ECHO_PIN = 3;                                 //Inicjalizacja pinu od czujnika odleglosci
const int relay_module = 5;                             //Inicjalizacja pinu od modulu przekaznika
const int key_module = 7;                               //Inicjalizacja pinu od modulu zamka

//byte readCard[4]                                        //Tablica do przechowywania zczytanej karty
byte succes_Read = false;
byte myCard []= {0x13, 0x53, 0xC2, 0x02};
byte mac [] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,1,140);
unsigned int localPort = 5000;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
String datReq;                                          //String for our data
int packetSize;                                         //Size of the packet


EthernetUDP Udp;                                        // Create a UDP Object
MFRC522 reader(SS_PIN,RST_PIN);                         //Inicjalizacja RFID'a
Servo servo;                                            //Inicjalizacja silniczka Servo
EthernetServer server(80);

void setup()
{
  Serial.begin(9600);
  //reader.init();
    pinMode(green_Pin,OUTPUT);                          //Ustawienie diody zielonej na odczyt
    pinMode(red_Pin,OUTPUT);                            //Ustawienie diody czerwonej na odczyt
    pinMode(key_module, OUTPUT);                        //Ustawienie modulu zamka na odczyt
    pinMode(relay_module,OUTPUT);                       //Ustawienie modulu przekaznika na odczyt
    pinMode(TRIG_PIN,OUTPUT);                           //Ustawienie czujnika odleglosci na odczyt
    pinMode(ECHO_PIN, INPUT);                           //Ustawienie czujnika odleglosci na zapis

    servo.attach(9);                                    //Inicjalizacja pinu silniczka Servo
    Ethernet.begin(mac,ip);
    Udp.begin(localPort);
    delay(1500);
}

void loop()
{
  if ( ! reader.PICC_IsNewCardPresent())
  {
    return;
  }
  if ( ! reader.PICC_ReadCardSerial())
  {
    return;
  }
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < reader.uid.size; i++)
  {
     Serial.print(reader.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(reader.uid.uidByte[i], HEX);
     content.concat(String(reader.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(reader.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();
  if (compare_ID(content))
  {
    Serial.println("Authorized access");
    Serial.println();
    delay(3000);
  }

 else   {
    Serial.println(" Access denied");
    delay(3000);
  }
}

bool compare_ID(String uid1){
    /*
   * Funkcja compareUids posiada 2 wskaŸniki jako argumenty
   * -uid1: pierwsza iloœæ bytów pierwszej karty
   * -uid2: druga iloœæ bytów drugiej karty\
   * Funkcja porównuje bajty w kartach. Jeœli, któryœ z bajtów siê nie zgadza funkcja zwraca FA£SZ.
   */
   Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());       //Inicjalizacja pakietu do wysyłania
   Udp.print(uid1);                                         //Wysłanie pakietu z odczytanym kluczem
   Udp.endPacket();                                         //Koniec pakietu
   memset(packetBuffer, 0 , UDP_TX_PACKET_MAX_SIZE);        //Czyszczenie bufora

   while(true){
    Serial.println("Czekam na odebranie danych");
    packetSize = Udp.parsePacket();
    if(packetSize > 0){
        break;
    }
   }
   Serial.println("Odebrałem dane");
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
