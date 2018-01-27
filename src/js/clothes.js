var collectStatus = 0;
var collectTime = 5000;
var collectID = '10dKR78Q';
onoffMotor(cmd){
  var motorOnOff = getLed(board, 12);
  if (cmd=='on') {
    motorOnOff.on();
  } else {
    motorOnOff.off();
  }
}
setMotorDir(cmd,callback){
  var motorDir = getLed(board,11);
  if (cmd=='left') {
    motorDir.on();
  } else {
    motorDir.off();
  }
  callback();
}
boardReady({board: 'Smart', device: 'collectID', transport: 'mqtt'}, function (board) {
  board.samplingInterval = 50;
  var led;
  led = getLed(board, 12);
  led.off();
  setInterval(function(){
    getCollectClothes(function(data){
      if (collectStatus&&!data) {
        setMotorDir('left',function(){
          onoffMotor('on');
          setTimeOut(onoffMotor('off'),collectTime);
        });
      } else if (!collectStatus&&data) {
        setMotorDir('right',function(){
          onoffMotor('on');
          setTimeOut(onoffMotor('off'),collectTime);
        });
      }
    });
  },10000);
});
