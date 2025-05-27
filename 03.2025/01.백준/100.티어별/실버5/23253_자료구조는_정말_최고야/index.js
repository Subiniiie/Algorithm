const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" "))

const [N, M] = input[0].map(Number);
const stacks = [];

for (let i = 1; i < input.length; i += 2) {
    const stack = input[i+1].map(Number);
    stacks.push(stack);
}

let possible = true;

for (const stack of stacks) {
    for (let i = 0; i < stack.length - 1; i++) {
        if (stack[i] < stack[i+1]) {
            possible = false;
            break;
        }
    }
    if (!possible) {
        break
    }
}

console.log(possible ? "Yes" : "No")