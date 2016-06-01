#include <nRF24L01.h>
#include <RF24.h> // https://github.com/maniacbug/RF24

#include <Servo.h>

Servo mouth;
int power = 23;
int redR = 2; //0
int greenR = 3; //1
int blueR = 4;
int redL = 5; 
int greenL = 6; 
int blueL = 7;
int XHeadPin = 12;
int YHeadPin = 11;

int servopositionX, servopositionY, servopositionZ, servoposition4, servoposition5;
const uint64_t pipe = 0xF0F1F2F3F4LL; // индитификатор передачи, "труба"
 
RF24 radio(9, 10); // CE, CSN
int tempX = 0;
int tempY = 0;
void setup(){
  mouth.attach(45);
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
  
  delay(1000);
  Serial.begin(115200);
  Serial3.begin(9600);
  pinMode(redR, OUTPUT);
  pinMode(greenR, OUTPUT);
  pinMode(blueR, OUTPUT);
  
  pinMode(power, OUTPUT);
  pinMode(redL, OUTPUT);
  pinMode(greenL, OUTPUT);
  pinMode(blueL, OUTPUT);
  
  
  analogWrite(redR, 0);
  analogWrite(greenR, 0);
  analogWrite(blueR, 0);
  
  analogWrite(redL, 0);
  analogWrite(greenL, 0);
  analogWrite(blueL, 0);
  
  

}
int pozXmin = 10;
int pozXMax  =70;

int pozYmin = 60;
int pozYMax = 150;
void loop(){
  int sendData[5];
  if (radio.available()){ // проверяем не пришло ли чего в буфер.
    radio.read(&sendData, sizeof(sendData)); // читаем данные и указываем сколько байт читать
    
    servopositionY = sendData[0]; // читаем значение
    servopositionX = sendData[1]; // читаем значение
    servopositionZ = sendData[2]; // читаем значение
    servoposition4 = sendData[3]; // читаем значение
    servoposition5 = sendData[4]; // читаем значение
    int posX = map(servopositionX, pozXmin, pozXMax, 600, 2500);
    //int posX = map(servopositionX, 0, 180, 2500, 600);
    int posY = map(servopositionY, pozYmin, pozYMax, 2500, 600);//15-130 - 0-160
    //Serial.print("posX: "); Serial.println(servopositionX);
    //Serial.print(" posY: "); Serial.print(servopositionY);
    //Serial.print(" posZ: "); Serial.println(servopositionZ);
    //if(tempX != servopositionX){
    if(abs(tempX - servopositionX)>=2){
      Serial3.println("#"+String(XHeadPin)+"P"+String(posX)+"T5");
      tempX = servopositionX;
    } 
    //if(tempY != servopositionY){
    if(abs(tempY - servopositionY)>=2){
      
      Serial3.println("#"+String(YHeadPin)+"P"+String(posY)+"T5");
      tempY = servopositionY;
    }
    
    
    
    
    //servo1.write(servoposition1);
    //servo2.write(servoposition2);
    //servo3.write(servoposition3);
    //servo4.write(servoposition4);
    //servo5.write(servoposition5);
    /*
    Serial.print("X:    ");
    Serial.print(servoposition1);
    Serial.print("    Y:    ");
    Serial.println(servoposition2);
    */
  }
  //Serial.flush(); 
  
  if(Serial.available()){
    
    String line = readlinePort();
    switch(line[0]){
      
      case 'M':{
        int indexBolshe = line.indexOf('>');
        int sercoPos = line.substring(indexBolshe+1).toInt();
        mouth.write(sercoPos);
        //Serial.println("#"+String(pinNamber)+"P"+String(pos)+"T50");
        break;
      }
      case 'S':{
        int indexD = line.indexOf('D');
        int indexBolshe = line.indexOf('>');
        int pinNamber = line.substring(indexD+1, indexBolshe).toInt();
        int sercoPos = line.substring(indexBolshe+1).toInt();
        int pos = map(sercoPos, 0, 180, 600, 2500);
        Serial3.println("#"+String(pinNamber)+"P"+String(pos)+"T0");
        //Serial.println("#"+String(pinNamber)+"P"+String(pos)+"T50");
        break;
      }
      case 'L':{
        int indexD = line.indexOf('D');
        int indexBolshe = line.indexOf('>');
        int pinNamber = line.substring(indexD+1, indexBolshe).toInt();
        int value = line.substring(indexBolshe+1).toInt();
        //value = map(value, 0, 255, 0, 1023);
        switch(pinNamber){
          case 1:
             analogWrite(redL, value);
             break;
          case 2:
             analogWrite(greenL, value);
             break;
          case 3:
             analogWrite(blueL, value);
             break;
          case 4:{
            analogWrite(redL, value);
            analogWrite(greenL, value);
            analogWrite(blueL, value);
          }
        }
        break; 
      }
      case 'R':{
        int indexD = line.indexOf('D');
        int indexBolshe = line.indexOf('>');
        int pinNamber = line.substring(indexD+1, indexBolshe).toInt();
        int value = line.substring(indexBolshe+1).toInt();
        //value = map(value, 0, 255, 0, 1023);
        switch(pinNamber){
          case 1:
             analogWrite(redR, value);
             break;
          case 2:
             analogWrite(greenR, value);
             break;
          case 3:
             analogWrite(blueR, value);
             break;
          case 4:{
            analogWrite(redR, value);
            analogWrite(greenR, value);
            analogWrite(blueR, value);
            break;
          }
             
        }
        break;
      }
      case 'A':{
        int indexD = line.indexOf('D');
        int indexBolshe = line.indexOf('>');
        int pinNamber = line.substring(indexD+1, indexBolshe).toInt();
        int value = line.substring(indexBolshe+1).toInt();
        //value = map(value, 0, 255, 0, 1023);
        analogWrite(redL, value);
        analogWrite(greenL, value);
        analogWrite(blueL, value);
        analogWrite(redR, value);
        analogWrite(greenR, value);
        analogWrite(blueR, value);
        break;
      }
      case 'D':{
        //DR255G255B255
        int indexR = line.indexOf('R');
        int indexG = line.indexOf('G');
        int indexB = line.indexOf('B');
        int valueR = line.substring(indexR+1, indexG).toInt();
        int valueG = line.substring(indexG+1, indexB).toInt();
        int valueB = line.substring(indexB+1).toInt();
        //value = map(value, 0, 255, 0, 1023);
        analogWrite(redL, valueR);
        analogWrite(greenL, valueG);
        analogWrite(blueL, valueB);
        analogWrite(redR, valueR);
        analogWrite(greenR, valueG);
        analogWrite(blueR, valueB);
        break;
      }
    
    case 'Q':{
        switch(line[1]){
            case 'X':{
              //QXL10B70R1
              int indexMin = line.indexOf('L');
              int indexMax = line.indexOf('B');
              int indexReverse = line.indexOf('R');
              int valueMinX = line.substring(indexMin+1, indexMax).toInt();
              int valueMaxX = line.substring(indexMax+1, indexReverse).toInt();
              int valueReverseX = line.substring(indexReverse+1).toInt();
              pozXmin = valueMinX;
              pozXMax = valueMaxX;
              break;
            }
            case 'Y':{
              //QYL10B70R1
              int indexMin = line.indexOf('L');
              int indexMax = line.indexOf('B');
              int indexReverse = line.indexOf('R');
              int valueMinY = line.substring(indexMin+1, indexMax).toInt();
              int valueMaxY = line.substring(indexMax+1, indexReverse).toInt();
              int valueReverseX = line.substring(indexReverse+1).toInt();
              pozYmin = valueMinY;
              pozYMax = valueMaxY;
              break;
            }
      }
      break;
    }
    //Serial3.println(line);
  
    }
  }
  /**
  if(Serial.overflow()){
        Serial.end();
        delay(15);
        Serial.begin(115200);
  }**/
  //Serial3.flush();
}

String readlinePort(){
  String command_pi = "";
  while (1){
    if(Serial.available( )){
      char buf = Serial.read();
      if(buf != '\n'){
        command_pi += buf;
      }else{
        return command_pi;
      }  
    }
  }
}
