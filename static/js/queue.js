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
      <div class="col col-md-2 col-sm-6 col-xs-6 mb-3">
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
    <div class="col col-md-2 col-sm-6 col-xs-6 mb-3">
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
const getTotalWt = (joined, leave) => {
  let leaveDate;
  if (leave != "-") {
    leaveDate = new Date(leave);
  } else {
    leaveDate = new Date();
  }
  const joinedDate = new Date(joined);
  const diffMs = leaveDate - joinedDate;
  const diffDays = Math.floor(diffMs / 86400000); // days
  const diffHrs = Math.floor((diffMs % 86400000) / 3600000); // hours
  const diffMins = Math.round(((diffMs % 86400000) % 3600000) / 60000);
  return diffMins;
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

const lcData = {
  labels: [],
  datasets: [
    {
      label: "Queue Statistics (X:client,Y:min)",
      backgroundColor: "#ffc107",
      borderColor: "#FFF",
      titleColor: "#FFF",
      borderWidth: 2,
      data: [0, 0, 0],
    },
  ],
};
const lcConfig = {
  type: "bar",
  data: lcData,
  options: {
    plugins: {
      tooltip: {
        callbacks: {
          footer: (tooltipItem) =>
            "Waiting Time: " + tooltipItem[0].raw.y + "Min",
        },
      },
    },
  },
};
const lChartObj = new Chart(lChart, lcConfig);

const handleLcChart = () => {
  const wts = [];
  const labes = [];
  if (chartData.length > 0) {
    for (let i = 0; i < chartData.length; i++) {
      const wt = getTotalWt(
        chartData[i].joinedTimeAndDate,
        chartData[i].leaveTimeAndDate
      );
      if (wts.indexOf(wt) == -1) wts.push({ x: "C", y: wt });
      labes.push("C");
    }
  } else {
    lcData.labels = [];
  }
  lcData.labels = labes;
  lcData.datasets[0].data = wts;
  lChartObj.update();
};
const getChartData = () => {
  $.ajax({
    url: "/api/chart",
    method: "GET",
    success: (data) => {
      chartData = data;
      handleLcChart();
    },
  });
};
$(document).ready(function () {
  loadQueue();
  getChartData();
  $.ajax({
    url: "/api/getclients",
    method: "GET",
    success: (data) => {
      queue = data;
      loadQueue();
    },
  });
});
