#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h> // https://github.com/maniacbug/RF24
#include <Servo.h>

 // Создаём объект сервопривода servo1.
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
 // Также определим постоянный аналоговый входной пин для измерения положения датчика изгиба.
const int flexpin1 = 0;
const int flexpin2 = 1;
const int flexpin3 = 2;
const int flexpin4 = 3;
const int flexpin5 = 4;

const uint64_t pipe = 0xF0F1F2F3F4LL; // индитификатор передачи, "труба"
 
RF24 radio(9, 10); // CE, CSN
 

void setup(){
  Serial.begin(9600);
  
  servo1.attach(2);
  servo2.attach(3);
  //servo3.attach(4);
  //servo4.attach(5);
  //servo5.attach(6);
  
  radio.begin();
  delay(2);
  radio.setChannel(9); // канал (0-127)
    
      // скорость, RF24_250KBPS, RF24_1MBPS или RF24_2MBPS
      // RF24_250KBPS на nRF24L01 (без +) неработает.
      // меньше скорость, выше чувствительность приемника.
  radio.setDataRate(RF24_1MBPS); 
   
      // мощьность передатчика, RF24_PA_MIN=-18dBm, RF24_PA_LOW=-12dBm, RF24_PA_MED=-6dBM,
  radio.setPALevel(RF24_PA_HIGH);   

  radio.openReadingPipe(1,pipe); // открываем первую трубу с индитификатором "pipe"
  radio.startListening(); // включаем приемник, начинаем слушать трубу
  
} 


void loop()   
{
  int servoposition1, servoposition2, servoposition3, servoposition4, servoposition5;
  int sendData[5];
  
  if (radio.available()){ // проверяем не пришло ли чего в буфер.
    radio.read(&sendData, sizeof(sendData)); // читаем данные и указываем сколько байт читать
    
    servoposition1 = sendData[0]; // читаем значение
    servoposition2 = sendData[1]; // читаем значение
    servoposition3 = sendData[2]; // читаем значение
    servoposition4 = sendData[3]; // читаем значение
    servoposition5 = sendData[4]; // читаем значение
    
    //servo1.write(servoposition1);
    //servo2.write(servoposition2);
    //servo3.write(servoposition3);
    //servo4.write(servoposition4);
    //servo5.write(servoposition5);
    Serial.print("X:    ");
    Serial.print(servoposition1);
    Serial.print("    Y:    ");
    Serial.println(servoposition2);
  }else{
    //Serial.println("No data");
  }
  //Serial.print("data: ");
  //Serial.println(data);
  
//  delay(1000);
} 

