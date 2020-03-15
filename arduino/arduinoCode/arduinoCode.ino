#include "DHT.h"

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

#include "SD.h"
#include "SPI.h"

#define DHTPIN 2

#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)

#define CSpin 4

// ======================================================== BMP280 ==================================================
Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);


// ======================================================== DHT11 ==================================================
#define DHTTYPE DHT11   // DHT 11


// pin 1 (izquierda del sensor) a +5V
// pin 2 del sensor a cualquier DHTPIN
// pin 4 (derecha del sensor) a GROUND
// resistencia de 10k del pin 2 (data) a pin 1 (power) del sensor

// inicialización del sensor
DHT dht(DHTPIN, DHTTYPE);


// ======================================================== SD CARD ==================================================
//const int CSpin = 53;

String dataString = ""; // holds the data to be written to the SD card
float sensorReading1 = 0.00; // value read from your first sensor
float sensorReading2 = 1.00; // value read from your second sensor
float sensorReading3 = 0.00; // value read from your third sensor
File sensorData;


void setup() {

  Serial.begin(9600);
  Serial.println("Medicion de variables para el clima");

  // ======================================================== DHT11 SETUP ==================================================
  Serial.println("Inicializando DHT11");
  dht.begin();

  // ======================================================== BMP280 SETUP ==================================================
  Serial.println("Inicializando BMP280");
  if (!bmp.begin()) {
    Serial.println(F("NO SE HA ENCONTRADO SENSOR BMP280"));
    while (1);
  }

  /* Default settings from datasheet. */
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

  // ======================================================== SD CARD SETUP ==================================================
  Serial.println("Inicializando tarjeta SD");
  pinMode(CSpin, OUTPUT);
  if (!SD.begin(CSpin)) {
    Serial.println("No se leyo tarjeta SD");
    // don't do anything more:
    return;
  }
  Serial.println("SD INICIALIZADA");


}

void loop() {

  Serial.println("************************************");
  Serial.print("Temperatura de DHT11: ");

  Serial.print(getTemp("c"));

  Serial.print(" *C ");
  Serial.print(getTemp("f"));
  Serial.println (" *F");

  Serial.println("************************************");

  Serial.print("Indice de calor: ");
  Serial.print(getTemp("hic"));
  Serial.print(" *C ");
  Serial.print(getTemp("hif"));
  Serial.println(" *F");
  Serial.print(getTemp("k"));
  Serial.println(" *K");

  Serial.println("************************************");

  Serial.print("Humedad: ");
  Serial.print(getTemp("h"));
  Serial.println(" % ");

  Serial.println("************************************");

  Serial.print(F("Temperatura de BMP280 = "));
  Serial.print(bmp.readTemperature());
  Serial.println(" *C");

  Serial.print(F("Presión = "));
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");

  Serial.print(F("Altitud aprox = "));
  Serial.print(bmp.readAltitude(1013.25)); /* AJUSTAR! */
  Serial.println(" m");

    Serial.println("************************************");
// ======================================================== SD CARD WRITING INICIO ==================================================
  dataString = String(sensorReading1) + "," + String(sensorReading2) + "," + String(sensorReading3); // convert to CSV
  saveData(); // save to SD card
// ======================================================== SD CARD WRITING END ==================================================

  Serial.println();
  delay(10000);

}


float getTemp(String req)
{

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  // Compute heat index in Kelvin
  float k = t + 273.15;
  if (req == "c") {
    return t;//return Cilsus
  } else if (req == "f") {
    return f;// return Fahrenheit
  } else if (req == "h") {
    return h;// return humidity
  } else if (req == "hif") {
    return hif;// return heat index in Fahrenheit
  } else if (req == "hic") {
    return hic;// return heat index in Cilsus
  } else if (req == "k") {
    return k;// return temprature in Kelvin
  } else {
    return 0.000;// if no reqest found, retun 0.000
  }

}

void saveData() {
  if (SD.exists("data.csv")) { // chequear que la tarjeta exista
    // append new data file
    sensorData = SD.open("data.csv", FILE_WRITE);
    if (sensorData) {
      sensorData.println(dataString);
      sensorData.close(); // cerrar el archivo
    }
  }
  else {
    Serial.println("Error escribiendo el archivo");
  }
}



// ======================================================== SIDE NOTES ==================================================

/*
   getTemp(String req)
   returns the temprature related parameters
   req is string request
   This code can display temprature in:
   getTemp("c") is used to get Celsius
   getTemp("f") is used to get fahrenheit
   getTemp("k") is used for Kelvin
   getTemp("hif") is used to get fahrenheit
   getTemp("hic") is used to get Celsius
   getTemp("f") is used to get humidity
*/
