let takeSeatMap = [12,12,132,456];
if (takeSeatMap) {
    console.info(1)
}

let seatNumList = [0, 1, 2, 3, 4, 5, 6, 7, 8];
let onSeatNumList = Object.keys(takeSeatMap).map(function (onSeat) {
    return Number(onSeat)
});

console.info(onSeatNumList);