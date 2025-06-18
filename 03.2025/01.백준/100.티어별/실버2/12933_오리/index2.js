const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

const strLenth = input.length;
let cnt = 0;
let visited = new Array(strLenth).fill(false);
const duck = 'quack';

if (strLenth % 5 !== 0) {
    console.log(-1);
    process.exit();
};


function checkDuck(i) {
    let idx = 0;
    let oneDuck = false;

    for (let j = i; j < strLenth; j++) {
        if (duck[idx] === input[j] && !visited[j]) {
            visited[j] = true;
            if (idx === 4) {
                if (!oneDuck) {
                    cnt += 1;
                    oneDuck = true;
                };
                idx = 0;
            } else {
                idx += 1;
            };
        };
    };
};

for (let i = 0; i < strLenth; i++) {
        checkDuck(i);
};

console.log(cnt === 0 || visited.includes(false) ? -1 : cnt)