var api_route = "http://127.0.0.1:5000/IOT/api/v1.0/"
var serverStatus_b = document.getElementById("serverStatus");
var connection = false;
function checkConnection(){
  $.get(api_route+"status",function(){
    //onsole.log("requesting for server status...");
  }).done(function(data){
    serverStatus_b.innerHTML = data.status;
    connection = true;
  }).fail(function(){
    serverStatus_b.innerHTML = "disconnected";
    connection = false;
  });
}
setInterval(checkConnection,5000);
$(document).ready(function (){
  checkConnection();
});
function getCalendar(callback){
  $.get(api_route+"Calendar").done(function(data){
    callback(data);
  }).fail(function(){
    callback("fail")
  });
}
function getTemperature(callback){
  $.get(api_route+"Temperature").done(function(data){
    callback(data.temperature);
  }).fail(function(){
    callback("failed");
  });
}
