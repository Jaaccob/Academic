#include <Arduino.h>
#include <MMRC522.h>                                    //Biblioteka RFID'a
#include <Servo.h>                                      //Biblioteka silniczka Servo
#include "Adafruit_MCP23017.h"
#include <Wire.h>
#include <Ethernet.h>

const int green_Pin = A2;                               //Inicjalizacja pinu od diody zielonej
const int red_Pin = A3;                                 //Inicjalizacja pinu od diody czerwonej
const int SS_PIN = 5;                                   //Inicjalizacja pinu od RFID'a
const int RST_PIN = 3;                                  //Inicjalizacja pinu od RFID'a
//const int TRIG_PIN = ;                                //Inicjalizacja pinu od czujnika odleglosci
//const int ECHO_PIN = ;                                //Inicjalizacja pinu od czujnika odleglosci
//const int relay_module = ;                            //Inicjalizacja pinu od modulu przekaznika
const byte mcp_A_pin_PA0 = 0;                           //Inicjalizacja ECHO_PIN
const byte mcp_A_pin_PA1 = 1;                           //Inicjalizacja TRIG_PIN
const byte mcp_A_pin_PA2 = 2;                           //Inicjalizacja relay_module
const byte mcp_A_pin_PA3 = 3;                           //Inicjalizacja magnetic_lock

byte readCard[4]                                        //Tablica do przechowywania zczytanej karty
byte succes_Read = false;
byte myCard []= {0x13, 0x53, 0xC2, 0x02};
byte mac [] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,1,140);

MFRC522 reader(SS_PIN,RST_PIN);                         //Inicjalizacja RFID'a
Servo servo;                                            //Inicjalizacja silniczka Servo
Adafruit_MCP23017 mcp;
EthernetServer server(80);

void setup()
{
  Serial.begin(9600);
    pinMode(green_Pin,OUTPUT);                          //Ustawienie diody zielonej na odczyt
    pinMode(red_Pin,OUTPUT);                            //Ustawienie diody czerwonej na odczyt
    //pinMode(TRIG_PIN,OUTPUT);                           //Ustawienie czujnika odleglosci na odczyt
    //pinMode(relay_module,OUTPUT);                       //Ustawienie modulu przekaznika na odczyt
    //pinMode(ECHO_PIN, INPUT);                           //Ustawienie czujnika odleglosci na zapis
    servo.attach(9);                                    //Inicjalizacja pinu silniczka Servo
    mcp.begin(7);
    mcp.pinMode(mcp_A_pin_PA0, INPUT);                  //Ustawienie ECHO_PIN na zapis
    mpc.pinMode(mcp_A_pin_PA1, OUTPUT);                 //Ustawienie TRIG_PIN na odczyt
    mpc.pinMode(mcp_A_pin_PA2, OUTPUT);                 //Ustawienie relay_module na odczyt
    mpc.pinMode(mcp_A_pin_PA3, OUTPUT);                 //Ustawienie magnetic_lock na odczyt
    Ethernet.begin(mac,ip);
    server.begin();
}

void loop()
{
    do{
        Serial.println("Czekam na zczytanie karty");
        succes_Read = read_ID();
    }while(succes_Read != true)

    if(compare_ID(readCard,myCard)){
        granted();
        door_Open();
        wait_For_Entry();
        door_Close();
        succes_Read = false;
    }
    else{
        succes_Read = false;
    }
}

bool read_ID(){
    /*
   * Funkcja odpowiedzialna za zczytanie danych z przy³o¿onej do czytnika karty. Funkcja ma równie¿ za zadanie
   * zapisaæ klucz do tablicy readCard i zwróciæ PRAWDÊ jeœli ta operacja siê powiedzie
   */
    if(! MFRC522.PICC_ReadCardSeroal()){
        return false;
    }
    if(! MFRC522.PICC_IsNewCardPresent()){
        return false;
    }
    Serial.print("Scanned ID from Card");
    for(uint8_t i=0; i<4; i++){
        readCard[i] = MFRC522::uid.uidByte[i];
        Serial.print(readCard[i],HEX);
    }
    Serial.println("");
    MFRC522.PICC_HaltA();
    return true;
}

bool compare_ID(byte *uid1,byte *uid2){
    /*
   * Funkcja compareUids posiada 2 wskaŸniki jako argumenty
   * -uid1: pierwsza iloœæ bytów pierwszej karty
   * -uid2: druga iloœæ bytów drugiej karty\
   * Funkcja porównuje bajty w kartach. Jeœli, któryœ z bajtów siê nie zgadza funkcja zwraca FA£SZ.
   */
    for(byte i=0;i<4;i++){
        if(uid1[i] != uid2){
            return false;
        }
    }
    return true;
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
    mcp.digitalWrite(mcp_A_pin_PA3,true);
    mcp.digitalWrite(mcp_A_pin_PA2,HIGH);
    for(pos = 0; pos < 90; pos++){
        servo.write(pos);
        delay(15);
    }
}

void door_Close(){
    for(pos = 90; pos >= 0; pos--){
        servo.write(pos);
        delay(15);
    }
    mcp.digitalWrite(mcp_A_pin_PA3,false);
}

void wait_For_Entry(){
    int distance = 0;
    int tempolary = 0;
    mcp.digitalWrite(mcp_A_pin_PA1,HIGH);
    delayMicrosecond(1000);
    mcp.digitalWrite(mcp_A_pin_PA1,LOW);
    distance = (pulseIn(mcp_A_pin_PA0,HIGH)/58);
    distance = tempolary;
    Serial.println("Czekam na wejscie osoby");
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        mcp.digitalWrite(mcp_A_pin_PA1,HIGH);
        delayMicroseconds(1000);
        mcp.digitalWrite(mcp_A_pin_PA1,LOW);
        tempolary = (pulseIn(mcp_A_pin_PA0,HIGH))/58;
    }
    Serial.println("Czekam na przejscie osoby");
    distance = tempolary
    delay(1000);
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        mcp.digitalWrite(mcp_A_pin_PA1,HIGH);
        delayMicroseconds(1000);
        mcp.digitalWrite(mcp_A_pin_PA1,LOW);
        tempolary = (pulseIn(mcp_A_pin_PA0,HIGH))/58;
    }
    delay(1000);
}
