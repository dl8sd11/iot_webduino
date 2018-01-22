// function makeGarage(callback) {
//
//   callback();
// }
var garageID = '10Q84e8Q';
var ButtonPort = 4;
boardReady({board: 'Smart', device: garageID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("garage connected");
  button = getButton(board, ButtonPort);
  button.on("released", function(){
    console.log("Pressed");
    $('#garage').show();
  });
  button.on("pressed",function(){
    $('#garage').hide();
    console.log("released");
  });
});
