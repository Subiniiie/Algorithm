const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    "/dev/stdin" : path.join(__dirname, "input.txt")
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const n = input[0][0];
let cards = input[1];
cards = cards.sort(function(a, b) {
    if (a>b) return -1;
    if (a===b) return 0;
    if (a<b) return 1;
});

let gold = 0;

if (n === 0) {
    gold = cards[0];
} else {
    for (let i = 0; i < n - 1; i++) {
        gold += cards[i] + cards[i+1];
        cards[i+1] = Math.max(cards[i], cards[i+1]);
    };
};

console.log(gold)