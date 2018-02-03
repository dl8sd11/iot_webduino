var kitchenID = '10yegA8Q';
var ButtonPort = 4;

function makeRecipe(){
  getRecipe(function(data){
    $('#arecipe').attr("href",data);
    console.log("recipe updated");
  });
}
boardReady({board: 'Smart', device: kitchenID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("kitchen connected");
  button = getButton(board, ButtonPort);
  button.on("released", function(){
    //console.log("Pressed");
    $('#kitchen').show();
    makeRecipe();
  });
  button.on("pressed",function(){
    $('#kitchen').hide();
    //console.log("released");
  });
});
makeRecipe();
