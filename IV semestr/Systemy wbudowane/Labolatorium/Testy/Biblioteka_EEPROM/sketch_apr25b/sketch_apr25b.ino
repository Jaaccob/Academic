#include <EEPROM.h>

byte masterCard[] = {0x13, 0x53, 0xC2, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  if (true) {
    Serial.println("EEPROM DUMP:");
    Serial.print("Cards count: ");
    Serial.println(EEPROM.read(0));
    for (int x = 1; x < EEPROM.length(); x++) {
      if ((x - 1) % 10 == 0) {
        Serial.print((x - 1) / 10);
        Serial.print(":\t\t");
      }
      Serial.print(EEPROM.read(x), HEX);
      if (x % 10 == 0) {
        Serial.println();
      } else {
        Serial.print("\t");
      }
    }
    Serial.println();
  }

  addToEEPROM(masterCard);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(EEPROM.read(0));
  Serial.println(EEPROM.length());
  delay(100);
}

bool addToEEPROM(byte * uid) {
  /*
   * Funkcja addToEEPROM posiada 1 argument
   * -uid: wskaźnik na tablicę, która przechowuje klucz karty dostępu
   * Funkcja ma za zadanie dodać kartę do pamięci EEPROM
   */
  int cardsLimit = (EEPROM.length() - 1) / 10;        //Ilość kart w pamięci eeprom
  byte cardsCount = EEPROM.read(0);                   //
  if(cardsCount >= cardsLimit) {
    if(true) Serial.println("Failed adding card to EEPROM. Out of memory.");
    return false;
  }

  EEPROM.write(0, cardsCount + 1);                    //Dodanie kolejnej karty (ilości) do pamięci
  for(byte x = 0; x < 10; x++) {                      //Zapisywanie klucza karty do pamięci EEPROM
    EEPROM.write(1 + (10 * cardsCount) + x, uid[x]);
  }
  if(true) Serial.println("Card added to EEPROM");
  return true;
}
