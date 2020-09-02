#include <BluetoothSerial.h>
#include <HardwareSerial.h>
HardwareSerial MVIN(1);

String x = "";//Charcollector for parseSerial 
String val = "0";
BluetoothSerial SerialBT;

int analogpin = 36 ;
int bend = 0 ;

void setup() {
  Serial.begin(38400);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  MVIN.begin(38400, SERIAL_8N1, 16, 17);
  Serial.setTimeout(50);
  delay(50);
   
}

void loop() {

   while (MVIN.available() )  {
  String killme = "?";
 
char c =  MVIN.read();
//int num = 10;  
    //for i in range(num):
   String(byteFS) = String(c);
    //  Serial.print("I received: ");
  //    Serial.println(byteFS);
                   
     if (killme == byteFS)  {
      int bend = analogRead(36);  // read the input pin
      float temp = analogRead(39);  // read the input pin
      String Temp = String(temp);
      String val = String(bend);
      String wal = String( "Bend="  + val );
      String memp = String( "Temp=" + Temp );
      val = ( wal + "," + memp + ",");
      x = (val + x + ",");
      Serial.println(x);
      SerialBT.println(x);
     
  //
        //
    
  // Serial.println('\r','\n');
       x = "";//Charcollector for parseSerial 
  delay(10);
    }
    if (byteFS != "?"){
     x += byteFS;
   }  
   }
    }
