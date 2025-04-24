const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim());

let s = 0;

const t = Number(input[0]);

for (let i = 1; i <= t; i++) {
    const w = input[i];
    let c = [];
    c.push(w[0]);
    const l = w.length;
    if (l === 1) {
        s += 1;
    } else {
        for (let z = 1; z < l; z++) {
            if (w[z - 1] !== w[z] && c.includes(w[z])) {
                break; 
            } else if (!c.includes(w[z])) {
                c.push(w[z]);
            };
            if (z === l - 1) {
                s += 1;
            };
        };
    };
};

console.log(s)