const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '011_input.txt')
).toString().trim().split('\n').map(Number);

const N = input[0];
let A = new Array(N).fill(0);

for (let i = 1; i <= N; i++) {
    A[i - 1] = input[i];
};

let stack = new Array();
let num = 1;
let result = true;
let answer = '';

for (let i = 0; i < N; i++) {
    let su = A[i];
    
    if (su >= num) {
        while (su >= num) {
            stack.push(num);
            num += 1;
            answer += "+\n"
        }
        stack.pop()
        answer += "-\n"
    } else {
        let n = stack.pop()

        if (n > su) {
            console.log('NO')
            result = false;
            break
        } else {
            answer += '-\n'
        }
    }
}

if (result) {
    console.log(answer)
}