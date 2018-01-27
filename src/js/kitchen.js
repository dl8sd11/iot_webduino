var kitchenID = '10yegA8Q';
var ButtonPort = 4;
function makeRecipe(){
  getRecipe(function(data){
    for(i=0;i<data.length;i++) {
      $('#dishes').append(data[i]);
    }
    // $('#dishName').html(data[0]);
    // $('#serves').html(data[1]);
    // let i;
    // for(i=3;i<data.length;i++) {
    //   if (data[i]=="Instructions:") break;
    //   $('#recipeIngredients').append("<li>"+data[i]+"</li>");
    // }
    // for(;i<data.length;i++){
    //   $('#recipeSteps').append("<li>"+data[i]+"</li>");
    // }
  });
}
boardReady({board: 'Smart', device: kitchenID, transport: 'mqtt'}, function (board) {
  board.systemReset();
  board.samplingInterval = 50;
  console.log("kitchen connected");
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
