const URL = "http://localhost:5000";
// const URL = "https://bank-queue-socket-server.herokuapp.com";
const currentTimeComponent = $("#currentTimeComponent");
const queueContainer = $("#queueContainer");
const queueLengthContainer = $("#queueLengthContainer");
const lChart = document.getElementById("lChart");
var intervals = [];
var queue = [];
var chartData = [];
