#define HC12SetPin 40

void setup() {
  
  Serial3.begin(9600);
  digitalWrite(HC12SetPin, HIGH); 
  // put your setup code here, to run once:

}

void loop() {
  byte key[16] = {0xAA,0xFA,0x03,0x14,0x01,0x03,0x75, 0xCA, 0xAA,0xFA,0x03,0x14,0x01,0x03,0x75, 0xCA};

  for (int kx = 0; kx < 16; kx ++) {
    Serial3.write(key[kx]);
    //Serial3.print((byte)hexk.data[kx], (HEX));
  }
  // put your main code here, to run repeatedly:

}
