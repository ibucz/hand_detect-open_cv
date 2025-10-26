#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize the LCD (change 0x27 to the correct address if needed)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // Initialize the LCD
  lcd.begin(16, 2);
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n'); // Read until newline character
    lcd.clear();                  // Clear previous message
    lcd.setCursor(0, 0);         // Set cursor to the first column of the first row
    lcd.print(message);           // Print the new message
  }
}