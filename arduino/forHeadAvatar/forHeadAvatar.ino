#include <Wire.h>
#include "Kalman.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h> // https://github.com/maniacbug/RF24
  
const uint64_t pipe = 0xF0F1F2F3F4LL; // индитификатор передачи, "труба"
 
RF24 radio(9, 10); // CE, CSN

Kalman kalmanX;
Kalman kalmanY;
uint8_t IMUAddress = 0x68;
/* IMU Data */
int16_t accX;
int16_t accY;
int16_t accZ;
int16_t tempRaw;
int16_t gyroX;
int16_t gyroY;
int16_t gyroZ;
double accXangle; // Angle calculate using the accelerometer
double accYangle;
double temp;
double gyroXangle = 180; // Angle calculate using the gyro
double gyroYangle = 180;
double compAngleX = 180; // Calculate the angle using a Kalman filter
double compAngleY = 180;
double kalAngleX; // Calculate the angle using a Kalman filter
double kalAngleY;
uint32_t timer;
void setup() {
  Wire.begin();
  //Serial.begin(9600);
  i2cWrite(0x6B,0x00); // Disable sleep mode      
  kalmanX.setAngle(180); // Set starting angle
  kalmanY.setAngle(180);
  timer = micros();
  
  radio.begin();
  delay(2);
  radio.setChannel(9); // канал (0-127)
    
      // скорость, RF24_250KBPS, RF24_1MBPS или RF24_2MBPS
      // RF24_250KBPS на nRF24L01 (без +) неработает.
      // меньше скорость, выше чувствительность приемника.
  radio.setDataRate(RF24_1MBPS); 
   
      // мощьность передатчика, RF24_PA_MIN=-18dBm, RF24_PA_LOW=-12dBm, RF24_PA_MED=-6dBM,
  radio.setPALevel(RF24_PA_HIGH);   

  radio.openWritingPipe(pipe); // открываем трубу на передачу.
  
}

int servoAngleX;
int servoAngleY;
void loop() {
  /* Update all the values */
  uint8_t* data = i2cRead(0x3B,14);
  accX = ((data[0] << 8) | data[1]);
  accY = ((data[2] << 8) | data[3]);
  accZ = ((data[4] << 8) | data[5]);
  tempRaw = ((data[6] << 8) | data[7]);
  gyroX = ((data[8] << 8) | data[9]);
  gyroY = ((data[10] << 8) | data[11]);
  gyroZ = ((data[12] << 8) | data[13]);
  /* Calculate the angls based on the different sensors and algorithm */
  accYangle = (atan2(accX,accZ)+PI)*RAD_TO_DEG;
  accXangle = (atan2(accY,accZ)+PI)*RAD_TO_DEG;  
  double gyroXrate = (double)gyroX/131.0;
  double gyroYrate = -((double)gyroY/131.0);
  gyroXangle += kalmanX.getRate()*((double)(micros()-timer)/1000000); // Calculate gyro angle using the unbiased rate
  gyroYangle += kalmanY.getRate()*((double)(micros()-timer)/1000000);
  kalAngleX = kalmanX.getAngle(accXangle, gyroXrate, (double)(micros()-timer)/1000000); // Calculate the angle using a Kalman filter
  kalAngleY = kalmanY.getAngle(accYangle, gyroYrate, (double)(micros()-timer)/1000000);
  
  /*
  Serial.println();
  Serial.print("X:");
  Serial.print(kalAngleX,0);
  Serial.print(" ");
  Serial.print("Y:");
  Serial.print(kalAngleY,0);
  Serial.println(" ");
  */
  int sendData[5];
  sendData[0] = (int)kalAngleX-90;
  sendData[1] = (int)kalAngleY-90;
  sendData[2] = 0;
  sendData[3] = 0;
  sendData[4] = 0;
  radio.write(&sendData, sizeof(sendData)); 
 //myservoX.write((int)kalAngleX-90);
 //myservoY.write((int)kalAngleY-90);
  // The accelerometer's maximum samples rate is 1kHz
  timer = micros();
}
void i2cWrite(uint8_t registerAddress, uint8_t data){
  Wire.beginTransmission(IMUAddress);
  Wire.write(registerAddress);
  Wire.write(data);
  Wire.endTransmission(); // Send stop
}
uint8_t* i2cRead(uint8_t registerAddress, uint8_t nbytes) {
  uint8_t data[nbytes];
  Wire.beginTransmission(IMUAddress);
  Wire.write(registerAddress);
  Wire.endTransmission(false); // Don't release the bus
  Wire.requestFrom(IMUAddress, nbytes); // Send a repeated start and then release the bus after reading
  for(uint8_t i = 0; i < nbytes; i++)
    data [i]= Wire.read();
  return data;
}
