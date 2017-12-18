// assign pin num
int right_pin = 6;
int left_pin = 7;
int forward_pin = 10;
int reverse_pin = 9;

// duration for output
int time = 50;

void setup() {
  pinMode(right_pin, OUTPUT);
  pinMode(left_pin, OUTPUT);
  pinMode(forward_pin, OUTPUT);
  pinMode(reverse_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    command = Serial.readString();
    if(command.equals("STOP")){
        reset();
        break;
    } else if(command.equals("FORWARD")){
        forward(time);
        break;
    } else if(command.equals("BACK")){
        reverse(time);
        break;
    } else if(command.equals("RIGHT")){
        right(time);
        break;
    } else if(command.equals("LEFT")){
        left(time);
        break;
    } else if(command.equals("F_RIGHT")){
        forward_right(time);
        break;
    } else if(command.equals("F_LEFT")){
        forward_left(time);
        break;
    } else if(command.equals("R_RIGHT")){
        reverse_right(time);
        break;
    } else if(command.equals("R_LEFT")){
        reverse_left(time);
        break;
    } else {
        Serial.println(command)
    }
  } else {
    reset();
  }
}

void right(int time){
  digitalWrite(right_pin, LOW);
  delay(time);
}

void left(int time){
  digitalWrite(left_pin, LOW);
  delay(time);
}

void full_right(){
  digitalWrite(forward_pin, LOW);
  digitalWrite(right_pin, LOW);
  delay(3000);
}

void full_left(){
  digitalWrite(forward_pin, LOW);
  digitalWrite(left_pin, LOW);
  delay(3000);
}

void forward(int time){
  digitalWrite(forward_pin, LOW);
  delay(time);
}

void reverse(int time){
  digitalWrite(reverse_pin, LOW);
  delay(time);
}

void forward_right(int time){
  digitalWrite(forward_pin, LOW);
  digitalWrite(right_pin, LOW);
  delay(time);
}

void reverse_right(int time){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(right_pin, LOW);
  delay(time);
}

void forward_left(int time){
  digitalWrite(forward_pin, LOW);
  digitalWrite(left_pin, LOW);
  delay(time);
}

void reverse_left(int time){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(left_pin, LOW);
  delay(time);
}

void reset(){
  digitalWrite(right_pin, HIGH);
  digitalWrite(left_pin, HIGH);
  digitalWrite(forward_pin, HIGH);
  digitalWrite(reverse_pin, HIGH);
}
