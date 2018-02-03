var outdoorID = '10VxwaJy';
var ButtonPort = 4;
function makeOutdoor(){
  getOutdoorInfo(function(data){
    $('#pmStat').html(data.pm+"μg／m³");
    if (parseInt(data.pm)<15) {
      $('#pmLevel').html("空氣品質正常");
      $('#maskimg').attr("src","./pic/nmask.jpg");
    } else {
      $('#pmLevel').html("PM2.5濃度過高出門記得攜帶口罩");
      $('#maskimg').attr("src","./pic/mask.jpeg");
    }
    $('#rainStat').html("降雨機率"+data.rain+"%");
    if (data.rain>=50) {
      $('#umbimg').attr("src","./pic/unb.jpg");
    } else {
      $('#umbimg').attr("src","./pic/sun.png");
    }
  });
}
boardReady({board: 'Smart', device: '10VxwaJy', transport: 'mqtt'}, function (board) {
  board.samplingInterval = 50;
  console.log("connected outdoor")
  button = getButton(board, 4);

  button.on("released", function(){
    console.log("pressed");
    $('#outdoor').show();
  });
  button.on("pressed",function(){
    console.log("released");
    $('#outdoor').hide();
  });
});
// boardReady({board: 'Smart', device: outdoorID, transport: 'mqtt'}, async function (board) {
//   board.systemReset();
//   board.samplingInterval = 50;
//   console.log("outdoor connected");
//   button = getPin(board, ButtonPort);
//   button.setMode(0);
//   while(1) {
//     let a = await button.read();
//     console.log(a);
//     if (a==0) {
//       onCnt++;
//       offCnt = 0;
//       if (onCnt>10&&btnStat==0) {
//         console.log("btnOn");
//         makeOutdoor();
//         $('#outdoor').show();
//         btnStat=1;
//       }
//     } else {
//       offCnt++;
//       onCnt=0;
//       if (offCnt>10&&btnStat==1) {
//         console.log("btnOff");
//         $('#outdoor').hide();
//         btnStat=0;
//       }
//     }
//   }
//
// });
  makeOutdoor();
console.log("outdoor.js");
