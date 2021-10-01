webgazer.showVideoPreview(false).showPredictionPoints(false);

let var1 = 0;
function stop() {
  var1 = 1;
  console.log('var1은 1이다 stop~!');
}
function start() {
  var1 = 2;
  console.log('var1은 2이다 start~!');
}

webgazer
  .setGazeListener((data, timestamp) => {
    if (var1 == 1) {
      webgazer.pause();
    }
    if (var1 == 2) {
      console.log(data, new Date(timestamp).getTime());
    }
  })
  .begin()

function start1() {
    var1 = 3;
    console.log('테스트완료');
}