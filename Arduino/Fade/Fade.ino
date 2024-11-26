// This is meant as a basic test for the Mosfets dimming that are controlling led light strips
// Can see the different between having a common ground with the boat vs the Arduino running on a floating ground yields more flickering
// Otherwise just use basic blink example to test the Mosfets
int mosfetPin = 3;    // Mosfet is connected to digital pin 3
bool faidIn = true;
void setup() { }

void loop() {
    for (int fadeValue = 0; fadeValue <= 255 and fadeValue>=0; faidIn ? fadeValue += 5 : fadeValue -= 5) {
        analogWrite(mosfetPin, fadeValue);
        delay(30); //30 milliseconds
        } //end for
        faidIn=!faidIn;
    } //end loop