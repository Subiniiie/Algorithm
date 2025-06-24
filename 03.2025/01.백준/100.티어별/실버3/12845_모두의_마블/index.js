const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    "/dev/stdin" : path.join(__dirname, "input.txt")
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const n = input[0][0];
const cards = input[1];

let gold = 0;

let maxNum = 0;
let maxIdx = 0;

for (let i = 0; i < n; i++) {
    if (maxNum < cards[i]) {
        maxNum = cards[i];
        maxIdx = i;
    };
};

while (cards.length > 0) {
    if (cards.length > 1) {
        if (maxIdx > 0 && maxIdx < n - 1) {
            if (cards[maxIdx-1] > cards[maxIdx+1]) {
                gold += cards[maxIdx] + cards[maxIdx-1];
                cards.splice(maxIdx-1, 1);
                maxIdx -= 1;
            } else {
                gold += cards[maxIdx] + cards[maxIdx+1];
                cards.splice(maxIdx+1, 1);
            };
        } else if (maxIdx === 0) {
            gold += cards[maxIdx] + cards[maxIdx+1];
            cards.splice(maxIdx+1, 1);
        } else {
            gold += cards[maxIdx] + cards[maxIdx-1];
            cards.splice(maxIdx-1, 1);
            maxIdx -= 1;
        }
    } else {
        if (gold === 0) {
            gold += cards[0];
        };
        break;
    };
};

console.log(gold)