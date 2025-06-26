const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().trim().split("\n").map((el) => el.trim().split(" "));

const N = Number(input[0][0]);
const P = input[1].map(Number);
let arr = input.slice(2, N+2).map((el) => el.map(Number));

let dic = {};

for (let i = 0; i < arr.length; i++) {
    const a = arr[i][0];
    const b = arr[i][1];

    if (a in dic) {
        dic[a].push(b);
    } else {
        dic[a] = [b];
    };
};

let totalTime = 0;
let previousLevelUsed = false;

for (let i = 1; i <= P.length; i++) {
  const need = P[i - 1];
  const candidates = (dic[i] || []).sort((a, b) => a - b);
  const selected = candidates.slice(0, need).sort((a, b) => a - b);
  

  totalTime += selected.reduce((sum, t) => sum + t, 0);

  for (let j = 0; j < selected.length - 1; j++) {
    totalTime += selected[j+1] - selected[j];
  };

  if (previousLevelUsed && need > 0) {
    totalTime += 60;
  };

  previousLevelUsed = need > 0;
};

console.log(totalTime)
