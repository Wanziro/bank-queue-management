const handleCurrentTime = () => {
  const currentdate = new Date();
  currentTimeComponent.html(
    currentdate.getHours() +
      ":" +
      currentdate.getMinutes() +
      ":" +
      currentdate.getSeconds()
  );
};

//intervals
setInterval(() => {
  handleCurrentTime();
}, 1000);

const addFreeChairs = () => {
  let chs = "";
  const chairs = $(".user-blank");
  if (chairs.length < 3) {
    for (let i = 0; i < 6; i++) {
      chs += `
      <div class="col-md-2 mb-3">
        <div class="user-container user-blank">
          <div class="blank-image">&nbsp;</div>
          <div class="position">${queue.length + i + 1}</div>
          <div class="waiting-time">WT: 00:00:00</div>
        </div>
      </div>
      `;
    }
  }
  queueContainer.append(chs);
};

const updateQueueLength = () => {
  queueLengthContainer.html(queue.length);
};

const addUserToQueue = (user) => {
  queue.push(user);
  loadQueue();
};

const loadQueue = () => {
  queueContainer.html("");
  let contents = "";
  for (let i = 0; i < queue.length; i++) {
    contents += `
    <div class="col-md-2 mb-3">
      <div class="user-container">
        <img src="/static/images/p1.svg" style="width: 50px" />
        <div class="position">${i + 1}</div>
        <div class="waiting-time">WT: 00:05:10</div>
      </div>
    </div>
    `;
  }
  queueContainer.html(contents);
  updateQueueLength();
  addFreeChairs();
};

$(document).ready(function () {
  loadQueue();
});
