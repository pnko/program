void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(9, map(analogRead(A0),0,1023,0,255));
}
