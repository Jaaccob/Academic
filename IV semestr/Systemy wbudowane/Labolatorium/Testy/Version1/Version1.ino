#include <Arduino.h>
#include <MMRC522.h>                                    //Biblioteka RFID'a
#include <Servo.h>                                      //Biblioteka silniczka Servo

const int green_Pin = A0;                               //Inicjalizacja pinu od diody zielonej
const int red_Pin = A1;                                 //Inicjalizacja pinu od diody czerwonej
const int SS_PIN = 5;                                   //Inicjalizacja pinu od RFID'a
const int RST_PIN = 3;                                  //Inicjalizacja pinu od RFID'a
const int TRIG_PIN = 8;                                 //Inicjalizacja pinu od czujnika odległości
const int ECHO_PIN = 10;                                //Inicjalizacja pinu od czujnika odległości
const int relay_module = 6;                             //Inicjalizacja pinu od modułu przekaźnika

MFRC522 reader(SS_PIN,RST_PIN);                         //Inicjalizacja RFID'a
Servo servo;                                            //Inicjalizacja silniczka Servo

byte readCard[4]                                        //Tablica do przechowywania zczytanej karty
byte succes_Read = false;
byte myCard []= {0x13, 0x53, 0xC2, 0x02};

void setup()
{
  Serial.begin(9600);
    pinMode(green_Pin,OUTPUT);                          //Ustawienie diody zielonej na odczyt
    pinMode(red_Pin,OUTPUT);                            //Ustawienie diody czerwonej na odczyt
    pinMode(TRIG_PIN,OUTPUT);                           //Ustawienie czujnika odległości na odczyt
    pinMode(relay_module,OUTPUT);                       //Ustawienie moułu przekaźnika na odczyt
    pinMode(ECHO_PIN, INPUT);                           //Ustawienie czujnika odległości na zapis
    servo.attach(9);                                    //Inicjalizacja pinu silniczka Servo
}

void loop()
{
    do{
        Serial.println("Czekam na zczytanie karty");
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
   * Funkcja odpowiedzialna za zczytanie danych z przyłożonej do czytnika karty. Funkcja ma również za zadanie
   * zapisać klucz do tablicy readCard i zwrócić PRAWDĘ jeśli ta operacja się powiedzie
   */
    if(! MFRC522.PICC_ReadCardSeroal()){
        return false;
    }
    if(! MFRC522.PICC_IsNewCardPresent()){
        return false;
    }
    Serial.print("Scanned ID from Card");
    for(uint8_t i=0; i<4; i++){
        readCard[i] = MFRC522.uid.uidByte[i];
        Serial.print(readCard[i],HEX);
    }
    Serial.println("");
    MFRC522.PICC_HaltA();
    return true;
}

bool compare_ID(byte *uid1,byte *uid2){
    /*
   * Funkcja compareUids posiada 2 wskaźniki jako argumenty
   * -uid1: pierwsza ilość bytów pierwszej karty
   * -uid2: druga ilość bytów drugiej karty\
   * Funkcja porównuje bajty w kartach. Jeśli, któryś z bajtów się nie zgadza funkcja zwraca FAŁSZ.
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
    pinMode(relay_module,HIGH);
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
}

void wait_For_Entry(){
    int distance = 0;
    int tempolary = 0;
    digitalWrite(TRIG_PIN,HIGH);
    delayMicrosecond(1000);
    digitalWrite(TRIG_PIN,LOW);
    distance = (pulseIn(ECHO_PIN,HIGH)/58);
    distance = tempolary;
    Serial.println("Czekam na wejście osoby");
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        digitalWrite(trig,HIGH);
        delayMicroseconds(1000);
        digitalWrite(trig,LOW);
        tempolary = (pulseIn(echo,HIGH))/58;
    }
    Serial.println("Czekam na przejście osoby");
    distance = tempolary
    delay(1000);
    while(distance + 2 > tempolary or distance - 2 > tempolary){
        digitalWrite(trig,HIGH);
        delayMicroseconds(1000);
        digitalWrite(trig,LOW);
        tempolary = (pulseIn(echo,HIGH))/58;
    }
    delay(1000);
}
