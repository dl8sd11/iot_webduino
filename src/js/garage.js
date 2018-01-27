
var garageID = '10Q84e8Q';
var ButtonPort = 4;
boardReady({board: 'Smart', device: garageID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("garage connected");
  button = getButton(board, ButtonPort);
  button.on("pressed", function(){
    console.log("Pressed");
    $('#garage').show();
  });
  button.on("released",function(){
    $('#garage').hide();
    console.log("released");
  });
});
