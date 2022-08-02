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
  handleClientsTimeEllapsed();
}, 1000);

// setInterval(() => {
//   handleClientsTimeEllapsed();
// }, 50);

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
          <div class="waiting-time">WT 00:00:00</div>
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

const removeUserFromQueue = () => {
  queue.splice(0, 1);
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
        <div class="waiting-time ${specifyColorOnTheFly(
          queue[i]
        )}" id="wt${i}">${calculateTimeOnTheFly(queue[i])}</div>
      </div>
    </div>
    `;
  }
  queueContainer.html(contents);
  updateQueueLength();
  addFreeChairs();
};

const specifyColorOnTheFly = (item) => {
  const startTime = new Date(item.joinedTimeAndDate);
  const endTime = new Date();
  const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
  const formatted = new Date(seconds * 1000).toISOString().slice(11, 19);
  const splted = formatted.split(":");
  return Number(splted[1]) >= 1 ? "text-danger" : "";
};

const calculateTimeOnTheFly = (item) => {
  const startTime = new Date(item.joinedTimeAndDate);
  const endTime = new Date();
  const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
  const formatted = new Date(seconds * 1000).toISOString().slice(11, 19);
  return "WT " + formatted;
};

const handleClientsTimeEllapsed = () => {
  for (let i = 0; i < queue.length; i++) {
    const startTime = new Date(queue[i].joinedTimeAndDate);
    const endTime = new Date();
    const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
    const formatted = new Date(seconds * 1000).toISOString().slice(11, 19);
    const formatted2 = new Date(seconds * 1000);
    const splted = formatted.split(":");
    if (Number(splted[1]) >= 1) {
      $("#wt" + i).addClass("text-danger");
    } else {
      $("#wt" + i).removeClass("text-danger");
    }
    $("#wt" + i).html("WT " + formatted);
  }
};

$(document).ready(function () {
  loadQueue();
  $.ajax({
    url: "/api/getclients",
    method: "GET",
    success: (data) => {
      queue = data;
      loadQueue();
    },
  });
});
