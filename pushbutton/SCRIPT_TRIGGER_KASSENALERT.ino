#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


// enter wlan ssid and password here
const char* ssid = "";
const char* password = "";

int button = 2; // push button is connected
int temp = 0;    // temporary variable for reading the button pin status

void setup () {

  pinMode(button, INPUT); // declare push button as input

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {

    delay(100);
    Serial.print("Connecting..");

  }

}

void loop() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

    temp = digitalRead(button);
    if (temp == HIGH) {

      Serial.println("Kassenöffnung Triggern");

      HTTPClient http;  //Declare an object of class HTTPClient
      // Request
      http.begin("https://hhz-ucc.de/api/v1/kassenbutton/attributes?UseCase=Kasse"); // Ticket Endpoint
      http.POST("{}"); // Post request to server

      //Response
      String payload = http.getString();
      int httpCode = http.GET();  //Send the request
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);
      Serial.println(httpCode);
      if (httpCode == HTTP_CODE_OK) {
        const String& payload = http.getString();
        Serial.println("received payload:\n<<");
        Serial.println(payload);
        Serial.println(">>");
      }

      http.end();
    }
    
    // stay in sleep mode until the pushbutton button is clicked
    ESP.deepSleep(30e6);
  }
}
