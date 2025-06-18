const fs = require('fs');
const path = require('path');
const { exit } = require('process');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

let cnt = 0;
let visited = new Array(input.length).fill(false);
const d = 'quack';

if (input.length % 5 !== 0) {
    console.log(-1);
    process.exit();
}


function check_duck(i) {
    let idx = 0;
    let isRight = true;
    for (let j = i; j < input.length; j++) {
        if (input[j] === d[idx] && visited[j] === false) {  // 한 마리의 오리가 얼마나 많이 울었는지
            visited[j] = true;
            if (d[idx] === 'k') {
                if (isRight) {    // 한 오리가 여러 번 울 때, 제일 처음 운 경우
                    cnt += 1;
                    isRight = false;     
                };
                idx = 0;    // 찾은 한 마리가 얼마나 많이 울 수 있는지 확인
            } else {
                idx += 1;
            };
        } ;
    };
};



for (let i = 0; i < input.length; i++) {
    check_duck(i);
};


console.log(cnt === 0 || visited.includes(false) ? -1 : cnt);