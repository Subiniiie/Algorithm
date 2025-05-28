const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number))

const N = input[0][0];
let D = new Array(N+1).fill(0);

for (let i = 1; i <= N; i++) {
    const finishedDay = i + input[i][0] - 1;
    console.log('상담이 끝나는 날', finishedDay)
    if (finishedDay <= N) {
        // 하루 상담이 아니면
        if (i !== finishedDay) {
            console.log('하루 상담x', D[finishedDay], D[i] + input[i][1])
            D[finishedDay] = Math.max(D[finishedDay], D[i] + input[i][1])
            // 하루 상담이면
        } else {
            console.log('하루 상담o', D[finishedDay], input[i][1])
            D[finishedDay] = Math.max(D[finishedDay], input[i][1]);
        }
    };
    console.log('최종 변경', D)
};

console.log(D[N])