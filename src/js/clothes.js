var collectStatus = 0;
var collectTime = 5000;
var INA;
var INB;
var collectID = '10dKR78Q';
function gather(callback) {
  INA.write(1);
  INB.write(0);
  callback();
}
function dry(callback) {
  INA.write(0);
  INB.write(1);
  callback();
}
boardReady({board: 'Smart', device: '10dKR78Q', transport: 'mqtt'}, function (board) {
  console.log("clotheshorse connected");
  board.samplingInterval = 50;
  INA = getPin(board, 13);
  INB = getPin(board, 12);
  INA.setMode(1);
  INB.setMode(1);

  setInterval(async function () {
    getCollectClothes(async function(data){
      if (data=='1'&&collectStatus==0) {
        INA.write(1);
        INB.write(0);
        await delay(5);
        INA.write(0);
        INB.write(0);
        collectStatus = 1;
      } else if (data=='0'&&collectStatus==1) {
        INA.write(0);
        INB.write(1);
        await delay(5);
        INA.write(0);
        INB.write(0);
        collectStatus = 0;
      }
    });
  }, 1000 * 10);

});


console.log("loaded clothes.js")
