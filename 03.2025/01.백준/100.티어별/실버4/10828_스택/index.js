const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" "))


const N = Number(input[0][0]);
let order = '';
let answer = '';
let stack = new Array();

function orderNum(order, num) {
    if (order === 'push') {
        stack.push(num);
    }
};

function justOrder(order) {
    if (order === 'pop') {
        if (stack.length === 0) {
            answer += "-1\n"
        } else {
            answer += (stack.pop() + "\n")
        }
    } else if (order === 'size') {
        answer += (stack.length + "\n")
    } else if (order === 'empty') {
        if (stack.length === 0) {
            answer += "1\n"
        } else {
            answer += "0\n"
        }
    } else {
        if (stack.length === 0) {
            answer += "-1\n"
        } else {
            answer += (stack[stack.length - 1] + "\n")
        }
    }
};

for (let i = 1; i <= N; i++) {
    if (input[i].length === 2) {
        order = input[i][0];
        const num = Number(input[i][1]);
        orderNum(order, num);
    } else {
        order = input[i][0];
        justOrder(order);
    };
};

console.log(answer)