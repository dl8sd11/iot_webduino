var outdoorID = '10VxwaJy';
var ButtonPort = 4;
function makeOutdoor(){
  getOutdoorInfo(function(data){
    $('#pmStat').html("pm2.5濃度: "+data.pm+"μg／m3");
    console.log(data.pm);
    if (parseInt(data.pm)<15) $('#pmLevel').html("空氣品質正常");
    else $('#pmLevel').html("PM濃度過高出門記得攜帶口罩");
    $('#rainStat').html("降雨機率"+data.rain);
  });
}
boardReady({board: 'Smart', device: outdoorID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("outdoor connected");
  button = getButton(board, ButtonPort);
  button.on("released", function(){
    $('#outdoor').show();
    makeOutdoor();
  });
  button.on("pressed",function(){
    $('#outdoor').hide();
  });
});
