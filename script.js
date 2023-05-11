const timeDiv = document.getElementById("time");

function getTime() {
    let now = new Date();

    let hour = now.getHours();
    let minute = now.getMinutes();
    let second = now.getSeconds();

    hour = padZero(hour);
    minute = padZero(minute);
    second = padZero(second);

    timeDiv.textContent = `${hour}시 ${minute}분 ${second}초`;
}

function padZero(data) {
    return data < 10 ? `0${data}` : data;
}

setInterval(getTime, 1000);
getTime();
