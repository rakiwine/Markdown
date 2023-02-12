let TexasPoker = require('./TexasPoker');

// 分池
let calcPot = function (anti, gameUser) {

    let potArr = [];

    // 筹码数量排序 由小到大
    let a = gameUser.sort(function (p1, p2) {
        return p1.totalBet - p2.totalBet;
    });

    let prevTotalBet = 0;

    let dealAntiFlag = False;
    let gameUser_len = gameUser.length;
    let User = gameUser[gameUser_len - 1];
    if (User["currentBetAnti"] !== 0) {
        dealAntiFlag = True;
        User.totalBet = User.totalBet - anti;
    }

    console.info("anti", anti);
    gameUser.forEach(function (item, index) {
        if (item.totalBet - prevTotalBet > 0) {
            let sum = (item.totalBet - prevTotalBet) * (gameUser.length - index);

            if (dealAntiFlag) {
                dealAntiFlag = False;
                sum = sum + anti;
            }

            potArr.push({
                pot: sum,
                userArr: gameUser.slice(index, gameUser.length)
            });

            prevTotalBet = item.totalBet;
        }
    });

    return potArr;
};

let room = {};
let winMap = {};
let winUserArrList = [];
let playingUserArr = [];

// room.gameUser = [
//   {
//     "id": "1561630607241515061",
//     "name": "辛咏志",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607241515061",
//     "jetton": 59925,
//     "operationType": 0,
//     "seatNumber": 0,
//     "currentBet": 0,
//     "totalBet": 200,
//     "currentBetAnti": 0,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "lastWinBet": 40025,
//     "pkArr": [],
//     "cardType": None,
//     "winBet": 0
//   },
//   {
//     "id": "1561630607291846661",
//     "name": "勾修筠",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607291846661",
//     "jetton": 19725,
//     "operationType": 0,
//     "seatNumber": 3,
//     "currentBet": 0,
//     "totalBet": 50,
//     "currentBetAnti": 0,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "lastWinBet": 0,
//     "pkArr": [],
//     "cardType": None,
//     "winBet": 0
//   },
//   {
//     "id": "1561630607254097979",
//     "name": "牵雅美",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607254097979",
//     "jetton": 0,
//     "operationType": 0,
//     "seatNumber": 1,
//     "currentBet": 0,
//     "totalBet": 100,
//     "currentBetAnti": 0,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "lastWinBet": -19850,
//     "pkArr": [],
//     "cardType": None,
//     "winBet": 0
//   },
//   {
//     "id": "1561630607270875149",
//     "name": "孟昊磊",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607270875149",
//     "jetton": 0,
//     "operationType": 0,
//     "seatNumber": 2,
//     "currentBet": 0,
//     "totalBet": 200,
//     "currentBetAnti": 0,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "winBet": 0,
//     "lastWinBet": -19950,
//     "pkArr": [],
//     "cardType": None
//   },
//   {
//     "id": "1561630607312818201",
//     "name": "森芳懿",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607312818201",
//     "jetton": 0,
//     "operationType": 0,
//     "seatNumber": 4,
//     "currentBet": 0,
//     "totalBet": 20000,
//     "currentBetAnti": 100,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "lastWinBet": 0,
//     "pkArr": [],
//     "cardType": None,
//     "winBet": 0
//   },
//   {
//     "id": "1561630607312818202",
//     "name": "森芳",
//     "isAI": 1,
//     "headPortraitUrl": None,
//     "gameId": "237153861159092224",
//     "userId": "1561630607312818202",
//     "jetton": 0,
//     "operationType": 0,
//     "seatNumber": 4,
//     "currentBet": 0,
//     "totalBet": 20000,
//     "currentBetAnti": 100,
//     "isCollocation": False,
//     "autoAbandon": 2,
//     "lastWinBet": 0,
//     "pkArr": [],
//     "cardType": None,
//     "winBet": 0
//   }
// ];
room.gameUser = [
  {
    "id": "1561630607241515061",
    "name": "辛咏志",
    "isAI": 1,
    "headPortraitUrl": None,
    "gameId": "237153861159092224",
    "userId": "1561630607241515061",
    "jetton": 59925,
    "operationType": 0,
    "seatNumber": 0,
    "currentBet": 0,
    "totalBet": 200,
    "currentBetAnti": 0,
    "isCollocation": False,
    "autoAbandon": 2,
    "lastWinBet": 40025,
    "pkArr": [],
    "cardType": None,
    "winBet": 0
  },
  {
    "id": "1561630607291846661",
    "name": "勾修筠",
    "isAI": 1,
    "headPortraitUrl": None,
    "gameId": "237153861159092224",
    "userId": "1561630607291846661",
    "jetton": 19725,
    "operationType": 0,
    "seatNumber": 3,
    "currentBet": 0,
    "totalBet": 50,
    "currentBetAnti": 0,
    "isCollocation": False,
    "autoAbandon": 2,
    "lastWinBet": 0,
    "pkArr": [],
    "cardType": None,
    "winBet": 0
  },
];


// let dealCards = [
//     "FK_2",
//     "FK_7",
//     "HT_6",
//     "FK_12",
//     "FK_10"
// ];
// 获取公共牌 MH FK HX HT
// 11 12 13 14
// J  Q  K  A
let dealCards = [
    "MH_2",
    "FK_4",
    "HX_6",
    "HT_10",
    "FK_12"
];

let room_userPkMap = {
    "1561630607241515061": [
        "FK_8",
        "HX_9"
    ],
    "1561630607291846661": [
        "HT_9",
        "HX_8"
    ]
};
// let room_userPkMap = {
//     "1561630607241515061": [
//         "FK_6",
//         "HT_5"
//     ],
//     "1561630607291846661": [
//         "HX_12",
//         "HT_14"
//     ],
//     "1561630607254097979": [
//         "HT_12",
//         "MH_6"
//     ],
//     "1561630607270875149": [
//         "HX_3",
//         "HT_7"
//     ],
//     "1561630607312818201": [
//         "MH_5",
//         "FK_9"
//     ],
//     "1561630607312818202": [
//         "MH_2",
//         "HX_8"
//     ]
// };

room.gameUser.forEach(function (userItem) {
    if (userItem.operationType !== 3) {
        playingUserArr.push(userItem);
    }
});

let potArr = calcPot(0, room.gameUser);

let userIdJetton = {};
playingUserArr.forEach(function (playingUser) {
    userIdJetton[playingUser.id] = playingUser.jetton
});

// 没有弃牌的玩家 记录七张牌 返回牌型
room.gameUser.forEach(function (item) {
    // 0未进行任何操作 1加注 2跟注 3弃牌 4看牌 5allin 6Straddle 7小盲 8大盲
    if (item.operationType !== 3) {
        let userCards = room_userPkMap[item.id];
        let userAllPk = dealCards.concat(userCards);

        let cardType = TexasPoker.score(userAllPk);
        item.pkArr = userCards;
        item.cardType = cardType;
    } else {
        item.cardType = {
            type: 11,
            resultArr: [],
            compareFLag: []
        };
    }
});

potArr.forEach(function (item) {
    let pot = item.pot;
    let userArr = item.userArr;

    //根据牌型大小排序
    userArr.sort(function (p1, p2) {
        if (p1.cardType.type === p2.cardType.type) {
            for (let i = 0; i < p1.cardType.compareFLag.length; i++) {
                let compareNum1 = p1.cardType.compareFLag[i];
                let compareNum2 = p2.cardType.compareFLag[i];
                if (compareNum1 !== compareNum2) {
                    return compareNum2 - compareNum1;
                }
            }
            return 0;
        } else {
            return p1.cardType.type - p2.cardType.type;
        }

    });

    //获取赢的用户
    let winUserArr = [userArr[0]];

    let compareStr = userArr[0].cardType.type + "," + userArr[0].cardType.compareFLag.join(",");
    //判断相同牌型相同大小的用户
    for (let i = 1; i < userArr.length; i++) {
        let s = userArr[i].cardType.type + "," + userArr[i].cardType.compareFLag.join(",");
        if (s !== compareStr) {
            break;
        }
        winUserArr.push(userArr[i]);
    }

    winUserArr.forEach(function (item, index) {
        let fPot = Math.floor(pot / (winUserArr.length - index));
        pot = pot - fPot;

        if (!item["winBet"]) {
            item["winBet"] = 0;
        }

        item["winBet"] = item["winBet"] + fPot;
        item.jetton = item.jetton + fPot;

        if (!winMap[item.id]) {
            winUserArrList.push(item);
            winMap[item.id] = item;
        }

    });
});

playingUserArr.forEach(function (item) {
    if (!item["winBet"]) {
        item["winBet"] = 0;
    }
    item["winBet"] = item["winBet"] - item.totalBet;
});

if (winUserArrList.length > 1) {

    let show = False;
    let showId = None;
    winUserArrList.forEach(function (winUser) {
        let totalBet = winUser["totalBet"];
        let winBet = winUser["winBet"];
        if (totalBet + winBet === 200 && !showId) {

            showId = winUser.id;
            show = True;
        }
    });

    if (show) {
        winUserArrList.forEach(function (winUser) {

            let oldJetton = userIdJetton[winUser.id];
            let jetton = winUser["jetton"];
            let totalBet = winUser["totalBet"];
            let winBet = winUser["winBet"];

            let userCardsList = room_userPkMap;

            console.info(potArr);
            // console.info(!JSON.parse(gameUserString));
            console.info(!dealCards);
            console.info(!userCardsList);

            console.info(
                "roomId",
                "赢家记录",
                room["bigBlinds"] === room["anti"],
                oldJetton + totalBet + winBet === jetton,
                totalBet + winBet === 200,
                oldJetton, totalBet, winBet, jetton
            );

            console.info()
        })
    }
}

console.info(winUserArrList);
console.info(playingUserArr);
console.info(132132);