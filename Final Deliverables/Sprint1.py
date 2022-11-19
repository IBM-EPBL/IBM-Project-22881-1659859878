#include
<ESP32Se
rvo.h> #include
<LiquidC rystal_I 2C.h>
LiquidCrystal_I2C LCD = LiquidCrystal_I2C(0x27, 16, 2); Servo servo;
int trigPin1= 2

digitalWrite(trigPin2, LOW); delayMicroseconds(2); digitalWrite(trigPin2, HIGH); delayMicroseconds(10); digitalWrite(trigPin2, LOW); duration2 = pulseIn(echoPin2, HIGH); distance2= duration2*0.034/2; Serial.println("The lid is closed");

}
LCD.setCursor(0,1); LCD.print("Fill Status: ");

if(distance2>300 && distance2<=400){ LCD.setCursor(12,1); LCD.print("25% ");
Serial.println("Bin status:25%");
}
else if(distance2 > 200 && distance2<= 299){ LCD.setCursor(12,1);
LCD.print("50%");
Serial.println("Bin status:50%");
}
else if(distance2 >50 && distance2<=199){ LCD.setCursor(12,1);
LCD.print("75%");
Serial.println("Bin status:75%");
}
else{
LCD.setCursor(12,1); LCD.print("100%");
Serial.println("Bin status:100%");
}
if(distance1<=50){ servo.write(90);
}
else{
servo.write(0);
}
}
