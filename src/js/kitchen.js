var garageID = '10Q84jXQ';
var ButtonPort = 4;
function makeRecipe(){
  getRecipe(function(data){
    $('#dishName').html(data[0]);
    $('#serves').html(data[1]);
    let i;
    for(i=3;i<data.length;i++) {
      if (data[i]=="Instructions:") break;
      $('#recipeIngredients').append("<li>"+data[i]+"</li>");
    }
    for(;i<data.length;i++){
      $('#recipeSteps').append("<li>"+data[i]+"</li>");
    }
  });
}
boardReady({board: 'Smart', device: garageID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("garage connected");
  button = getButton(board, ButtonPort);
  button.on("released", function(){
    console.log("Pressed");
    $('#kitchen').show();
    makeRecipe();
  });
  button.on("pressed",function(){
    $('#kitchen').hide();
    console.log("released");
  });
});
