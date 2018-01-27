console.log("loaded wardrobe.js");
function makeWardrobe(callback) {
  getTemperature(function(data){
    $("#wardrobeTemp").html(data);
  });
  getCalendar(function(data){
    if (data=='fail') return;
    events = data.events;
    let calendar = document.getElementById("calendar");
    calendar.innerHTML="";
    for (var i=0,len=events.length;i<len;i++) {
      let nowEvent = events[i];
      let tmpLi = document.createElement("li");
      tmpLi.innerHTML = nowEvent.summary;
      calendar.append(tmpLi);
    }
  });
  callback();
}
var photocell;
var rgbled;
var wardrobeDoor = 0;
var wardrobeID = "10Q84jXQ";
boardReady({board: 'Smart', device: wardrobeID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("wardrobe connected");
  photocell = getPhotocell(board, 0);
  rgbled = getRGBLedCathode(board, 15, 12, 13);
  rgbled.setColor('#ff0000');
  photocell.on(function(val){
    photocell.detectedVal = val;
    if (val>0.05) {
      if (wardrobeDoor == 0) {
        wardrobeDoor = 1;
        makeWardrobe(function(){
          $("#wardrobe").show();
        });
      }

    }
    else {
      if (wardrobeDoor == 1)
        wardrobeDoor = 0;
        $("#wardrobe").hide();
    }
  });
});
