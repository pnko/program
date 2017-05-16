
byte digits[10][7] =
{
  {0,0,0,0,0,0,1},
  {1,0,0,1,1,1,1},
  {0,0,1,0,0,1,0},
  {0,0,0,0,1,1,0},
  {1,0,0,1,1,0,0},
  {0,1,0,0,1,0,0},
  {0,1,0,0,0,0,0},
  {0,0,0,1,1,1,1},
  {0,0,0,0,0,0,0},
  {0,0,0,1,1,0,0},
};
void setup() {
  // put your setup code here, to run once:
  for(int i=2; i<10; i++) {
    pinMode(i, OUTPUT);
  }
  digitalWrite(9, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<10; i++){
    delay(1000);
    displayDigit(i);
  }
}

void displayDigit(int num){
  int pin = 2;
  int csd ;
  for(int i=0; i<7; i++){
    if(digits[num][i] == 0){
      csd = 1;
    }else{
      csd = 0;
    }
    digitalWrite(pin+i, csd);
  }
}

